#!/usr/bin/env python3
"""
CodeAct Analyzer - Measures model understanding vs pattern matching.

Analyzes detection outputs against CodeAct annotations to compute:
- ROOT_CAUSE hit rate (did model find actual cause?)
- DECOY trap rate (did model fall for fake suspicious code?)
- Fix recognition rate (did model recognize patches work?)
- Line-level precision (did model point to exact lines?)
"""

import json
import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


PROJECT_ROOT = Path(__file__).parent.parent.parent


@dataclass
class CodeActMatch:
    """Result of matching a detection line to a CodeAct."""
    line: int
    code_act_id: str
    code_act_type: str
    security_function: str
    rationale: str = ""


@dataclass
class SampleAnalysis:
    """Analysis results for a single sample."""
    sample_id: str
    variant: str  # ms, tr, df
    detector_model: str

    # Lines mentioned in detection
    lines_flagged: list[int] = field(default_factory=list)

    # CodeAct matches
    matches: list[CodeActMatch] = field(default_factory=list)

    # Counts by security function
    root_cause_hits: int = 0
    secondary_vuln_hits: int = 0
    prereq_hits: int = 0
    benign_hits: int = 0
    decoy_hits: int = 0
    unrelated_hits: int = 0

    # Ground truth
    total_root_causes: int = 0
    total_decoys: int = 0
    total_secondary_vulns: int = 0

    # Computed metrics
    @property
    def root_cause_found(self) -> bool:
        return self.root_cause_hits > 0

    @property
    def root_cause_precision(self) -> float:
        if not self.lines_flagged:
            return 0.0
        return self.root_cause_hits / len(self.lines_flagged)

    @property
    def root_cause_recall(self) -> float:
        if self.total_root_causes == 0:
            return 0.0
        return self.root_cause_hits / self.total_root_causes

    @property
    def decoy_trap_rate(self) -> float:
        if self.total_decoys == 0:
            return 0.0
        return self.decoy_hits / self.total_decoys

    @property
    def benign_flag_rate(self) -> float:
        if not self.lines_flagged:
            return 0.0
        return self.benign_hits / len(self.lines_flagged)

    @property
    def precision(self) -> float:
        """Precision = (ROOT_CAUSE + SECONDARY_VULN) / total flagged"""
        if not self.lines_flagged:
            return 0.0
        valid = self.root_cause_hits + self.secondary_vuln_hits
        return valid / len(self.lines_flagged)

    def to_dict(self) -> dict:
        return {
            "sample_id": self.sample_id,
            "variant": self.variant,
            "detector_model": self.detector_model,
            "lines_flagged": self.lines_flagged,
            "matches": [
                {
                    "line": m.line,
                    "code_act_id": m.code_act_id,
                    "code_act_type": m.code_act_type,
                    "security_function": m.security_function
                }
                for m in self.matches
            ],
            "counts": {
                "root_cause_hits": self.root_cause_hits,
                "secondary_vuln_hits": self.secondary_vuln_hits,
                "prereq_hits": self.prereq_hits,
                "benign_hits": self.benign_hits,
                "decoy_hits": self.decoy_hits,
                "unrelated_hits": self.unrelated_hits
            },
            "ground_truth": {
                "total_root_causes": self.total_root_causes,
                "total_decoys": self.total_decoys,
                "total_secondary_vulns": self.total_secondary_vulns
            },
            "metrics": {
                "root_cause_found": self.root_cause_found,
                "root_cause_precision": round(self.root_cause_precision, 3),
                "root_cause_recall": round(self.root_cause_recall, 3),
                "decoy_trap_rate": round(self.decoy_trap_rate, 3),
                "benign_flag_rate": round(self.benign_flag_rate, 3),
                "precision": round(self.precision, 3)
            }
        }


class CodeActAnnotation:
    """Loads and queries CodeAct annotations for a sample."""

    def __init__(self, variant: str, sample_id: str):
        self.variant = variant
        self.sample_id = sample_id
        self.data = None
        self.line_to_codeact: dict[int, dict] = {}
        self._load()

    def _get_annotation_path(self) -> Path:
        variant_dirs = {
            "ms": "minimalsanitized",
            "tr": "trojan",
            "df": "differential"
        }
        variant_dir = variant_dirs.get(self.variant, self.variant)
        return PROJECT_ROOT / f"samples/tc/{variant_dir}/code_acts_annotation/{self.sample_id}.yaml"

    def _load(self):
        path = self._get_annotation_path()
        if not path.exists():
            raise FileNotFoundError(f"Annotation not found: {path}")

        with open(path) as f:
            self.data = yaml.safe_load(f)

        self._build_line_mapping()

    def _build_line_mapping(self):
        """Build line → code_act lookup based on variant type."""

        if self.variant == "ms":
            self._build_ms_mapping()
        elif self.variant == "tr":
            self._build_tr_mapping()
        elif self.variant == "df":
            self._build_df_mapping()

    def _build_ms_mapping(self):
        """Build mapping for minimalsanitized (full code act listing)."""
        # Use line_to_code_act if available
        if "line_to_code_act" in self.data:
            code_act_funcs = self.data.get("code_act_security_functions", {})
            code_acts_by_id = {ca["id"]: ca for ca in self.data.get("code_acts", [])}

            for line, ca_id in self.data["line_to_code_act"].items():
                line_num = int(line)
                sec_func = code_act_funcs.get(ca_id, "UNKNOWN")
                ca_data = code_acts_by_id.get(ca_id, {})

                self.line_to_codeact[line_num] = {
                    "code_act_id": ca_id,
                    "code_act_type": ca_data.get("type", "UNKNOWN"),
                    "security_function": sec_func,
                    "rationale": ca_data.get("rationale", "")
                }
        else:
            # Fall back to code_acts array
            for ca in self.data.get("code_acts", []):
                lines = ca.get("lines", [])
                if isinstance(lines, int):
                    lines = [lines]
                for line in lines:
                    self.line_to_codeact[line] = {
                        "code_act_id": ca.get("id", ""),
                        "code_act_type": ca.get("type", "UNKNOWN"),
                        "security_function": ca.get("security_function", "UNKNOWN"),
                        "rationale": ca.get("rationale", "")
                    }

    def _build_tr_mapping(self):
        """Build mapping for trojan (base vuln + decoys)."""
        # First load base vulnerability lines
        base_vuln = self.data.get("base_vulnerability", {})
        vuln_lines = base_vuln.get("vulnerable_lines", [])
        for line in vuln_lines:
            self.line_to_codeact[line] = {
                "code_act_id": "BASE_VULN",
                "code_act_type": base_vuln.get("type", "UNKNOWN"),
                "security_function": "ROOT_CAUSE",
                "rationale": "Base vulnerability from minimalsanitized"
            }

        # Add decoy injections
        for inj in self.data.get("injections", []):
            location = inj.get("location", {})
            lines = location.get("lines", [])
            for line in lines:
                self.line_to_codeact[line] = {
                    "code_act_id": inj.get("id", ""),
                    "code_act_type": inj.get("type", "UNKNOWN"),
                    "security_function": inj.get("security_function", "DECOY"),
                    "rationale": "; ".join(inj.get("safe_because", []))
                }

    def _build_df_mapping(self):
        """Build mapping for differential (fixed code)."""
        for ca in self.data.get("code_acts", []):
            fixed = ca.get("fixed", {})
            lines = fixed.get("lines", fixed.get("line", []))
            if isinstance(lines, int):
                lines = [lines]

            for line in lines:
                self.line_to_codeact[line] = {
                    "code_act_id": ca.get("id", ""),
                    "code_act_type": ca.get("type", "UNKNOWN"),
                    "security_function": fixed.get("security_function", "BENIGN"),
                    "rationale": fixed.get("rationale", ""),
                    "transition": ca.get("transition", "")
                }

    def lookup(self, line: int) -> Optional[dict]:
        """Look up code act for a line number."""
        return self.line_to_codeact.get(line)

    def get_root_cause_lines(self) -> list[int]:
        """Get all lines marked as ROOT_CAUSE."""
        return [ln for ln, ca in self.line_to_codeact.items()
                if ca["security_function"] == "ROOT_CAUSE"]

    def get_decoy_lines(self) -> list[int]:
        """Get all lines marked as DECOY."""
        return [ln for ln, ca in self.line_to_codeact.items()
                if ca["security_function"] == "DECOY"]

    def get_secondary_vuln_lines(self) -> list[int]:
        """Get all lines marked as SECONDARY_VULN."""
        return [ln for ln, ca in self.line_to_codeact.items()
                if ca["security_function"] == "SECONDARY_VULN"]


def extract_lines_from_detection(detection: dict) -> list[int]:
    """Extract line numbers from detection output.

    Primary source: vulnerable_lines array in each finding.
    Fallback: parse line numbers from location/explanation text.
    """
    lines = set()

    prediction = detection.get("prediction", {})
    vulnerabilities = prediction.get("vulnerabilities", [])

    for vuln in vulnerabilities:
        # Primary: use vulnerable_lines field if present
        vuln_lines = vuln.get("vulnerable_lines", [])
        if vuln_lines:
            for ln in vuln_lines:
                if isinstance(ln, int):
                    lines.add(ln)
                elif isinstance(ln, str) and ln.isdigit():
                    lines.add(int(ln))

        # Fallback: parse from location and explanation text
        if not vuln_lines:
            location = vuln.get("location", "")

            # Pattern: "line 45", "lines 45-50", "L45", etc.
            line_patterns = [
                r'[Ll]ine[s]?\s*(\d+)',
                r'[Ll]ines?\s*(\d+)\s*[-–]\s*(\d+)',
                r'[Ll](\d+)',
                r':(\d+)',
            ]

            for pattern in line_patterns:
                matches = re.findall(pattern, str(location))
                for match in matches:
                    if isinstance(match, tuple):
                        start, end = int(match[0]), int(match[1])
                        lines.update(range(start, end + 1))
                    else:
                        lines.add(int(match))

    return sorted(lines)


def analyze_sample(
    variant: str,
    sample_id: str,
    detector_model: str,
    detection: dict
) -> SampleAnalysis:
    """Analyze a single detection output against CodeAct annotations."""

    # Load annotation
    annotation = CodeActAnnotation(variant, sample_id)

    # Extract lines from detection
    lines_flagged = extract_lines_from_detection(detection)

    # Initialize analysis
    analysis = SampleAnalysis(
        sample_id=sample_id,
        variant=variant,
        detector_model=detector_model,
        lines_flagged=lines_flagged,
        total_root_causes=len(annotation.get_root_cause_lines()),
        total_decoys=len(annotation.get_decoy_lines()),
        total_secondary_vulns=len(annotation.get_secondary_vuln_lines())
    )

    # Match each flagged line to code acts
    for line in lines_flagged:
        ca = annotation.lookup(line)
        if ca:
            match = CodeActMatch(
                line=line,
                code_act_id=ca["code_act_id"],
                code_act_type=ca["code_act_type"],
                security_function=ca["security_function"],
                rationale=ca.get("rationale", "")
            )
            analysis.matches.append(match)

            # Count by security function
            sf = ca["security_function"]
            if sf == "ROOT_CAUSE":
                analysis.root_cause_hits += 1
            elif sf == "SECONDARY_VULN":
                analysis.secondary_vuln_hits += 1
            elif sf == "PREREQ":
                analysis.prereq_hits += 1
            elif sf == "BENIGN":
                analysis.benign_hits += 1
            elif sf == "DECOY":
                analysis.decoy_hits += 1
            elif sf == "UNRELATED":
                analysis.unrelated_hits += 1

    return analysis


def analyze_detector_on_variant(
    detector_model: str,
    variant: str,
    limit: int = None
) -> list[SampleAnalysis]:
    """Analyze all samples for a detector on a variant."""

    variant_dirs = {
        "ms": "minimalsanitized",
        "tr": "trojan",
        "df": "differential"
    }
    variant_dir = variant_dirs.get(variant, variant)

    # Get detection files
    detection_dir = PROJECT_ROOT / f"results/detection/llm/{detector_model}/tc/{variant_dir}"
    if not detection_dir.exists():
        print(f"No detection results for {detector_model} on tc/{variant_dir}")
        return []

    # Get annotation files to know which samples have annotations
    annotation_dir = PROJECT_ROOT / f"samples/tc/{variant_dir}/code_acts_annotation"
    annotated_samples = {f.stem for f in annotation_dir.glob("*.yaml")}

    results = []
    detection_files = sorted(detection_dir.glob("d_*.json"))

    for i, det_file in enumerate(detection_files):
        if limit and i >= limit:
            break

        sample_id = det_file.stem.replace("d_", "")

        # Check if we have annotation for this sample
        if sample_id not in annotated_samples:
            continue

        with open(det_file) as f:
            detection = json.load(f)

        try:
            analysis = analyze_sample(variant, sample_id, detector_model, detection)
            results.append(analysis)
        except Exception as e:
            print(f"Error analyzing {sample_id}: {e}")

    return results


def compute_aggregate_metrics(analyses: list[SampleAnalysis]) -> dict:
    """Compute aggregate metrics across multiple samples."""
    if not analyses:
        return {}

    n = len(analyses)

    return {
        "sample_count": n,
        "root_cause_found_rate": sum(1 for a in analyses if a.root_cause_found) / n,
        "avg_root_cause_precision": sum(a.root_cause_precision for a in analyses) / n,
        "avg_root_cause_recall": sum(a.root_cause_recall for a in analyses) / n,
        "avg_decoy_trap_rate": sum(a.decoy_trap_rate for a in analyses) / n,
        "avg_benign_flag_rate": sum(a.benign_flag_rate for a in analyses) / n,
        "avg_precision": sum(a.precision for a in analyses) / n,
        "total_root_cause_hits": sum(a.root_cause_hits for a in analyses),
        "total_decoy_hits": sum(a.decoy_hits for a in analyses),
        "total_secondary_hits": sum(a.secondary_vuln_hits for a in analyses),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze detection outputs with CodeActs")
    parser.add_argument("--detector", "-d", required=True, help="Detector model")
    parser.add_argument("--variant", "-v", required=True, choices=["ms", "tr", "df"], help="Variant")
    parser.add_argument("--sample", "-s", help="Single sample ID")
    parser.add_argument("--limit", "-l", type=int, help="Limit samples")
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    if args.sample:
        # Analyze single sample
        variant_dirs = {"ms": "minimalsanitized", "tr": "trojan", "df": "differential"}
        det_path = PROJECT_ROOT / f"results/detection/llm/{args.detector}/tc/{variant_dirs[args.variant]}/d_{args.sample}.json"

        with open(det_path) as f:
            detection = json.load(f)

        analysis = analyze_sample(args.variant, args.sample, args.detector, detection)
        print(json.dumps(analysis.to_dict(), indent=2))
    else:
        # Analyze all samples
        analyses = analyze_detector_on_variant(args.detector, args.variant, args.limit)

        if args.verbose:
            for a in analyses:
                print(f"{a.sample_id}: RC_found={a.root_cause_found}, decoy_trap={a.decoy_trap_rate:.2f}")

        metrics = compute_aggregate_metrics(analyses)
        print("\n=== Aggregate Metrics ===")
        print(json.dumps(metrics, indent=2))

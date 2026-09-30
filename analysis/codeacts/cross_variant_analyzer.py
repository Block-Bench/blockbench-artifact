#!/usr/bin/env python3
"""
Cross-Variant Analyzer - Compares model performance across ms/tr/df variants.

Computes:
- Contamination Index: (ms_accuracy - tr_accuracy) / ms_accuracy
- Understanding Score: Combination of metrics
- Pattern Matching Index: Based on decoy trap rate
"""

import json
from pathlib import Path
from dataclasses import dataclass

from codeact_analyzer import (
    analyze_detector_on_variant,
    compute_aggregate_metrics,
    SampleAnalysis
)


PROJECT_ROOT = Path(__file__).parent.parent.parent

DETECTORS = [
    "claude-opus-4-5",
    "deepseek-v3-2",
    "gemini-3-pro",
    "gpt-5.2",
    "grok-4-fast",
    "llama-4-maverick",
    "qwen3-coder-plus"
]


@dataclass
class CrossVariantAnalysis:
    """Cross-variant analysis for a detector."""
    detector: str

    # Per-variant metrics
    ms_metrics: dict
    tr_metrics: dict
    df_metrics: dict

    # Computed composite metrics
    @property
    def contamination_index(self) -> float:
        """Higher = more reliance on memorization vs understanding."""
        ms_rate = self.ms_metrics.get("root_cause_found_rate", 0)
        tr_rate = self.tr_metrics.get("root_cause_found_rate", 0)
        if ms_rate == 0:
            return 0.0
        return (ms_rate - tr_rate) / ms_rate

    @property
    def decoy_resistance(self) -> float:
        """1 - decoy_trap_rate. Higher = better understanding."""
        trap_rate = self.tr_metrics.get("avg_decoy_trap_rate", 0)
        return 1.0 - trap_rate

    @property
    def fix_recognition_rate(self) -> float:
        """1 - false_positive_rate on differential. Higher = recognizes fixes."""
        # In differential, any ROOT_CAUSE hit is a false positive
        df_rc_rate = self.df_metrics.get("root_cause_found_rate", 0)
        return 1.0 - df_rc_rate

    @property
    def understanding_score(self) -> float:
        """
        Composite score:
        - 40% ROOT_CAUSE found rate on trojan (hard test)
        - 30% Decoy resistance
        - 30% Fix recognition
        """
        tr_rc = self.tr_metrics.get("root_cause_found_rate", 0)
        return (
            0.4 * tr_rc +
            0.3 * self.decoy_resistance +
            0.3 * self.fix_recognition_rate
        )

    @property
    def pattern_matching_index(self) -> float:
        """
        Higher = more pattern matching behavior.
        Based on: decoy trap rate + benign flag rate
        """
        decoy_trap = self.tr_metrics.get("avg_decoy_trap_rate", 0)
        benign_flag = self.ms_metrics.get("avg_benign_flag_rate", 0)
        return (decoy_trap + benign_flag) / 2

    def to_dict(self) -> dict:
        return {
            "detector": self.detector,
            "variant_metrics": {
                "minimalsanitized": self.ms_metrics,
                "trojan": self.tr_metrics,
                "differential": self.df_metrics
            },
            "composite_metrics": {
                "contamination_index": round(self.contamination_index, 3),
                "decoy_resistance": round(self.decoy_resistance, 3),
                "fix_recognition_rate": round(self.fix_recognition_rate, 3),
                "understanding_score": round(self.understanding_score, 3),
                "pattern_matching_index": round(self.pattern_matching_index, 3)
            }
        }

    def summary_row(self) -> dict:
        """Summary row for comparison table."""
        return {
            "detector": self.detector,
            "ms_rc_rate": round(self.ms_metrics.get("root_cause_found_rate", 0) * 100, 1),
            "tr_rc_rate": round(self.tr_metrics.get("root_cause_found_rate", 0) * 100, 1),
            "contamination_idx": round(self.contamination_index * 100, 1),
            "decoy_trap": round(self.tr_metrics.get("avg_decoy_trap_rate", 0) * 100, 1),
            "fix_recognition": round(self.fix_recognition_rate * 100, 1),
            "understanding": round(self.understanding_score * 100, 1),
            "pattern_matching": round(self.pattern_matching_index * 100, 1)
        }


def analyze_detector_cross_variant(detector: str, verbose: bool = False) -> CrossVariantAnalysis:
    """Run cross-variant analysis for a single detector."""

    if verbose:
        print(f"Analyzing {detector}...")

    # Analyze each variant
    ms_analyses = analyze_detector_on_variant(detector, "ms")
    tr_analyses = analyze_detector_on_variant(detector, "tr")
    df_analyses = analyze_detector_on_variant(detector, "df")

    # Compute aggregate metrics
    ms_metrics = compute_aggregate_metrics(ms_analyses)
    tr_metrics = compute_aggregate_metrics(tr_analyses)
    df_metrics = compute_aggregate_metrics(df_analyses)

    return CrossVariantAnalysis(
        detector=detector,
        ms_metrics=ms_metrics,
        tr_metrics=tr_metrics,
        df_metrics=df_metrics
    )


def analyze_all_detectors(detectors: list[str] = None, verbose: bool = False) -> list[CrossVariantAnalysis]:
    """Analyze all detectors."""
    if detectors is None:
        detectors = DETECTORS

    results = []
    for detector in detectors:
        try:
            analysis = analyze_detector_cross_variant(detector, verbose)
            results.append(analysis)
        except Exception as e:
            print(f"Error analyzing {detector}: {e}")

    return results


def print_comparison_table(analyses: list[CrossVariantAnalysis]):
    """Print a comparison table."""

    print("\n" + "=" * 120)
    print("CROSS-VARIANT ANALYSIS: Understanding vs Pattern Matching")
    print("=" * 120)

    # Header
    print(f"{'Detector':<25} {'MS RC%':>8} {'TR RC%':>8} {'Contam%':>8} {'Decoy%':>8} {'FixRec%':>8} {'Underst':>8} {'PatMatch':>8}")
    print("-" * 120)

    # Sort by understanding score
    sorted_analyses = sorted(analyses, key=lambda a: a.understanding_score, reverse=True)

    for a in sorted_analyses:
        row = a.summary_row()
        print(f"{row['detector']:<25} {row['ms_rc_rate']:>7.1f}% {row['tr_rc_rate']:>7.1f}% "
              f"{row['contamination_idx']:>7.1f}% {row['decoy_trap']:>7.1f}% "
              f"{row['fix_recognition']:>7.1f}% {row['understanding']:>7.1f}% {row['pattern_matching']:>7.1f}%")

    print("=" * 120)
    print("\nLegend:")
    print("  MS RC%      = ROOT_CAUSE found rate on MinimalSanitized (with hints)")
    print("  TR RC%      = ROOT_CAUSE found rate on Trojan (no hints + decoys)")
    print("  Contam%     = Contamination Index: (MS-TR)/MS - higher = more memorization")
    print("  Decoy%      = Decoy trap rate - higher = more pattern matching")
    print("  FixRec%     = Fix recognition rate - higher = understands patches")
    print("  Underst     = Understanding Score (composite) - higher = better")
    print("  PatMatch    = Pattern Matching Index - higher = worse")


def save_results(analyses: list[CrossVariantAnalysis], output_path: Path):
    """Save detailed results to JSON."""
    results = {
        "summary": [a.summary_row() for a in analyses],
        "detailed": [a.to_dict() for a in analyses]
    }

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cross-variant CodeAct analysis")
    parser.add_argument("--detector", "-d", action="append", help="Specific detector(s)")
    parser.add_argument("--output", "-o", type=Path, help="Output JSON path")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    detectors = args.detector if args.detector else DETECTORS

    analyses = analyze_all_detectors(detectors, args.verbose)
    print_comparison_table(analyses)

    if args.output:
        save_results(analyses, args.output)
    else:
        # Default output
        output_path = PROJECT_ROOT / "code_acts/results/cross_variant_analysis.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        save_results(analyses, output_path)

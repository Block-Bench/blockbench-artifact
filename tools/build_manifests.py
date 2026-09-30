#!/usr/bin/env python3
"""Generate runs/<run>/MANIFEST.json by inspecting the run directories.

The manifest records what a run actually contains, including its gaps.
Gaps are recorded as data rather than left for a reader to discover.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "analysis"))

from judge_rules import JUDGES_MAJORITY, UNUSED_JUDGES, is_sample_file  # noqa: E402

# Expected sample counts differ by run: the Gold Standard subset was
# expanded from 34 to 106 between the January and May evaluations, so a
# January GS directory holding 34 files is complete, not short.
EXPECTED_BY_RUN = {
    "2026-01": {"gs": 34, "tc": 46},
    "2026-05": {"gs": 106, "negative": 100, "tc": 46},
}
DS_TIERS = {"tier1": 20, "tier2": 37, "tier3": 30, "tier4": 13}


def count(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    return sum(1 for p in directory.rglob("*.json") if is_sample_file(p))


def survey(root: Path) -> dict:
    """Map model -> subset -> variant -> file count."""
    tree: dict = defaultdict(lambda: defaultdict(dict))
    if not root.is_dir():
        return {}
    for model_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for subset_dir in sorted(p for p in model_dir.iterdir() if p.is_dir()):
            children = [p for p in subset_dir.iterdir() if p.is_dir()]
            if children:
                for variant_dir in sorted(children):
                    tree[model_dir.name][subset_dir.name][variant_dir.name] = count(variant_dir)
            else:
                tree[model_dir.name][subset_dir.name]["_"] = count(subset_dir)
    return {m: dict(s) for m, s in tree.items()}


def timestamps(root: Path, limit: int = 4000) -> list[str]:
    months = set()
    for i, path in enumerate(root.rglob("*.json")):
        if i >= limit:
            break
        try:
            stamp = json.loads(path.read_text()).get("timestamp")
        except (OSError, ValueError, AttributeError):
            continue
        if isinstance(stamp, str):
            months.add(stamp[:7])
    return sorted(months)


def find_gaps(detection: dict, run: str) -> list[str]:
    """Directories holding fewer samples than that run's subset expects."""
    expected_subsets = EXPECTED_BY_RUN.get(run, {})
    gaps = []
    for model, subsets in sorted(detection.items()):
        for subset, variants in sorted(subsets.items()):
            for variant, n in sorted(variants.items()):
                if subset == "ds":
                    expected = DS_TIERS.get(variant)
                else:
                    expected = expected_subsets.get(subset)
                if expected is None or n == 0 or n >= expected:
                    continue
                label = subset if variant == "_" else f"{subset}/{variant}"
                gaps.append(f"{model} {label}: {n}/{expected}")
    return gaps


def main() -> None:
    for run_dir in sorted((ROOT / "runs").iterdir()):
        if not run_dir.is_dir():
            continue
        detection = survey(run_dir / "detection")
        judge_root = run_dir / "judge"
        judges = sorted(p.name for p in judge_root.iterdir() if p.is_dir()) if judge_root.is_dir() else []

        manifest = {
            "run": run_dir.name,
            "evaluation_months": timestamps(run_dir / "detection"),
            "detector_models": sorted(detection),
            "subsets": sorted({s for v in detection.values() for s in v}),
            "judges_present": judges,
            "judges_used_for_published_numbers": list(JUDGES_MAJORITY),
            "judges_not_used": [j for j in UNUSED_JUDGES if j in judges],
            "file_counts": {
                "detection": count(run_dir / "detection"),
                "judge": count(judge_root),
                "traditional": count(run_dir / "traditional"),
            },
            "detection_coverage": detection,
            "expected_sample_counts": {
                **EXPECTED_BY_RUN.get(run_dir.name, {}),
                "ds_tiers": DS_TIERS,
            },
            "known_gaps": find_gaps(detection, run_dir.name),
        }

        out = run_dir / "MANIFEST.json"
        out.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"{out}: {len(manifest['known_gaps'])} gaps recorded")


if __name__ == "__main__":
    main()

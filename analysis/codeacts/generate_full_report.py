#!/usr/bin/env python3
"""
Generate comprehensive CodeAct metrics report across all models and variants.
"""

import json
from pathlib import Path
from codeact_analyzer import analyze_detector_on_variant, compute_aggregate_metrics

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

VARIANTS = ["ms", "tr", "df"]
VARIANT_NAMES = {
    "ms": "MinimalSanitized",
    "tr": "Trojan",
    "df": "Differential"
}


def generate_full_report():
    """Generate comprehensive metrics for all models and variants."""

    results = {}

    for detector in DETECTORS:
        print(f"Analyzing {detector}...")
        results[detector] = {}

        for variant in VARIANTS:
            analyses = analyze_detector_on_variant(detector, variant)
            metrics = compute_aggregate_metrics(analyses)
            results[detector][variant] = metrics

    return results


def print_detailed_table(results: dict):
    """Print detailed metrics table."""

    print("\n" + "=" * 140)
    print("CODEACT DETAILED METRICS BY MODEL AND VARIANT")
    print("=" * 140)

    # Header
    print(f"\n{'='*140}")
    print(f"{'MINIMALSANITIZED (with documentation hints)'}")
    print(f"{'='*140}")
    print(f"{'Detector':<22} {'Samples':>8} {'RC Found%':>10} {'RC Prec%':>10} {'RC Recall%':>10} {'SecVuln':>8} {'Benign%':>10} {'Precision%':>10}")
    print("-" * 140)

    for detector in DETECTORS:
        m = results[detector].get("ms", {})
        if m:
            print(f"{detector:<22} {m.get('sample_count', 0):>8} "
                  f"{m.get('root_cause_found_rate', 0)*100:>9.1f}% "
                  f"{m.get('avg_root_cause_precision', 0)*100:>9.1f}% "
                  f"{m.get('avg_root_cause_recall', 0)*100:>9.1f}% "
                  f"{m.get('total_secondary_hits', 0):>8} "
                  f"{m.get('avg_benign_flag_rate', 0)*100:>9.1f}% "
                  f"{m.get('avg_precision', 0)*100:>9.1f}%")

    print(f"\n{'='*140}")
    print(f"{'TROJAN (no documentation + decoys)'}")
    print(f"{'='*140}")
    print(f"{'Detector':<22} {'Samples':>8} {'RC Found%':>10} {'RC Prec%':>10} {'RC Recall%':>10} {'Decoy Trap%':>12} {'DecoyHits':>10} {'Precision%':>10}")
    print("-" * 140)

    for detector in DETECTORS:
        m = results[detector].get("tr", {})
        if m:
            print(f"{detector:<22} {m.get('sample_count', 0):>8} "
                  f"{m.get('root_cause_found_rate', 0)*100:>9.1f}% "
                  f"{m.get('avg_root_cause_precision', 0)*100:>9.1f}% "
                  f"{m.get('avg_root_cause_recall', 0)*100:>9.1f}% "
                  f"{m.get('avg_decoy_trap_rate', 0)*100:>11.1f}% "
                  f"{m.get('total_decoy_hits', 0):>10} "
                  f"{m.get('avg_precision', 0)*100:>9.1f}%")

    print(f"\n{'='*140}")
    print(f"{'DIFFERENTIAL (fixed/patched code)'}")
    print(f"{'='*140}")
    print(f"{'Detector':<22} {'Samples':>8} {'RC Found%':>10} {'RC Hits':>10} {'Benign%':>10} {'FalsePos':>10}")
    print("-" * 140)

    for detector in DETECTORS:
        m = results[detector].get("df", {})
        if m:
            # In differential, any RC hit is a false positive
            rc_hits = m.get('total_root_cause_hits', 0)
            print(f"{detector:<22} {m.get('sample_count', 0):>8} "
                  f"{m.get('root_cause_found_rate', 0)*100:>9.1f}% "
                  f"{rc_hits:>10} "
                  f"{m.get('avg_benign_flag_rate', 0)*100:>9.1f}% "
                  f"{'YES' if rc_hits > 0 else 'NO':>10}")

    # Summary comparison
    print(f"\n{'='*140}")
    print(f"{'CROSS-VARIANT COMPARISON'}")
    print(f"{'='*140}")
    print(f"{'Detector':<22} {'MS→TR Drop':>12} {'Contamination':>14} {'Decoy Resist':>13} {'Fix Recog':>11} {'Understanding':>14}")
    print("-" * 140)

    for detector in DETECTORS:
        ms = results[detector].get("ms", {})
        tr = results[detector].get("tr", {})
        df = results[detector].get("df", {})

        ms_rc = ms.get('root_cause_found_rate', 0)
        tr_rc = tr.get('root_cause_found_rate', 0)

        drop = (ms_rc - tr_rc) * 100
        contam = ((ms_rc - tr_rc) / ms_rc * 100) if ms_rc > 0 else 0
        decoy_resist = (1 - tr.get('avg_decoy_trap_rate', 0)) * 100
        fix_recog = (1 - df.get('root_cause_found_rate', 0)) * 100

        # Understanding score: 40% TR accuracy + 30% decoy resist + 30% fix recog
        understanding = 0.4 * tr_rc * 100 + 0.3 * decoy_resist + 0.3 * fix_recog

        print(f"{detector:<22} {drop:>11.1f}% {contam:>13.1f}% {decoy_resist:>12.1f}% {fix_recog:>10.1f}% {understanding:>13.1f}%")

    print("=" * 140)
    print("\nMetric Definitions:")
    print("  RC Found%     = % of samples where model found at least one ROOT_CAUSE line")
    print("  RC Prec%      = Of lines flagged, what % are ROOT_CAUSE")
    print("  RC Recall%    = Of all ROOT_CAUSE lines, what % did model find")
    print("  SecVuln       = Total SECONDARY_VULN hits (bonus findings)")
    print("  Decoy Trap%   = % of DECOY lines that model incorrectly flagged")
    print("  Benign%       = % of flagged lines that are actually BENIGN (safe code)")
    print("  MS→TR Drop    = Performance drop from MinimalSanitized to Trojan")
    print("  Contamination = (MS-TR)/MS - higher = more reliance on docs/memorization")
    print("  Decoy Resist  = 1 - decoy_trap_rate (higher = better)")
    print("  Fix Recog     = 1 - false_positive_on_fixed (higher = recognizes patches)")
    print("  Understanding = Composite score (higher = better true understanding)")


def save_report(results: dict, output_path: Path):
    """Save detailed results to JSON."""

    # Compute derived metrics
    summary = []
    for detector in DETECTORS:
        ms = results[detector].get("ms", {})
        tr = results[detector].get("tr", {})
        df = results[detector].get("df", {})

        ms_rc = ms.get('root_cause_found_rate', 0)
        tr_rc = tr.get('root_cause_found_rate', 0)

        contam = ((ms_rc - tr_rc) / ms_rc) if ms_rc > 0 else 0
        decoy_resist = 1 - tr.get('avg_decoy_trap_rate', 0)
        fix_recog = 1 - df.get('root_cause_found_rate', 0)
        understanding = 0.4 * tr_rc + 0.3 * decoy_resist + 0.3 * fix_recog

        summary.append({
            "detector": detector,
            "ms_root_cause_found_rate": round(ms_rc, 3),
            "ms_avg_precision": round(ms.get('avg_precision', 0), 3),
            "ms_avg_root_cause_recall": round(ms.get('avg_root_cause_recall', 0), 3),
            "ms_total_secondary_hits": ms.get('total_secondary_hits', 0),
            "ms_avg_benign_flag_rate": round(ms.get('avg_benign_flag_rate', 0), 3),
            "tr_root_cause_found_rate": round(tr_rc, 3),
            "tr_avg_precision": round(tr.get('avg_precision', 0), 3),
            "tr_avg_decoy_trap_rate": round(tr.get('avg_decoy_trap_rate', 0), 3),
            "tr_total_decoy_hits": tr.get('total_decoy_hits', 0),
            "df_root_cause_found_rate": round(df.get('root_cause_found_rate', 0), 3),
            "df_false_positives": df.get('total_root_cause_hits', 0),
            "contamination_index": round(contam, 3),
            "decoy_resistance": round(decoy_resist, 3),
            "fix_recognition": round(fix_recog, 3),
            "understanding_score": round(understanding, 3)
        })

    # Sort by understanding score
    summary.sort(key=lambda x: x['understanding_score'], reverse=True)

    output = {
        "summary": summary,
        "detailed_by_model": results
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {output_path}")
    return summary


if __name__ == "__main__":
    results = generate_full_report()
    print_detailed_table(results)

    output_path = PROJECT_ROOT / "code_acts/results/codeact_full_metrics.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary = save_report(results, output_path)

    # Print summary JSON
    print("\n" + "=" * 80)
    print("SUMMARY JSON (sorted by understanding score)")
    print("=" * 80)
    print(json.dumps(summary, indent=2))

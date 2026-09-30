"""Statistics for the BlockBench paper tables.

Mirrors src/aggregation/statistics.py in Block-Bench/evaluation (1000
bootstrap resamples, percentile interval, McNemar with continuity
correction) and adds the Holm correction the original pipeline lacked.

Standard library only, so the artifact runs without scipy.
"""

from __future__ import annotations

import math
import random

BOOTSTRAP_RESAMPLES = 1000
CONFIDENCE = 0.95


def bootstrap_ci(
    outcomes: list[bool],
    resamples: int = BOOTSTRAP_RESAMPLES,
    confidence: float = CONFIDENCE,
    seed: int = 42,
) -> tuple[float, float]:
    """Percentile bootstrap interval for a detection rate, in percent.

    Contracts are resampled with replacement and the rate recomputed on
    each resample; the interval is read off the empirical percentiles.
    """
    if not outcomes:
        return (0.0, 0.0)

    rng = random.Random(seed)
    n = len(outcomes)
    rates = []
    for _ in range(resamples):
        sample = [outcomes[rng.randrange(n)] for _ in range(n)]
        rates.append(100.0 * sum(sample) / n)
    rates.sort()

    alpha = 1.0 - confidence
    lo = rates[int(alpha / 2 * resamples)]
    hi = rates[min(int((1 - alpha / 2) * resamples), resamples - 1)]
    return (lo, hi)


def bootstrap_ci_tier_mean(
    per_tier: dict[str, list[bool]],
    resamples: int = BOOTSTRAP_RESAMPLES,
    confidence: float = CONFIDENCE,
    seed: int = 42,
) -> tuple[float, float]:
    """Percentile bootstrap interval for the unweighted mean of tier rates.

    The DS "Avg" column averages the four tier rates rather than pooling
    contracts, so the interval must resample within each tier and recompute
    that same statistic.
    """
    tiers = [v for v in per_tier.values() if v]
    if not tiers:
        return (0.0, 0.0)

    rng = random.Random(seed)
    means = []
    for _ in range(resamples):
        rates = []
        for outcomes in tiers:
            n = len(outcomes)
            drawn = [outcomes[rng.randrange(n)] for _ in range(n)]
            rates.append(100.0 * sum(drawn) / n)
        means.append(sum(rates) / len(rates))
    means.sort()

    alpha = 1.0 - confidence
    lo = means[int(alpha / 2 * resamples)]
    hi = means[min(int((1 - alpha / 2) * resamples), resamples - 1)]
    return (lo, hi)


def _chi2_sf_1df(x: float) -> float:
    """Upper tail of the chi-square distribution with one degree of freedom."""
    if x <= 0:
        return 1.0
    return math.erfc(math.sqrt(x / 2.0))


def mcnemar(a_outcomes: list[bool], b_outcomes: list[bool]) -> tuple[float, int, int]:
    """McNemar's test with continuity correction on paired outcomes.

    Returns (p_value, b, c) where b and c are the discordant counts.
    """
    if len(a_outcomes) != len(b_outcomes):
        raise ValueError("paired outcomes must have equal length")

    b = sum(1 for x, y in zip(a_outcomes, b_outcomes) if x and not y)
    c = sum(1 for x, y in zip(a_outcomes, b_outcomes) if y and not x)
    if b + c == 0:
        return (1.0, b, c)

    statistic = (abs(b - c) - 1) ** 2 / (b + c)
    return (_chi2_sf_1df(statistic), b, c)


def holm(pvalues: dict[str, float]) -> dict[str, float]:
    """Holm-Bonferroni step-down correction over a family of comparisons.

    Controls the family-wise error rate. Returned values are adjusted
    p-values, so they are compared against the original alpha.
    """
    if not pvalues:
        return {}

    ordered = sorted(pvalues.items(), key=lambda kv: kv[1])
    m = len(ordered)
    adjusted: dict[str, float] = {}
    running = 0.0
    for index, (key, p) in enumerate(ordered):
        running = max(running, (m - index) * p)
        adjusted[key] = min(running, 1.0)
    return adjusted

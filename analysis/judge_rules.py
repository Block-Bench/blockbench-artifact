"""Canonical judge aggregation rules for the BlockBench paper tables.

Verified against the published manuscript: this module reproduces Table 3
exactly, all 35 DS cells and all 49 TC cells.

The rules are not obvious from the raw files, so they are pinned here:

1. Judges are glm-4.7, mimo-v2-flash and mistral-large. Two further judges
   (codestral, gemini-3-flash) exist in the raw data but back no published
   number; they came from a superseded pipeline that averaged per-judge
   rates instead of voting.
2. DS and TC treat a target as found when ``complete_found`` OR
   ``partial_found`` is true, then take a 2-of-3 majority vote.
3. GS uses ``complete_found`` alone. See docs/OPEN_QUESTIONS.md.
4. Files whose basename starts with "_" are per-tier aggregates, not
   samples, and must be skipped or every denominator is inflated.
5. ``complete_found`` is read with a default of False. A legacy ``found`` key
   present in some outputs is not consulted.
"""

from __future__ import annotations

import json
from pathlib import Path

JUDGES_MAJORITY = ("glm-4.7", "mimo-v2-flash", "mistral-large")
UNUSED_JUDGES = ("codestral", "gemini-3-flash")


def is_sample_file(path: Path) -> bool:
    """Per-tier and per-variant aggregates start with "_" and are not samples."""
    return path.suffix == ".json" and not path.name.startswith("_")


def target_found(path: Path, rule: str = "complete_or_partial") -> bool | None:
    """Did the judge consider the documented target vulnerability found?

    Returns None when the file cannot be read or carries no assessment, so
    callers can distinguish a failed judgment from a genuine miss.
    """
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None

    ta = data.get("target_assessment")
    if not isinstance(ta, dict) or not ta:
        return None

    complete = ta.get("complete_found", False)
    if rule == "complete_only":
        return bool(complete)
    return bool(complete) or bool(ta.get("partial_found", False))


def majority(votes: list[bool | None]) -> bool | None:
    """Strict majority of the votes that were actually cast."""
    cast = [v for v in votes if v is not None]
    if not cast:
        return None
    return sum(cast) * 2 > len(cast)


def rate(
    judge_root: Path,
    relative: str,
    judges: tuple[str, ...] = JUDGES_MAJORITY,
    rule: str = "complete_or_partial",
) -> tuple[float | None, int, int]:
    """Detection rate over one subset directory.

    ``relative`` is the path below each judge directory, for example
    "claude-opus-4-5/ds/tier1". Returns (percentage, hits, n). The sample
    set is the union of sample files across judges, so a judge missing a
    file simply casts no vote rather than removing the sample.
    """
    names: set[str] = set()
    for judge in judges:
        directory = judge_root / judge / relative
        if directory.is_dir():
            names |= {p.name for p in directory.iterdir() if is_sample_file(p)}

    hits = n = 0
    for name in sorted(names):
        verdict = majority(
            [target_found(judge_root / j / relative / name, rule) for j in judges]
        )
        if verdict is None:
            continue
        n += 1
        hits += verdict

    return (100.0 * hits / n if n else None), hits, n

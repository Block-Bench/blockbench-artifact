# Open questions

Recorded rather than hidden. Each is something a reader could otherwise
discover and be puzzled by.

## 1. The GS aggregation rule differs from DS and TC

DS and TC take a 2-of-3 majority over `glm-4.7`, `mimo-v2-flash` and
`mistral-large`, counting a target as found when `complete_found OR
partial_found`. That reproduces Table 3 exactly.

The published GS column instead matches `glm-4.7` alone under `complete_found`
only. Under the DS/TC rule, GS comes out higher, for example 34.9 against a
published 33.0 for Claude. The May repository's aggregator
(`scripts/--Z.py:539`) uses `complete OR partial`, so either the published GS
numbers predate that script or a stricter rule was applied deliberately.

The paper does state that GS uses a different judge set from DS and TC, so a
different rule is not inconsistent, only undocumented. `config/analysis.yaml`
pins the rule that reproduces the paper.

## 2. Half the DS and TC judge outputs use a legacy key

Of 15,776 DS and TC judge files, 8,054 carry a legacy `found` key rather than
`complete_found`, and 964 carry neither. The published pipeline read
`complete_found` with a default of False and never consulted `found`, so every
one of those samples was counted as a miss.

This makes the published DS and TC rates **systematically conservative**. We
reproduce the published behaviour by default. Passing `legacy_found=True` to
`judge_rules.target_found` shows what the corrected reading gives, which is
materially higher.

Deciding whether to re-report on the corrected reading is a call for the
authors, not for this artifact.

## 3. Confidence intervals do not reproduce exactly

The paper reports [82--91] for Claude's DS average. Bootstrapping the same
statistic here, the unweighted mean of the four tier rates with 1000
percentile resamples, gives [80--92]. Our intervals are consistently a little
wider across all seven models.

The point estimates reproduce exactly, so this concerns the interval method
alone. The original interval computation has not been located.

## 4. Reasoning-effort variants are unreported

`runs/2026-01` contains `gemini-3-pro-low`, `-medium`, `-extended` and
`-hyper-extended`. These appear in no published table. They are retained as
part of the record and are excluded from all generated artifacts.

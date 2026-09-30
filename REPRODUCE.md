# Reproducing the paper

```bash
python analysis/build_tables.py
```

No dependencies beyond the Python standard library. Outputs are written to
`paper_artifacts/`.

## Which file backs which table

| Paper object | Generated file | Status |
|---|---|---|
| Table 3, DS columns | `table3_ds_tc.md` | reproduces exactly, 35/35 cells |
| Table 3, TC columns | `table3_ds_tc.md` | reproduces exactly, 49/49 cells |
| Table 3, 95% CI | `table3_ds_tc.md` | point estimates exact, intervals wider (see docs/OPEN_QUESTIONS.md) |
| Table 4, GS slices | `table4_and_10_gs.md` | reproduces for 5 of 7 models |
| Table 10, longitudinal | `table4_and_10_gs.md` | reproduces |
| Appendix FP rates | `fp_rates.md` | reproduces, with true denominators |
| GS per prompt | `gs_per_prompt.md` | not previously published |
| DS significance tests | `stats_ds.md` | raw p-values plus Holm correction |

## The configuration that matters

Four things must be right or the numbers will not reproduce. All are pinned in
`config/analysis.yaml` and implemented in `analysis/judge_rules.py`.

1. **Judges.** `glm-4.7`, `mimo-v2-flash`, `mistral-large`. Two further judges
   in the raw data back nothing published.
2. **Vote.** 2-of-3 majority for DS and TC. GS uses a single judge.
3. **Target found.** `complete_found OR partial_found` for DS and TC;
   `complete_found` alone for GS. The legacy `found` key is deliberately not
   consulted, matching the published pipeline.
4. **Aggregate files.** Any file whose basename starts with `_` is a per-tier
   or per-variant summary, not a sample. Counting them inflates every
   denominator by one and silently lowers every rate.

## Things worth knowing about the numbers

**The DS `Avg` column is an unweighted mean of the four tier rates**, not the
sample-weighted overall rate. For Claude that is 86.5 rather than 84.0.

**The DS evaluation set is 100 contracts at 20 / 37 / 30 / 13**, drawn from the
full 210. This is not proportional stratification; tiers 3 and 4 are taken in
full.

**False positive denominators are not all 100.** Three models were not
evaluated on the complete clean set. `fp_rates.md` prints the real denominator
per model and marks the short ones.

**GS-Orig is defined as the sample set carried by the January run**, which is
what makes the two runs directly comparable on identical contracts rather than
on a date filter applied after the fact.

## Statistics

Bootstrap intervals use 1000 percentile resamples at 95% with seed 42,
resampling within each tier and recomputing the tier mean. Pairwise model
comparisons use McNemar with continuity correction. Holm-Bonferroni is applied
across all 21 comparisons; the original pipeline applied no correction, so
`stats_ds.md` reports raw and adjusted values side by side and counts how many
comparisons change status.

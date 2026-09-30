# BlockBench Artifact

Evaluation records and analysis code for the BlockBench papers.

The benchmark itself (contracts, transformation strategies, dataset browser)
lives in [Block-Bench/base](https://github.com/Block-Bench/base). This
repository holds what was run and the code that computes the result tables
from it.

## Structure

```
runs/                 raw evaluation records, one directory per run
  2026-01/
  2026-05/
    detection/        <model>/<subset>/<variant>/d_<sample>.json
    judge/            <judge>/<model>/<subset>/<variant>/j_<sample>.json
    traditional/      <tool>/<subset>/{raw,processed}/
    MANIFEST.json     models, subsets, judges, file counts, coverage

analysis/             analysis code
  judge_rules.py      judge selection, vote rule, target-found rule
  stats.py            bootstrap intervals, McNemar, Holm correction
  build_tables.py     entry point, writes results/

results/              generated tables, one file per table

config/
  analysis.yaml       the analysis configuration, in one place

tools/
  build_manifests.py  regenerates runs/*/MANIFEST.json
```

Runs are named by evaluation date. The same Gold Standard contracts appear in
both runs, so slicing by run directory gives the two evaluation dates directly.

## Running it

```bash
python analysis/build_tables.py     # writes results/
python tools/build_manifests.py     # rewrites runs/*/MANIFEST.json
```

Python 3.9 or newer. Standard library only, no dependencies to install.
Output is deterministic; re-running produces identical files.

## Record layout

A detection record carries the prompt sent, the parsed prediction, the full
raw model response, ground-truth fields for the sample, and API metrics.

A judge record carries the judge's per-finding classifications and a
`target_assessment` block holding `complete_found`, `partial_found`,
`root_cause_match`, `location_match`, `type_match` and the three reasoning
quality scores.

Within any subset directory, files whose basename begins with `_` are
per-directory aggregates rather than samples.

## Configuration

`config/analysis.yaml` holds the judge set, vote rule, target-found rule,
sample counts and statistical parameters used by `analysis/`. Change it there
rather than in the analysis modules.

Five judge models appear under `runs/*/judge/`. The set used by the analysis
code is listed in `config/analysis.yaml`; the remainder are retained as part
of the record.

## Licensing

Code is MIT (`LICENSE-CODE`). Annotations and metadata we authored are
CC BY 4.0 (`LICENSE-DATA`). Solidity source contracts and raw model responses
keep their upstream terms; see `NOTICE.md`.

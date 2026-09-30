# BlockBench Artifact

Reproducibility artifact for the BlockBench papers. Tagged per publication.

BlockBench is a contamination-controlled evaluation of LLM smart contract
vulnerability detection. This repository holds the raw evaluation records and
the analysis code that turns them into the numbers reported in the paper.

The living benchmark itself (contracts, transformation strategies, dataset
browser) lives in [Block-Bench/base](https://github.com/Block-Bench/base).
This repository is the frozen record of what was run.

## Layout

```
runs/2026-01/     first evaluation round
runs/2026-05/     second round, four months later
  detection/      per-model model outputs, including raw responses
  judge/          per-judge assessments of those outputs
  traditional/    Slither and Mythril
  MANIFEST.json   what the run contains, including its gaps
analysis/         judge rules, statistics, table builder
paper_artifacts/  generated tables, one file per paper object
config/           the pinned analysis configuration
docs/             provenance, licensing, open questions
tools/            manifest generation
```

## Two runs, not one

The same Gold Standard contracts were evaluated twice, in January and May
2026, with the same models, prompts and judges. Detection on those fixed
contracts rose from roughly 6% to roughly 85% over that interval. Both runs
are therefore required to reproduce the paper, and `runs/` is scoped by
evaluation date rather than by iteration so the comparison is visible in the
directory structure.

## Reproducing the paper

```bash
python analysis/build_tables.py
```

Outputs land in `paper_artifacts/`. See [REPRODUCE.md](REPRODUCE.md) for which
file backs which table, and which numbers reproduce exactly.

## Judges

Five judge models appear in the raw data. Only three back published numbers:
`glm-4.7`, `mimo-v2-flash` and `mistral-large`. The other two, `codestral`
and `gemini-3-flash`, come from a superseded pipeline that averaged per-judge
rates instead of voting; they are retained for completeness and are marked
unused in `config/analysis.yaml` and in each `MANIFEST.json`.

## Licensing

Code is MIT. Our own annotations and metadata are CC BY 4.0. The Solidity
source contracts keep their upstream licences, which are not uniform. See
[NOTICE.md](NOTICE.md) before redistributing.

# Provenance and third-party terms

This repository redistributes Solidity source code that we did not author.
Those files keep their original licences, which are **not uniform**. Read this
before reusing or redistributing any part of the dataset.

## Our contribution

The annotations, difficulty tiers, CodeActs labels, transformation variants,
evaluation records and analysis code are ours, licensed under `LICENSE-CODE`
(code) and `LICENSE-DATA` (annotations and metadata).

Every dataset sample carries `source_reference` and `external_references`
fields pointing at the original report or repository, so provenance can be
checked per sample rather than taken on trust.

## Upstream sources

### Difficulty Stratified (DS)

| Source | Terms |
|---|---|
| SmartBugs Curated | permissive, attribution required |
| Trail of Bits, Not So Smart Contracts | permissive, attribution required |
| DeFiVulnLabs | permissive, attribution required |

### Temporal Contamination (TC)

Reconstructions of publicly documented DeFi exploits, 2016 to 2024. Derived
from public post-mortems and educational repositories such as DeFiHackLabs.
Transformation variants are **derivative works** and inherit whatever the
source contract carries.

### Gold Standard (GS)

Professional audit findings published by Code4rena, Spearbit and MixBytes.
All were retrieved from the auditors' public report pages. Publication on a
public page establishes provenance, not a redistribution grant, and the
contest repositories these findings refer to carry their own licences.
Consult the `source_reference` on a sample before redistributing it.

### Negative set (NEG)

Production protocol code. **These terms differ materially and must not be
treated as one pool.**

| Protocol | Contracts | Terms |
|---|---|---|
| OpenZeppelin v5 | 25 | MIT |
| Aave v3 | 19 | mixed, portions BUSL-1.1 |
| MakerDAO | 15 | AGPL-3.0 family |
| Uniswap v4 | 14 | BUSL-1.1 |
| Compound v3 | 14 | BSD-3-Clause family |
| Lido | 13 | GPL-3.0 family |

The table above is our reading of each project's published terms and is a
starting point, not a legal determination. Individual files may carry their own
SPDX headers that differ from their project default, so check the header on the
file you intend to reuse.

BUSL-1.1 carries use restrictions and a delayed open-source conversion date.
It is not equivalent to MIT. Anyone reusing the negative set for anything
beyond evaluation research should check each protocol's terms directly.

## Raw model responses

Detection records under `runs/*/detection/` retain a `raw_response` field with
the complete model output. These originate with Anthropic, OpenAI, Google,
DeepSeek, Meta, xAI and Alibaba respectively, and are retained so that judge
assessments can be independently rechecked. They are not covered by
`LICENSE-DATA`, and provider terms apply to their reuse.

## Corrections

If you hold rights to any material here and want it removed or its terms
restated, open an issue and we will act on it.

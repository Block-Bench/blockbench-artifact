# GS Context Protocol Summary

**Judge:** codestral
**Generated:** 2026-01-06T00:30:48.166295+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Gemini 3 Pro | 35.3% | 90.9% | 50.8% | 70.6% | 0.92 | 0.92 | 0.89 |
| 2 | Claude Opus 4.5 | 29.4% | 88.9% | 44.2% | 88.2% | 0.89 | 0.86 | 0.83 |
| 3 | GPT-5.2 | 23.5% | 70.8% | 35.3% | 61.8% | 0.86 | 0.86 | 0.81 |
| 4 | Qwen3 Coder Plus | 20.6% | 57.9% | 30.4% | 70.6% | 0.89 | 0.79 | 0.76 |
| 5 | Grok 4 Fast | 17.6% | 61.1% | 27.4% | 38.2% | 0.93 | 0.92 | 0.85 |
| 6 | DeepSeek V3.2 | 14.7% | 52.8% | 23.0% | 91.2% | 0.90 | 0.84 | 0.80 |
| 7 | Llama 4 Maverick | 14.7% | 39.3% | 21.4% | 91.2% | 0.84 | 0.84 | 0.70 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
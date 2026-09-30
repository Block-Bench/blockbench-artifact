# GS Context Protocol Summary

**Judge:** mimo-v2-flash
**Generated:** 2026-01-06T00:30:48.388079+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 26.5% | 41.1% | 32.2% | 88.2% | 0.94 | 0.97 | 0.88 |
| 2 | Gemini 3 Pro | 26.5% | 55.0% | 35.7% | 67.6% | 1.00 | 1.00 | 0.88 |
| 3 | DeepSeek V3.2 | 23.5% | 23.5% | 23.5% | 91.2% | 0.69 | 0.69 | 0.69 |
| 4 | GPT-5.2 | 11.8% | 83.3% | 20.6% | 61.8% | 1.00 | 1.00 | 0.97 |
| 5 | Grok 4 Fast | 11.8% | 38.9% | 18.1% | 38.2% | 0.94 | 0.94 | 0.91 |
| 6 | Llama 4 Maverick | 5.9% | 4.0% | 4.8% | 91.2% | 0.45 | 0.55 | 0.35 |
| 7 | Qwen3 Coder Plus | 5.9% | 5.6% | 5.7% | 70.6% | 0.65 | 0.70 | 0.55 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
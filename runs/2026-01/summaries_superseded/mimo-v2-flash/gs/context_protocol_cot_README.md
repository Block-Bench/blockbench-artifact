# GS Context + CoT Summary

**Judge:** mimo-v2-flash
**Generated:** 2026-01-06T00:30:48.433816+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 23.5% | 33.8% | 27.8% | 82.4% | 0.98 | 0.97 | 0.95 |
| 2 | Gemini 3 Pro | 23.5% | 63.0% | 34.3% | 76.5% | 0.99 | 0.99 | 0.95 |
| 3 | GPT-5.2 | 23.5% | 74.1% | 35.7% | 64.7% | 0.89 | 0.83 | 0.85 |
| 4 | Qwen3 Coder Plus | 20.6% | 15.4% | 17.6% | 85.3% | 0.66 | 0.63 | 0.63 |
| 5 | Llama 4 Maverick | 17.6% | 12.7% | 14.8% | 91.2% | 0.70 | 0.68 | 0.57 |
| 6 | DeepSeek V3.2 | 11.8% | 14.0% | 12.8% | 94.1% | 0.62 | 0.65 | 0.70 |
| 7 | Grok 4 Fast | 8.8% | 42.1% | 14.6% | 41.2% | 0.93 | 0.92 | 0.97 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
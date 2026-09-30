# GS Context + CoT (Naturalistic) Summary

**Judge:** mimo-v2-flash
**Generated:** 2026-01-06T00:30:48.547933+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | GPT-5.2 | 29.4% | 58.3% | 39.1% | 97.1% | 0.98 | 0.97 | 0.95 |
| 2 | Gemini 3 Pro | 26.5% | 52.2% | 35.1% | 91.2% | 0.98 | 0.98 | 0.95 |
| 3 | Claude Opus 4.5 | 23.5% | 37.5% | 28.9% | 79.4% | 0.96 | 0.93 | 0.91 |
| 4 | DeepSeek V3.2 | 20.6% | 12.2% | 15.3% | 94.1% | 0.83 | 0.78 | 0.80 |
| 5 | Qwen3 Coder Plus | 20.6% | 7.9% | 11.4% | 100.0% | 0.89 | 0.82 | 0.82 |
| 6 | Grok 4 Fast | 11.8% | 29.3% | 16.8% | 55.9% | 0.85 | 0.70 | 0.80 |
| 7 | Llama 4 Maverick | 5.9% | 12.0% | 7.9% | 38.2% | 0.80 | 0.75 | 0.70 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
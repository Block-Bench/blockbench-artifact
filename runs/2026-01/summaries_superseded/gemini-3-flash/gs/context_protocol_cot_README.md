# GS Context + CoT Summary

**Judge:** gemini-3-flash
**Generated:** 2026-01-06T00:30:48.680302+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Gemini 3 Pro | 29.4% | 95.5% | 45.0% | 76.5% | 0.97 | 0.94 | 0.98 |
| 2 | Claude Opus 4.5 | 26.5% | 56.9% | 36.1% | 82.4% | 0.99 | 0.99 | 0.98 |
| 3 | GPT-5.2 | 23.5% | 96.2% | 37.8% | 64.7% | 0.95 | 0.90 | 0.97 |
| 4 | Grok 4 Fast | 8.8% | 68.4% | 15.6% | 41.2% | 1.00 | 0.93 | 0.97 |
| 5 | DeepSeek V3.2 | 5.9% | 22.0% | 9.3% | 94.1% | 1.00 | 0.90 | 1.00 |
| 6 | Llama 4 Maverick | 5.9% | 5.8% | 5.8% | 91.2% | 0.75 | 0.80 | 0.65 |
| 7 | Qwen3 Coder Plus | 5.9% | 8.2% | 6.8% | 85.3% | 0.90 | 0.75 | 0.80 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
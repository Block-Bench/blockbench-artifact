# GS Context + CoT Summary

**Judge:** codestral
**Generated:** 2026-01-06T00:30:48.209308+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 32.4% | 74.3% | 45.1% | 82.4% | 0.91 | 0.89 | 0.82 |
| 2 | DeepSeek V3.2 | 29.4% | 61.0% | 39.7% | 94.1% | 0.91 | 0.88 | 0.82 |
| 3 | Gemini 3 Pro | 26.5% | 89.4% | 40.8% | 76.5% | 0.91 | 0.90 | 0.91 |
| 4 | GPT-5.2 | 26.5% | 77.8% | 39.5% | 64.7% | 0.84 | 0.83 | 0.77 |
| 5 | Qwen3 Coder Plus | 26.5% | 54.9% | 35.7% | 85.3% | 0.87 | 0.82 | 0.76 |
| 6 | Llama 4 Maverick | 23.5% | 25.4% | 24.4% | 91.2% | 0.88 | 0.85 | 0.79 |
| 7 | Grok 4 Fast | 14.7% | 63.2% | 23.9% | 41.2% | 0.90 | 0.90 | 0.86 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
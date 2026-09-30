# GS Context + CoT (Naturalistic) Summary

**Judge:** gemini-3-flash
**Generated:** 2026-01-06T00:30:48.765093+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | GPT-5.2 | 47.1% | 85.7% | 60.8% | 97.1% | 0.93 | 0.87 | 0.96 |
| 2 | Gemini 3 Pro | 35.3% | 88.9% | 50.5% | 91.2% | 0.99 | 0.97 | 0.97 |
| 3 | Claude Opus 4.5 | 26.5% | 76.2% | 39.3% | 76.5% | 0.98 | 0.92 | 0.97 |
| 4 | DeepSeek V3.2 | 26.5% | 30.7% | 28.4% | 94.1% | 0.91 | 0.81 | 0.84 |
| 5 | Qwen3 Coder Plus | 26.5% | 12.0% | 16.5% | 100.0% | 0.88 | 0.73 | 0.86 |
| 6 | Grok 4 Fast | 14.7% | 67.2% | 24.1% | 55.9% | 0.90 | 0.80 | 0.88 |
| 7 | Llama 4 Maverick | 2.9% | 12.5% | 4.8% | 35.3% | 0.60 | 0.50 | 0.40 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
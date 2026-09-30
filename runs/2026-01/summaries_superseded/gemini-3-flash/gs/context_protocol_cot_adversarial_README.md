# GS Context + CoT (Adversarial) Summary

**Judge:** gemini-3-flash
**Generated:** 2026-01-06T00:30:48.721120+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 41.2% | 56.7% | 47.7% | 100.0% | 0.94 | 0.89 | 0.97 |
| 2 | Gemini 3 Pro | 35.3% | 91.8% | 51.0% | 97.1% | 0.96 | 0.94 | 0.99 |
| 3 | GPT-5.2 | 35.3% | 89.2% | 50.6% | 94.1% | 0.94 | 0.93 | 0.97 |
| 4 | DeepSeek V3.2 | 14.7% | 34.6% | 20.6% | 100.0% | 0.94 | 0.84 | 1.00 |
| 5 | Grok 4 Fast | 11.8% | 82.9% | 20.6% | 64.7% | 1.00 | 0.95 | 1.00 |
| 6 | Qwen3 Coder Plus | 11.8% | 6.8% | 8.6% | 100.0% | 0.78 | 0.68 | 0.75 |
| 7 | Llama 4 Maverick | 0.0% | 7.9% | 0.0% | 85.3% | - | - | - |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
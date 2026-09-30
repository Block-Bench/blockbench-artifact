# GS Context + CoT (Adversarial) Summary

**Judge:** mimo-v2-flash
**Generated:** 2026-01-06T00:30:48.489891+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 35.3% | 25.9% | 29.9% | 100.0% | 0.90 | 0.89 | 0.84 |
| 2 | Gemini 3 Pro | 35.3% | 68.2% | 46.5% | 97.1% | 1.00 | 1.00 | 0.98 |
| 3 | GPT-5.2 | 32.4% | 78.4% | 45.8% | 91.2% | 0.96 | 0.95 | 0.91 |
| 4 | DeepSeek V3.2 | 14.7% | 22.5% | 17.8% | 100.0% | 0.90 | 0.84 | 0.94 |
| 5 | Grok 4 Fast | 11.8% | 44.2% | 18.6% | 61.8% | 0.96 | 0.95 | 0.93 |
| 6 | Qwen3 Coder Plus | 11.8% | 6.0% | 8.0% | 97.1% | 0.90 | 0.81 | 0.72 |
| 7 | Llama 4 Maverick | 2.9% | 2.9% | 2.9% | 82.4% | 0.80 | 0.60 | 0.70 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
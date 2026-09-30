# GS Context + CoT (Adversarial) Summary

**Judge:** codestral
**Generated:** 2026-01-06T00:30:48.253279+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Gemini 3 Pro | 41.2% | 85.3% | 55.5% | 97.1% | 0.94 | 0.94 | 0.92 |
| 2 | Claude Opus 4.5 | 38.2% | 87.0% | 53.1% | 100.0% | 0.92 | 0.90 | 0.88 |
| 3 | DeepSeek V3.2 | 35.3% | 71.7% | 47.3% | 100.0% | 0.91 | 0.88 | 0.85 |
| 4 | GPT-5.2 | 26.5% | 91.4% | 41.1% | 94.1% | 0.88 | 0.83 | 0.83 |
| 5 | Qwen3 Coder Plus | 20.6% | 32.6% | 25.2% | 100.0% | 0.87 | 0.81 | 0.76 |
| 6 | Grok 4 Fast | 14.7% | 66.7% | 24.1% | 64.7% | 0.90 | 0.88 | 0.88 |
| 7 | Llama 4 Maverick | 5.9% | 12.8% | 8.1% | 85.3% | 0.85 | 0.75 | 0.75 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
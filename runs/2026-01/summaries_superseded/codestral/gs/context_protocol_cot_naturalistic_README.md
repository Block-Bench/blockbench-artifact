# GS Context + CoT (Naturalistic) Summary

**Judge:** codestral
**Generated:** 2026-01-06T00:30:48.294492+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | GPT-5.2 | 38.2% | 92.5% | 54.1% | 97.1% | 0.88 | 0.85 | 0.85 |
| 2 | Gemini 3 Pro | 35.3% | 91.5% | 50.9% | 91.2% | 0.91 | 0.90 | 0.86 |
| 3 | Qwen3 Coder Plus | 29.4% | 55.3% | 38.4% | 100.0% | 0.87 | 0.83 | 0.82 |
| 4 | DeepSeek V3.2 | 26.5% | 58.9% | 36.5% | 94.1% | 0.88 | 0.84 | 0.87 |
| 5 | Claude Opus 4.5 | 20.6% | 86.5% | 33.3% | 79.4% | 0.91 | 0.90 | 0.87 |
| 6 | Grok 4 Fast | 14.7% | 93.3% | 25.4% | 64.7% | 0.92 | 0.88 | 0.88 |
| 7 | Llama 4 Maverick | 2.9% | 37.5% | 5.5% | 38.2% | 0.90 | 0.80 | 0.70 |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
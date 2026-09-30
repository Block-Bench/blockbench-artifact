# GS Context Protocol Summary

**Judge:** gemini-3-flash
**Generated:** 2026-01-06T00:30:48.634818+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Claude Opus 4.5 | 29.4% | 61.9% | 39.9% | 88.2% | 0.98 | 0.96 | 0.93 |
| 2 | Gemini 3 Pro | 23.5% | 95.2% | 37.7% | 70.6% | 0.96 | 0.90 | 0.96 |
| 3 | GPT-5.2 | 11.8% | 87.0% | 20.7% | 61.8% | 0.97 | 1.00 | 1.00 |
| 4 | Grok 4 Fast | 8.8% | 83.3% | 16.0% | 38.2% | 1.00 | 0.93 | 1.00 |
| 5 | DeepSeek V3.2 | 5.9% | 8.7% | 7.0% | 91.2% | 0.90 | 0.80 | 1.00 |
| 6 | Qwen3 Coder Plus | 2.9% | 5.7% | 3.9% | 70.6% | 0.90 | 0.80 | 0.70 |
| 7 | Llama 4 Maverick | 0.0% | 3.8% | 0.0% | 91.2% | - | - | - |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
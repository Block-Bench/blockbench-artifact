# GS Direct Summary

**Judge:** gemini-3-flash
**Generated:** 2026-01-06T00:30:48.591274+00:00
**Models Evaluated:** 7

## Model Rankings (by TDR)

| Rank | Model | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV |
|------|-------|-----|-----------|----|-----------|----|-----|-----|
| 1 | Gemini 3 Pro HE | 26.5% | 89.7% | 40.9% | 82.4% | 0.98 | 0.96 | 0.94 |
| 2 | Claude Opus 4.5 | 11.8% | 54.8% | 19.4% | 67.6% | 0.97 | 1.00 | 0.93 |
| 3 | GPT-5.2 | 8.8% | 100.0% | 16.2% | 44.1% | 1.00 | 1.00 | 1.00 |
| 4 | DeepSeek V3.2 | 2.9% | 15.2% | 4.9% | 76.5% | 0.90 | 0.90 | 0.70 |
| 5 | Grok 4 Fast | 2.9% | 62.5% | 5.6% | 20.6% | 1.00 | 1.00 | 1.00 |
| 6 | Llama 4 Maverick | 2.9% | 7.5% | 4.2% | 76.5% | 0.50 | 0.40 | 0.30 |
| 7 | Qwen3 Coder Plus | 0.0% | 5.6% | 0.0% | 50.0% | - | - | - |

## Metrics Legend

- **TDR**: Target Detection Rate - % of target vulnerabilities correctly identified
- **Precision**: True positives / (True positives + False positives)
- **F1**: Harmonic mean of Precision and TDR
- **Verdict Acc**: % of correct vulnerable/safe verdicts
- **RCIR**: Root Cause Identification Rating (0-1)
- **AVA**: Attack Vector Accuracy (0-1)
- **FSV**: Fix Suggestion Validity (0-1)
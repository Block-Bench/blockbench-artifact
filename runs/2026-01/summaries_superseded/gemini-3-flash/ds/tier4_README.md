# DS Tier4 - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 92.3% | 85.7% | 88.9% | 100.0% | 1.00 | 1.00 | 0.99 | 2.2 | 14.3% |
| 2 | gemini-3-pro | 92.3% | 100.0% | 96.0% | 92.3% | 0.97 | 1.00 | 0.98 | 1.3 | 0.0% |
| 3 | gpt-5.2 | 92.3% | 100.0% | 96.0% | 100.0% | 0.98 | 0.99 | 1.00 | 1.4 | 0.0% |
| 4 | llama-4-maverick | 84.6% | 57.1% | 68.2% | 100.0% | 0.93 | 0.89 | 0.89 | 1.6 | 42.9% |
| 5 | deepseek-v3-2 | 69.2% | 61.9% | 65.4% | 84.6% | 0.98 | 0.98 | 0.98 | 1.6 | 38.1% |
| 6 | qwen3-coder-plus | 69.2% | 57.9% | 63.1% | 92.3% | 0.98 | 0.93 | 0.91 | 1.5 | 42.1% |
| 7 | grok-4-fast | 30.8% | 100.0% | 47.1% | 38.5% | 0.95 | 1.00 | 0.97 | 0.5 | 0.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 12/13 | 7.7% | 0.0% | 53.8% | 24 | 4 | 0.31 |
| gemini-3-pro | 12/13 | 7.7% | 0.0% | 23.1% | 17 | 0 | 0.00 |
| gpt-5.2 | 12/13 | 7.7% | 0.0% | 38.5% | 18 | 0 | 0.00 |
| llama-4-maverick | 11/13 | 15.4% | 15.4% | 7.7% | 12 | 9 | 0.69 |
| deepseek-v3-2 | 9/13 | 30.8% | 7.7% | 15.4% | 13 | 8 | 0.62 |
| qwen3-coder-plus | 9/13 | 30.8% | 7.7% | 15.4% | 11 | 8 | 0.62 |
| grok-4-fast | 4/13 | 69.2% | 0.0% | 23.1% | 7 | 0 | 0.00 |

---

## Performance by Vulnerability Type

### Reentrancy (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Signature Replay (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 83.3% | 90.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 60.0% | 75.0% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.85 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.80 |
| qwen3-coder-plus | 1/2 | 50.0% | 33.3% | 40.0% | 1.00 |

### Storage Collision (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |

### Integer Issues (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |

### Weak Randomness (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 71.4% | 83.3% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 16.7% | 25.0% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 40.0% | 44.4% | 1.00 |

### Oracle Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Inflation Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.50 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Flash Loan Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

---

## Metric Definitions

| Metric | Description |
|:-------|:------------|
| **TDR** | Target Detection Rate - % of samples where target vulnerability was found |
| **Precision** | True Positives / (True Positives + False Positives) |
| **F1** | Harmonic mean of Precision and TDR |
| **Verdict Acc** | % of samples with correct vulnerable/safe verdict |
| **RCIR** | Root Cause Identification Rating (0-1) |
| **AVA** | Attack Vector Accuracy (0-1) |
| **FSV** | Fix Suggestion Validity (0-1) |
| **Lucky Guess** | Correct verdict but no target found and no bonus findings |
| **Bonus Disc** | Ancillary Discovery Rate - found additional valid vulnerabilities |
| **TP/FP** | True Positives / False Positives |
| **FAD** | False Alarm Density - avg false positives per sample |

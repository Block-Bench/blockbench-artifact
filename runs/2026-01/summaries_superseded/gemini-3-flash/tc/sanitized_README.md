# TC Sanitized - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 73.9% | 91.1% | 81.6% | 97.8% | 0.96 | 0.93 | 0.99 | 2.4 | 8.9% |
| 2 | qwen3-coder-plus | 65.2% | 63.8% | 64.5% | 97.8% | 0.95 | 0.88 | 0.93 | 1.5 | 36.2% |
| 3 | deepseek-v3-2 | 63.0% | 66.3% | 64.6% | 97.8% | 0.98 | 0.96 | 0.98 | 2.2 | 33.7% |
| 4 | llama-4-maverick | 63.0% | 42.5% | 50.7% | 100.0% | 0.93 | 0.82 | 0.94 | 2.3 | 57.5% |
| 5 | gpt-5.2 | 54.3% | 97.0% | 69.7% | 87.0% | 0.98 | 0.96 | 0.98 | 1.4 | 3.0% |
| 6 | gemini-3-pro | 50.0% | 98.0% | 66.2% | 63.0% | 0.96 | 0.90 | 0.87 | 1.1 | 2.0% |
| 7 | grok-4-fast | 41.3% | 95.3% | 57.6% | 71.7% | 0.99 | 0.97 | 0.96 | 0.9 | 4.7% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 34/46 | 26.1% | 0.0% | 82.6% | 102 | 10 | 0.22 |
| qwen3-coder-plus | 30/46 | 34.8% | 19.6% | 21.7% | 44 | 25 | 0.54 |
| deepseek-v3-2 | 29/46 | 37.0% | 13.0% | 54.3% | 67 | 34 | 0.74 |
| llama-4-maverick | 29/46 | 37.0% | 21.7% | 21.7% | 45 | 61 | 1.33 |
| gpt-5.2 | 25/46 | 45.7% | 0.0% | 65.2% | 64 | 2 | 0.04 |
| gemini-3-pro | 23/46 | 50.0% | 0.0% | 37.0% | 48 | 1 | 0.02 |
| grok-4-fast | 19/46 | 58.7% | 4.3% | 39.1% | 41 | 2 | 0.04 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 9/12 | 75.0% | 65.4% | 69.9% | 0.98 |
| llama-4-maverick | 9/12 | 75.0% | 50.0% | 60.0% | 0.96 |
| claude-opus-4-5 | 8/12 | 66.7% | 91.3% | 77.1% | 1.00 |
| qwen3-coder-plus | 8/12 | 66.7% | 64.7% | 65.7% | 0.93 |
| gpt-5.2 | 7/12 | 58.3% | 100.0% | 73.7% | 1.00 |
| gemini-3-pro | 6/12 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 6/12 | 50.0% | 88.9% | 64.0% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 6/7 | 85.7% | 100.0% | 92.3% | 0.90 |
| llama-4-maverick | 6/7 | 85.7% | 50.0% | 63.2% | 0.87 |
| qwen3-coder-plus | 6/7 | 85.7% | 77.8% | 81.6% | 0.98 |
| deepseek-v3-2 | 2/7 | 28.6% | 46.2% | 35.3% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 100.0% | 44.4% | 1.00 |
| gpt-5.2 | 2/7 | 28.6% | 90.0% | 43.4% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 75.0% | 24.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 5/6 | 83.3% | 53.8% | 65.4% | 0.98 |
| claude-opus-4-5 | 4/6 | 66.7% | 88.9% | 76.2% | 0.97 |
| deepseek-v3-2 | 4/6 | 66.7% | 55.6% | 60.6% | 1.00 |
| qwen3-coder-plus | 4/6 | 66.7% | 80.0% | 72.7% | 1.00 |
| gemini-3-pro | 3/6 | 50.0% | 88.9% | 64.0% | 0.83 |
| gpt-5.2 | 3/6 | 50.0% | 100.0% | 66.7% | 0.97 |
| grok-4-fast | 2/6 | 33.3% | 100.0% | 50.0% | 1.00 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/5 | 80.0% | 100.0% | 88.9% | 0.90 |
| qwen3-coder-plus | 4/5 | 80.0% | 62.5% | 70.2% | 0.97 |
| claude-opus-4-5 | 3/5 | 60.0% | 84.6% | 70.2% | 1.00 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| llama-4-maverick | 3/5 | 60.0% | 27.3% | 37.5% | 0.87 |
| deepseek-v3-2 | 2/5 | 40.0% | 57.1% | 47.1% | 0.95 |
| grok-4-fast | 2/5 | 40.0% | 100.0% | 57.1% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 80.0% | 88.9% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 40.0% | 44.4% | 0.80 |
| qwen3-coder-plus | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 1.00 |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.70 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

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

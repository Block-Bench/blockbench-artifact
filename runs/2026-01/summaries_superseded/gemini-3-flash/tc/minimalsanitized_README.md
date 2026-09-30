# TC Minimalsanitized - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 73.9% | 87.3% | 80.0% | 97.8% | 0.99 | 0.95 | 0.99 | 2.4 | 12.7% |
| 2 | gemini-3-pro | 63.0% | 89.5% | 74.0% | 97.8% | 0.98 | 0.93 | 0.96 | 1.7 | 10.5% |
| 3 | gpt-5.2 | 63.0% | 100.0% | 77.3% | 91.3% | 0.99 | 0.98 | 0.98 | 1.5 | 0.0% |
| 4 | llama-4-maverick | 63.0% | 42.0% | 50.4% | 100.0% | 0.93 | 0.83 | 0.92 | 2.2 | 58.0% |
| 5 | deepseek-v3-2 | 60.9% | 59.6% | 60.2% | 100.0% | 0.99 | 0.96 | 0.97 | 2.2 | 40.4% |
| 6 | qwen3-coder-plus | 58.7% | 57.1% | 57.9% | 100.0% | 0.98 | 0.91 | 0.97 | 1.7 | 42.9% |
| 7 | grok-4-fast | 39.1% | 94.7% | 55.4% | 67.4% | 0.98 | 0.96 | 0.98 | 0.8 | 5.3% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 34/46 | 26.1% | 0.0% | 78.3% | 96 | 14 | 0.30 |
| gemini-3-pro | 29/46 | 37.0% | 2.2% | 58.7% | 68 | 8 | 0.17 |
| gpt-5.2 | 29/46 | 37.0% | 0.0% | 60.9% | 69 | 0 | 0.00 |
| llama-4-maverick | 29/46 | 37.0% | 21.7% | 19.6% | 42 | 58 | 1.26 |
| deepseek-v3-2 | 28/46 | 39.1% | 19.6% | 45.7% | 59 | 40 | 0.87 |
| qwen3-coder-plus | 27/46 | 41.3% | 21.7% | 28.3% | 44 | 33 | 0.72 |
| grok-4-fast | 18/46 | 60.9% | 2.2% | 32.6% | 36 | 2 | 0.04 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 9/12 | 75.0% | 91.7% | 82.5% | 0.98 |
| gemini-3-pro | 8/12 | 66.7% | 100.0% | 80.0% | 0.97 |
| gpt-5.2 | 8/12 | 66.7% | 100.0% | 80.0% | 0.99 |
| llama-4-maverick | 8/12 | 66.7% | 50.0% | 57.1% | 0.94 |
| deepseek-v3-2 | 7/12 | 58.3% | 59.1% | 58.7% | 0.99 |
| qwen3-coder-plus | 7/12 | 58.3% | 66.7% | 62.2% | 0.99 |
| grok-4-fast | 5/12 | 41.7% | 100.0% | 58.8% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 6/7 | 85.7% | 46.7% | 60.4% | 0.90 |
| claude-opus-4-5 | 4/7 | 57.1% | 80.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 4/7 | 57.1% | 42.9% | 49.0% | 0.97 |
| deepseek-v3-2 | 3/7 | 42.9% | 35.7% | 39.0% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 66.7% | 40.0% | 1.00 |
| gpt-5.2 | 2/7 | 28.6% | 100.0% | 44.4% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 80.0% | 24.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 88.2% | 75.9% | 1.00 |
| deepseek-v3-2 | 4/6 | 66.7% | 73.3% | 69.8% | 0.97 |
| gemini-3-pro | 4/6 | 66.7% | 92.9% | 77.6% | 0.90 |
| gpt-5.2 | 4/6 | 66.7% | 100.0% | 80.0% | 1.00 |
| llama-4-maverick | 4/6 | 66.7% | 38.5% | 48.8% | 0.95 |
| qwen3-coder-plus | 4/6 | 66.7% | 81.8% | 73.5% | 0.97 |
| grok-4-fast | 1/6 | 16.7% | 100.0% | 28.6% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 92.3% | 96.0% | 0.96 |
| deepseek-v3-2 | 4/5 | 80.0% | 66.7% | 72.7% | 1.00 |
| gemini-3-pro | 4/5 | 80.0% | 85.7% | 82.8% | 0.97 |
| llama-4-maverick | 4/5 | 80.0% | 36.4% | 50.0% | 0.88 |
| qwen3-coder-plus | 4/5 | 80.0% | 57.1% | 66.7% | 0.97 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| grok-4-fast | 2/5 | 40.0% | 100.0% | 57.1% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 83.3% | 90.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 40.0% | 57.1% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 50.0% | 66.7% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 25.0% | 33.3% | 1.00 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
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
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 75.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
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

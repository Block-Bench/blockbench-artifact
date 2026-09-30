# TC Nocomments - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 67.4% | 85.8% | 75.5% | 97.8% | 0.98 | 0.96 | 0.98 | 2.5 | 14.2% |
| 2 | deepseek-v3-2 | 63.0% | 61.8% | 62.4% | 100.0% | 0.98 | 0.93 | 0.98 | 2.2 | 38.2% |
| 3 | gpt-5.2 | 58.7% | 97.3% | 73.2% | 89.1% | 0.98 | 0.96 | 1.00 | 1.6 | 2.7% |
| 4 | llama-4-maverick | 50.0% | 35.3% | 41.4% | 100.0% | 0.93 | 0.83 | 0.96 | 2.2 | 64.7% |
| 5 | gemini-3-pro | 45.7% | 88.7% | 60.3% | 78.3% | 1.00 | 0.99 | 1.00 | 1.3 | 11.3% |
| 6 | qwen3-coder-plus | 45.7% | 50.6% | 48.0% | 97.8% | 0.95 | 0.89 | 0.93 | 1.7 | 49.4% |
| 7 | grok-4-fast | 30.4% | 95.3% | 46.1% | 67.4% | 1.00 | 0.97 | 1.00 | 0.9 | 4.7% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 31/46 | 32.6% | 0.0% | 84.8% | 97 | 16 | 0.35 |
| deepseek-v3-2 | 29/46 | 37.0% | 17.4% | 47.8% | 63 | 39 | 0.85 |
| gpt-5.2 | 27/46 | 41.3% | 0.0% | 65.2% | 72 | 2 | 0.04 |
| llama-4-maverick | 23/46 | 50.0% | 37.0% | 23.9% | 36 | 66 | 1.43 |
| gemini-3-pro | 21/46 | 54.3% | 4.3% | 50.0% | 55 | 7 | 0.15 |
| qwen3-coder-plus | 21/46 | 54.3% | 34.8% | 28.3% | 39 | 38 | 0.83 |
| grok-4-fast | 14/46 | 69.6% | 0.0% | 43.5% | 41 | 2 | 0.04 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 9/12 | 75.0% | 50.0% | 60.0% | 0.98 |
| claude-opus-4-5 | 8/12 | 66.7% | 79.2% | 72.4% | 0.99 |
| gpt-5.2 | 8/12 | 66.7% | 100.0% | 80.0% | 0.99 |
| qwen3-coder-plus | 7/12 | 58.3% | 52.9% | 55.5% | 0.93 |
| gemini-3-pro | 6/12 | 50.0% | 90.9% | 64.5% | 1.00 |
| llama-4-maverick | 6/12 | 50.0% | 37.5% | 42.9% | 0.92 |
| grok-4-fast | 4/12 | 33.3% | 100.0% | 50.0% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 6/7 | 85.7% | 42.9% | 57.1% | 0.93 |
| claude-opus-4-5 | 4/7 | 57.1% | 80.0% | 66.7% | 0.97 |
| gpt-5.2 | 3/7 | 42.9% | 100.0% | 60.0% | 0.97 |
| deepseek-v3-2 | 2/7 | 28.6% | 52.9% | 37.1% | 1.00 |
| qwen3-coder-plus | 2/7 | 28.6% | 30.8% | 29.6% | 0.95 |
| gemini-3-pro | 1/7 | 14.3% | 77.8% | 24.1% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 94.4% | 78.2% | 1.00 |
| gpt-5.2 | 4/6 | 66.7% | 100.0% | 80.0% | 0.97 |
| llama-4-maverick | 4/6 | 66.7% | 53.8% | 59.6% | 0.97 |
| deepseek-v3-2 | 3/6 | 50.0% | 68.8% | 57.9% | 0.97 |
| gemini-3-pro | 2/6 | 33.3% | 100.0% | 50.0% | 0.95 |
| qwen3-coder-plus | 2/6 | 33.3% | 58.3% | 42.4% | 1.00 |
| grok-4-fast | 1/6 | 16.7% | 100.0% | 28.6% | 1.00 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/5 | 80.0% | 92.3% | 85.7% | 0.95 |
| deepseek-v3-2 | 4/5 | 80.0% | 54.5% | 64.9% | 1.00 |
| qwen3-coder-plus | 4/5 | 80.0% | 71.4% | 75.5% | 0.95 |
| gemini-3-pro | 3/5 | 60.0% | 88.9% | 71.6% | 1.00 |
| gpt-5.2 | 2/5 | 40.0% | 87.5% | 54.9% | 1.00 |
| grok-4-fast | 2/5 | 40.0% | 83.3% | 54.1% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 30.0% | 34.3% | 0.95 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 33.3% | 40.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 80.0% | 61.5% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 75.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 75.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 80.0% | 88.9% | 0.90 |
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
| llama-4-maverick | 0/1 | 0.0% | 25.0% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 75.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 66.7% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
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

# TC Chameleon Medical - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:44:07 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 54.3% | 79.8% | 64.7% | 95.7% | 0.99 | 0.98 | 0.99 | 2.5 | 20.2% |
| 2 | gemini-3-pro | 52.2% | 96.2% | 67.6% | 97.8% | 0.99 | 0.97 | 1.00 | 1.7 | 3.8% |
| 3 | deepseek-v3-2 | 45.7% | 63.4% | 53.1% | 97.8% | 0.92 | 0.84 | 0.93 | 2.4 | 36.6% |
| 4 | gpt-5.2 | 45.7% | 98.6% | 62.4% | 91.3% | 0.99 | 0.97 | 0.98 | 1.5 | 1.4% |
| 5 | grok-4-fast | 34.8% | 88.0% | 49.9% | 67.4% | 0.97 | 0.94 | 0.97 | 1.1 | 12.0% |
| 6 | llama-4-maverick | 28.3% | 30.6% | 29.4% | 100.0% | 0.90 | 0.75 | 0.89 | 2.6 | 69.4% |
| 7 | qwen3-coder-plus | 17.4% | 49.0% | 25.7% | 100.0% | 0.99 | 0.94 | 1.00 | 2.1 | 51.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 25/46 | 45.7% | 2.2% | 84.8% | 91 | 23 | 0.50 |
| gemini-3-pro | 24/46 | 47.8% | 0.0% | 76.1% | 75 | 3 | 0.07 |
| deepseek-v3-2 | 21/46 | 54.3% | 8.7% | 76.1% | 71 | 41 | 0.89 |
| gpt-5.2 | 21/46 | 54.3% | 2.2% | 65.2% | 69 | 1 | 0.02 |
| grok-4-fast | 16/46 | 65.2% | 2.2% | 45.7% | 44 | 6 | 0.13 |
| llama-4-maverick | 13/46 | 71.7% | 41.3% | 37.0% | 37 | 84 | 1.83 |
| qwen3-coder-plus | 8/46 | 82.6% | 30.4% | 58.7% | 47 | 49 | 1.07 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 9/12 | 75.0% | 93.8% | 83.3% | 0.98 |
| claude-opus-4-5 | 8/12 | 66.7% | 77.8% | 71.8% | 1.00 |
| deepseek-v3-2 | 7/12 | 58.3% | 46.4% | 51.7% | 0.96 |
| gemini-3-pro | 7/12 | 58.3% | 100.0% | 73.7% | 1.00 |
| grok-4-fast | 6/12 | 50.0% | 100.0% | 66.7% | 0.93 |
| qwen3-coder-plus | 6/12 | 50.0% | 66.7% | 57.1% | 0.98 |
| llama-4-maverick | 5/12 | 41.7% | 40.0% | 40.8% | 0.90 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 5/7 | 71.4% | 42.1% | 53.0% | 0.88 |
| deepseek-v3-2 | 4/7 | 57.1% | 73.7% | 64.4% | 0.90 |
| claude-opus-4-5 | 2/7 | 28.6% | 57.1% | 38.1% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 91.7% | 43.6% | 1.00 |
| gpt-5.2 | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 80.0% | 24.2% | 1.00 |
| qwen3-coder-plus | 0/7 | 0.0% | 47.1% | N/A | N/A |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 100.0% | 80.0% | 1.00 |
| gemini-3-pro | 4/6 | 66.7% | 100.0% | 80.0% | 0.97 |
| deepseek-v3-2 | 1/6 | 16.7% | 80.0% | 27.6% | 0.90 |
| gpt-5.2 | 1/6 | 16.7% | 100.0% | 28.6% | 1.00 |
| grok-4-fast | 1/6 | 16.7% | 88.9% | 28.1% | 0.90 |
| llama-4-maverick | 0/6 | 0.0% | 29.4% | N/A | N/A |
| qwen3-coder-plus | 0/6 | 0.0% | 41.7% | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/5 | 80.0% | 80.0% | 80.0% | 0.93 |
| claude-opus-4-5 | 3/5 | 60.0% | 84.6% | 70.2% | 0.97 |
| gemini-3-pro | 3/5 | 60.0% | 85.7% | 70.6% | 0.97 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| grok-4-fast | 3/5 | 60.0% | 85.7% | 70.6% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 36.4% | 38.1% | 0.90 |
| qwen3-coder-plus | 0/5 | 0.0% | 36.4% | N/A | N/A |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 60.0% | 54.5% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 75.0% | 60.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 60.0% | 54.5% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | 20.0% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 50.0% | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | 60.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 16.7% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 20.0% | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.70 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 75.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

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

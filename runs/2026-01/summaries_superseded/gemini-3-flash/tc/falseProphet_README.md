# TC Falseprophet - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 67.4% | 85.5% | 75.4% | 100.0% | 0.99 | 0.97 | 0.99 | 2.4 | 14.5% |
| 2 | qwen3-coder-plus | 65.2% | 70.8% | 67.9% | 100.0% | 0.98 | 0.92 | 0.97 | 1.6 | 29.2% |
| 3 | deepseek-v3-2 | 60.9% | 60.0% | 60.4% | 100.0% | 0.94 | 0.90 | 0.94 | 2.2 | 40.0% |
| 4 | gemini-3-pro | 56.5% | 92.3% | 70.1% | 80.4% | 0.99 | 0.97 | 1.00 | 1.4 | 7.7% |
| 5 | gpt-5.2 | 52.2% | 100.0% | 68.6% | 91.3% | 0.97 | 0.96 | 0.98 | 1.5 | 0.0% |
| 6 | llama-4-maverick | 45.7% | 35.1% | 39.7% | 100.0% | 0.92 | 0.82 | 0.88 | 2.0 | 64.9% |
| 7 | grok-4-fast | 34.8% | 95.7% | 51.0% | 71.7% | 0.97 | 0.95 | 0.98 | 1.0 | 4.3% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 31/46 | 32.6% | 2.2% | 78.3% | 94 | 16 | 0.35 |
| qwen3-coder-plus | 30/46 | 34.8% | 17.4% | 28.3% | 51 | 21 | 0.46 |
| deepseek-v3-2 | 28/46 | 39.1% | 15.2% | 50.0% | 60 | 40 | 0.87 |
| gemini-3-pro | 26/46 | 43.5% | 2.2% | 50.0% | 60 | 5 | 0.11 |
| gpt-5.2 | 24/46 | 47.8% | 0.0% | 69.6% | 71 | 0 | 0.00 |
| llama-4-maverick | 21/46 | 54.3% | 41.3% | 19.6% | 33 | 61 | 1.33 |
| grok-4-fast | 16/46 | 65.2% | 0.0% | 45.7% | 45 | 2 | 0.04 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 8/12 | 66.7% | 68.0% | 67.3% | 0.97 |
| llama-4-maverick | 8/12 | 66.7% | 52.0% | 58.4% | 0.93 |
| deepseek-v3-2 | 7/12 | 58.3% | 57.1% | 57.7% | 0.96 |
| gemini-3-pro | 7/12 | 58.3% | 80.0% | 67.5% | 1.00 |
| gpt-5.2 | 7/12 | 58.3% | 100.0% | 73.7% | 0.99 |
| qwen3-coder-plus | 6/12 | 50.0% | 50.0% | 50.0% | 1.00 |
| grok-4-fast | 5/12 | 41.7% | 100.0% | 58.8% | 0.94 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 7/7 | 100.0% | 81.8% | 90.0% | 0.97 |
| claude-opus-4-5 | 5/7 | 71.4% | 100.0% | 83.3% | 1.00 |
| deepseek-v3-2 | 3/7 | 42.9% | 40.0% | 41.4% | 0.97 |
| gemini-3-pro | 3/7 | 42.9% | 90.9% | 58.3% | 0.97 |
| gpt-5.2 | 3/7 | 42.9% | 100.0% | 60.0% | 0.87 |
| llama-4-maverick | 3/7 | 42.9% | 36.4% | 39.3% | 0.97 |
| grok-4-fast | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/6 | 83.3% | 93.8% | 88.2% | 0.98 |
| gemini-3-pro | 4/6 | 66.7% | 91.7% | 77.2% | 0.97 |
| llama-4-maverick | 4/6 | 66.7% | 46.2% | 54.5% | 1.00 |
| qwen3-coder-plus | 3/6 | 50.0% | 87.5% | 63.6% | 1.00 |
| deepseek-v3-2 | 2/6 | 33.3% | 86.7% | 48.1% | 0.85 |
| gpt-5.2 | 1/6 | 16.7% | 100.0% | 28.6% | 1.00 |
| grok-4-fast | 1/6 | 16.7% | 80.0% | 27.6% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 5/5 | 100.0% | 72.7% | 84.2% | 0.96 |
| qwen3-coder-plus | 5/5 | 100.0% | 72.7% | 84.2% | 0.96 |
| claude-opus-4-5 | 3/5 | 60.0% | 92.9% | 72.9% | 0.97 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| grok-4-fast | 3/5 | 60.0% | 85.7% | 70.6% | 1.00 |
| gemini-3-pro | 2/5 | 40.0% | 100.0% | 57.1% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 18.2% | 25.0% | 0.80 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 83.3% | 90.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 75.0% | 85.7% | 0.95 |
| qwen3-coder-plus | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 0.60 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 75.0% | 85.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
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

# TC Minimalsanitized - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 78.3% | 81.8% | 80.0% | 97.8% | 0.91 | 0.89 | 0.86 | 2.4 | 18.2% |
| 2 | deepseek-v3-2 | 71.7% | 78.8% | 75.1% | 100.0% | 0.91 | 0.86 | 0.82 | 2.2 | 21.2% |
| 3 | gemini-3-pro | 63.0% | 64.5% | 63.8% | 97.8% | 0.94 | 0.93 | 0.85 | 1.7 | 35.5% |
| 4 | gpt-5.2 | 63.0% | 84.1% | 72.0% | 91.3% | 0.91 | 0.90 | 0.83 | 1.5 | 15.9% |
| 5 | qwen3-coder-plus | 60.9% | 62.3% | 61.6% | 100.0% | 0.91 | 0.87 | 0.84 | 1.7 | 37.7% |
| 6 | grok-4-fast | 39.1% | 68.4% | 49.8% | 67.4% | 0.95 | 0.94 | 0.92 | 0.8 | 31.6% |
| 7 | llama-4-maverick | 39.1% | 37.0% | 38.0% | 100.0% | 0.89 | 0.84 | 0.77 | 2.2 | 63.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 36/46 | 21.7% | 8.7% | 67.4% | 90 | 20 | 0.43 |
| deepseek-v3-2 | 33/46 | 28.3% | 13.0% | 52.2% | 78 | 21 | 0.46 |
| gemini-3-pro | 29/46 | 37.0% | 26.1% | 30.4% | 49 | 27 | 0.59 |
| gpt-5.2 | 29/46 | 37.0% | 17.4% | 43.5% | 58 | 11 | 0.24 |
| qwen3-coder-plus | 28/46 | 39.1% | 32.6% | 26.1% | 48 | 29 | 0.63 |
| grok-4-fast | 18/46 | 60.9% | 23.9% | 10.9% | 26 | 12 | 0.26 |
| llama-4-maverick | 18/46 | 60.9% | 54.3% | 17.4% | 37 | 63 | 1.37 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 8/12 | 66.7% | 100.0% | 80.0% | 0.91 |
| deepseek-v3-2 | 7/12 | 58.3% | 81.8% | 68.1% | 0.91 |
| gemini-3-pro | 7/12 | 58.3% | 69.2% | 63.3% | 0.97 |
| gpt-5.2 | 7/12 | 58.3% | 78.6% | 67.0% | 0.91 |
| qwen3-coder-plus | 6/12 | 50.0% | 61.1% | 55.0% | 0.88 |
| grok-4-fast | 5/12 | 41.7% | 85.7% | 56.1% | 0.98 |
| llama-4-maverick | 5/12 | 41.7% | 41.7% | 41.7% | 0.88 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/7 | 71.4% | 66.7% | 69.0% | 0.96 |
| deepseek-v3-2 | 4/7 | 57.1% | 71.4% | 63.5% | 0.97 |
| qwen3-coder-plus | 4/7 | 57.1% | 57.1% | 57.1% | 1.00 |
| gemini-3-pro | 3/7 | 42.9% | 50.0% | 46.2% | 0.97 |
| gpt-5.2 | 2/7 | 28.6% | 62.5% | 39.2% | 0.95 |
| llama-4-maverick | 2/7 | 28.6% | 33.3% | 30.8% | 0.95 |
| grok-4-fast | 1/7 | 14.3% | 60.0% | 23.1% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 5/6 | 83.3% | 100.0% | 90.9% | 0.90 |
| claude-opus-4-5 | 4/6 | 66.7% | 76.5% | 71.2% | 0.93 |
| deepseek-v3-2 | 4/6 | 66.7% | 66.7% | 66.7% | 0.90 |
| gemini-3-pro | 4/6 | 66.7% | 57.1% | 61.5% | 0.93 |
| qwen3-coder-plus | 4/6 | 66.7% | 90.9% | 76.9% | 0.90 |
| grok-4-fast | 3/6 | 50.0% | 80.0% | 61.5% | 0.90 |
| llama-4-maverick | 3/6 | 50.0% | 76.9% | 60.6% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 76.9% | 87.0% | 0.90 |
| deepseek-v3-2 | 5/5 | 100.0% | 91.7% | 95.7% | 0.88 |
| gemini-3-pro | 5/5 | 100.0% | 85.7% | 92.3% | 0.98 |
| qwen3-coder-plus | 5/5 | 100.0% | 71.4% | 83.3% | 0.90 |
| gpt-5.2 | 3/5 | 60.0% | 75.0% | 66.7% | 0.90 |
| llama-4-maverick | 3/5 | 60.0% | 27.3% | 37.5% | 0.87 |
| grok-4-fast | 1/5 | 20.0% | 25.0% | 22.2% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.85 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gemini-3-pro | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 33.3% | 40.0% | 0.90 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.80 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
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

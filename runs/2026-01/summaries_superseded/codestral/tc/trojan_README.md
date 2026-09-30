# TC Trojan - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | deepseek-v3-2 | 63.0% | 57.0% | 59.9% | 97.8% | 0.90 | 0.88 | 0.84 | 2.0 | 43.0% |
| 2 | claude-opus-4-5 | 60.9% | 70.1% | 65.2% | 97.8% | 0.92 | 0.91 | 0.86 | 2.3 | 29.9% |
| 3 | gpt-5.2 | 60.9% | 85.9% | 71.3% | 89.1% | 0.90 | 0.89 | 0.83 | 1.4 | 14.1% |
| 4 | llama-4-maverick | 56.5% | 43.9% | 49.4% | 100.0% | 0.90 | 0.84 | 0.81 | 2.1 | 56.1% |
| 5 | qwen3-coder-plus | 56.5% | 53.5% | 55.0% | 100.0% | 0.91 | 0.87 | 0.83 | 1.5 | 46.5% |
| 6 | gemini-3-pro | 43.5% | 63.8% | 51.7% | 82.6% | 0.97 | 0.97 | 0.93 | 1.5 | 36.2% |
| 7 | grok-4-fast | 32.6% | 68.4% | 44.2% | 58.7% | 0.94 | 0.93 | 0.88 | 0.8 | 31.6% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| deepseek-v3-2 | 29/46 | 37.0% | 26.1% | 41.3% | 53 | 40 | 0.87 |
| claude-opus-4-5 | 28/46 | 39.1% | 21.7% | 63.0% | 75 | 32 | 0.70 |
| gpt-5.2 | 28/46 | 39.1% | 13.0% | 39.1% | 55 | 9 | 0.20 |
| llama-4-maverick | 26/46 | 43.5% | 34.8% | 23.9% | 43 | 55 | 1.20 |
| qwen3-coder-plus | 26/46 | 43.5% | 34.8% | 17.4% | 38 | 33 | 0.72 |
| gemini-3-pro | 20/46 | 56.5% | 28.3% | 34.8% | 44 | 25 | 0.54 |
| grok-4-fast | 15/46 | 67.4% | 17.4% | 13.0% | 26 | 12 | 0.26 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 10/12 | 83.3% | 75.0% | 78.9% | 0.91 |
| claude-opus-4-5 | 9/12 | 75.0% | 95.7% | 84.1% | 0.90 |
| llama-4-maverick | 8/12 | 66.7% | 68.0% | 67.3% | 0.89 |
| qwen3-coder-plus | 8/12 | 66.7% | 77.8% | 71.8% | 0.91 |
| gpt-5.2 | 7/12 | 58.3% | 78.6% | 67.0% | 0.89 |
| gemini-3-pro | 5/12 | 41.7% | 72.7% | 53.0% | 0.96 |
| grok-4-fast | 4/12 | 33.3% | 83.3% | 47.6% | 0.95 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 5/7 | 71.4% | 66.7% | 69.0% | 0.96 |
| claude-opus-4-5 | 4/7 | 57.1% | 80.0% | 66.7% | 0.97 |
| deepseek-v3-2 | 4/7 | 57.1% | 60.0% | 58.5% | 0.95 |
| gpt-5.2 | 4/7 | 57.1% | 75.0% | 64.9% | 0.93 |
| llama-4-maverick | 4/7 | 57.1% | 45.5% | 50.6% | 0.93 |
| gemini-3-pro | 1/7 | 14.3% | 36.4% | 20.5% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 75.0% | 24.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 4/6 | 66.7% | 100.0% | 80.0% | 0.93 |
| claude-opus-4-5 | 3/6 | 50.0% | 70.6% | 58.5% | 0.93 |
| gemini-3-pro | 3/6 | 50.0% | 66.7% | 57.1% | 0.97 |
| llama-4-maverick | 3/6 | 50.0% | 50.0% | 50.0% | 0.93 |
| deepseek-v3-2 | 1/6 | 16.7% | 14.3% | 15.4% | 0.90 |
| grok-4-fast | 1/6 | 16.7% | 75.0% | 27.3% | 0.90 |
| qwen3-coder-plus | 1/6 | 16.7% | 33.3% | 22.2% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 4/5 | 80.0% | 66.7% | 72.7% | 0.93 |
| deepseek-v3-2 | 3/5 | 60.0% | 75.0% | 66.7% | 0.93 |
| gemini-3-pro | 3/5 | 60.0% | 66.7% | 63.2% | 1.00 |
| gpt-5.2 | 3/5 | 60.0% | 62.5% | 61.2% | 0.90 |
| llama-4-maverick | 3/5 | 60.0% | 50.0% | 54.5% | 0.90 |
| qwen3-coder-plus | 3/5 | 60.0% | 42.9% | 50.0% | 0.87 |
| claude-opus-4-5 | 2/5 | 40.0% | 69.2% | 50.7% | 0.90 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 40.0% | 57.1% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.50 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | N/A |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
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

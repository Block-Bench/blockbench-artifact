# TC Shapeshifter L3 - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 63.0% | 68.1% | 65.5% | 100.0% | 0.91 | 0.90 | 0.87 | 2.5 | 31.9% |
| 2 | gpt-5.2 | 50.0% | 74.2% | 59.8% | 91.3% | 0.93 | 0.93 | 0.87 | 1.4 | 25.8% |
| 3 | deepseek-v3-2 | 47.8% | 55.9% | 51.5% | 97.8% | 0.92 | 0.90 | 0.86 | 2.2 | 44.1% |
| 4 | gemini-3-pro | 43.5% | 63.8% | 51.7% | 78.3% | 0.94 | 0.94 | 0.93 | 1.3 | 36.2% |
| 5 | llama-4-maverick | 37.0% | 27.6% | 31.6% | 100.0% | 0.86 | 0.81 | 0.74 | 2.3 | 72.4% |
| 6 | qwen3-coder-plus | 37.0% | 39.4% | 38.2% | 97.8% | 0.89 | 0.84 | 0.81 | 1.5 | 60.6% |
| 7 | grok-4-fast | 30.4% | 50.0% | 37.8% | 69.6% | 0.99 | 0.99 | 0.92 | 0.9 | 50.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 29/46 | 37.0% | 23.9% | 63.0% | 77 | 36 | 0.78 |
| gpt-5.2 | 23/46 | 50.0% | 23.9% | 43.5% | 49 | 17 | 0.37 |
| deepseek-v3-2 | 22/46 | 52.2% | 34.8% | 47.8% | 57 | 45 | 0.98 |
| gemini-3-pro | 20/46 | 56.5% | 19.6% | 23.9% | 37 | 21 | 0.46 |
| llama-4-maverick | 17/46 | 63.0% | 54.3% | 15.2% | 29 | 76 | 1.65 |
| qwen3-coder-plus | 17/46 | 63.0% | 52.2% | 19.6% | 28 | 43 | 0.93 |
| grok-4-fast | 14/46 | 69.6% | 30.4% | 10.9% | 20 | 20 | 0.43 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 10/12 | 83.3% | 88.9% | 86.0% | 0.89 |
| deepseek-v3-2 | 8/12 | 66.7% | 65.2% | 65.9% | 0.91 |
| gpt-5.2 | 8/12 | 66.7% | 85.7% | 75.0% | 0.93 |
| llama-4-maverick | 8/12 | 66.7% | 40.7% | 50.6% | 0.81 |
| gemini-3-pro | 7/12 | 58.3% | 90.0% | 70.8% | 0.93 |
| qwen3-coder-plus | 6/12 | 50.0% | 68.8% | 57.9% | 0.87 |
| grok-4-fast | 5/12 | 41.7% | 77.8% | 54.3% | 0.98 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/7 | 71.4% | 80.0% | 75.5% | 0.94 |
| qwen3-coder-plus | 5/7 | 71.4% | 80.0% | 75.5% | 0.96 |
| llama-4-maverick | 4/7 | 57.1% | 58.3% | 57.7% | 0.93 |
| deepseek-v3-2 | 3/7 | 42.9% | 52.9% | 47.4% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 54.5% | 37.5% | 1.00 |
| gpt-5.2 | 2/7 | 28.6% | 75.0% | 41.4% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 50.0% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 58.8% | 62.5% | 0.95 |
| gpt-5.2 | 3/6 | 50.0% | 90.9% | 64.5% | 0.90 |
| gemini-3-pro | 2/6 | 33.3% | 50.0% | 40.0% | 0.90 |
| llama-4-maverick | 1/6 | 16.7% | 13.3% | 14.8% | 0.90 |
| qwen3-coder-plus | 1/6 | 16.7% | 18.2% | 17.4% | 0.90 |
| deepseek-v3-2 | 0/6 | 0.0% | 17.6% | N/A | N/A |
| grok-4-fast | 0/6 | 0.0% | N/A | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/5 | 80.0% | 72.7% | 76.2% | 0.93 |
| gemini-3-pro | 4/5 | 80.0% | 50.0% | 61.5% | 1.00 |
| claude-opus-4-5 | 3/5 | 60.0% | 61.5% | 60.8% | 0.90 |
| gpt-5.2 | 2/5 | 40.0% | 71.4% | 51.3% | 0.90 |
| llama-4-maverick | 2/5 | 40.0% | 18.2% | 25.0% | 0.85 |
| grok-4-fast | 1/5 | 20.0% | 20.0% | 20.0% | 1.00 |
| qwen3-coder-plus | 1/5 | 20.0% | 9.1% | 12.5% | 0.80 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| gemini-3-pro | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 25.0% | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| gemini-3-pro | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
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

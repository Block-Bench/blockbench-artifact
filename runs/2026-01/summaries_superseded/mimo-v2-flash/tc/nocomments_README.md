# TC Nocomments - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | deepseek-v3-2 | 67.4% | 42.2% | 51.9% | 100.0% | 0.93 | 0.92 | 0.88 | 2.2 | 57.8% |
| 2 | claude-opus-4-5 | 60.9% | 54.0% | 57.2% | 97.8% | 0.93 | 0.91 | 0.92 | 2.5 | 46.0% |
| 3 | gpt-5.2 | 60.9% | 62.2% | 61.5% | 89.1% | 0.95 | 0.95 | 0.90 | 1.6 | 37.8% |
| 4 | llama-4-maverick | 51.1% | 23.2% | 31.9% | 100.0% | 0.83 | 0.79 | 0.81 | 2.2 | 76.8% |
| 5 | gemini-3-pro | 41.3% | 61.3% | 49.4% | 78.3% | 0.99 | 0.99 | 0.96 | 1.3 | 38.7% |
| 6 | qwen3-coder-plus | 40.0% | 29.7% | 34.1% | 97.8% | 0.88 | 0.86 | 0.83 | 1.6 | 70.3% |
| 7 | grok-4-fast | 28.9% | 62.5% | 39.5% | 66.7% | 0.97 | 0.97 | 0.93 | 0.9 | 37.5% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| deepseek-v3-2 | 31/46 | 32.6% | 26.1% | 17.4% | 43 | 59 | 1.28 |
| claude-opus-4-5 | 28/46 | 39.1% | 10.9% | 45.7% | 61 | 52 | 1.13 |
| gpt-5.2 | 28/46 | 39.1% | 10.9% | 26.1% | 46 | 28 | 0.61 |
| llama-4-maverick | 23/45 | 48.9% | 48.9% | 2.2% | 23 | 76 | 1.69 |
| gemini-3-pro | 19/46 | 58.7% | 15.2% | 30.4% | 38 | 24 | 0.52 |
| qwen3-coder-plus | 18/45 | 60.0% | 55.6% | 4.4% | 22 | 52 | 1.16 |
| grok-4-fast | 13/45 | 71.1% | 24.4% | 17.8% | 25 | 15 | 0.33 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 10/12 | 83.3% | 59.1% | 69.1% | 0.93 |
| claude-opus-4-5 | 8/12 | 66.7% | 62.5% | 64.5% | 0.93 |
| gpt-5.2 | 8/12 | 66.7% | 64.3% | 65.5% | 0.96 |
| gemini-3-pro | 6/12 | 50.0% | 72.7% | 59.3% | 0.98 |
| llama-4-maverick | 5/12 | 41.7% | 20.8% | 27.8% | 0.86 |
| qwen3-coder-plus | 5/12 | 41.7% | 41.2% | 41.4% | 0.89 |
| grok-4-fast | 4/12 | 33.3% | 80.0% | 47.1% | 0.97 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 5/7 | 83.3% | 45.5% | 58.8% | 0.76 |
| claude-opus-4-5 | 4/7 | 57.1% | 46.7% | 51.4% | 0.89 |
| qwen3-coder-plus | 3/7 | 50.0% | 30.0% | 37.5% | 0.77 |
| deepseek-v3-2 | 3/7 | 42.9% | 23.5% | 30.4% | 0.87 |
| gpt-5.2 | 3/7 | 42.9% | 70.0% | 53.2% | 0.95 |
| gemini-3-pro | 1/7 | 14.3% | 44.4% | 21.6% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 50.0% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 5/6 | 83.3% | 38.5% | 52.6% | 0.92 |
| claude-opus-4-5 | 4/6 | 66.7% | 72.2% | 69.3% | 0.99 |
| gpt-5.2 | 4/6 | 66.7% | 33.3% | 44.4% | 0.97 |
| deepseek-v3-2 | 3/6 | 50.0% | 37.5% | 42.9% | 0.95 |
| gemini-3-pro | 1/6 | 16.7% | 66.7% | 26.7% | 1.00 |
| grok-4-fast | 1/6 | 16.7% | 50.0% | 25.0% | 0.90 |
| qwen3-coder-plus | 1/6 | 16.7% | 16.7% | 16.7% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/5 | 80.0% | 36.4% | 50.0% | 0.94 |
| qwen3-coder-plus | 4/5 | 80.0% | 71.4% | 75.5% | 0.86 |
| claude-opus-4-5 | 3/5 | 60.0% | 46.2% | 52.2% | 0.85 |
| gemini-3-pro | 3/5 | 60.0% | 66.7% | 63.2% | 1.00 |
| gpt-5.2 | 2/5 | 40.0% | 75.0% | 52.2% | 0.95 |
| grok-4-fast | 2/5 | 40.0% | 50.0% | 44.4% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 20.0% | 26.7% | 0.90 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 50.0% | 66.7% | 0.95 |
| deepseek-v3-2 | 2/2 | 100.0% | 50.0% | 66.7% | 0.95 |
| gemini-3-pro | 2/2 | 100.0% | 66.7% | 80.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 50.0% | 66.7% | 0.75 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 2/2 | 100.0% | 40.0% | 57.1% | 0.95 |
| claude-opus-4-5 | 1/2 | 50.0% | 25.0% | 33.3% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.95 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.60 |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 25.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 25.0% | 40.0% | 0.30 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.95 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
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

# TC Minimalsanitized - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 73.9% | 54.5% | 62.8% | 97.8% | 0.95 | 0.95 | 0.92 | 2.4 | 45.5% |
| 2 | deepseek-v3-2 | 66.7% | 43.9% | 52.9% | 100.0% | 0.89 | 0.90 | 0.87 | 2.2 | 56.1% |
| 3 | gemini-3-pro | 63.0% | 57.9% | 60.4% | 97.8% | 0.96 | 0.91 | 0.89 | 1.7 | 42.1% |
| 4 | gpt-5.2 | 63.0% | 81.2% | 71.0% | 91.3% | 0.96 | 0.98 | 0.94 | 1.5 | 18.8% |
| 5 | qwen3-coder-plus | 60.0% | 45.3% | 51.6% | 100.0% | 0.91 | 0.88 | 0.86 | 1.7 | 54.7% |
| 6 | llama-4-maverick | 53.3% | 29.6% | 38.1% | 100.0% | 0.89 | 0.86 | 0.82 | 2.2 | 70.4% |
| 7 | grok-4-fast | 37.8% | 55.6% | 45.0% | 66.7% | 0.96 | 0.96 | 0.94 | 0.8 | 44.4% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 34/46 | 26.1% | 19.6% | 43.5% | 60 | 50 | 1.09 |
| deepseek-v3-2 | 30/45 | 33.3% | 28.9% | 15.6% | 43 | 55 | 1.22 |
| gemini-3-pro | 29/46 | 37.0% | 23.9% | 23.9% | 44 | 32 | 0.70 |
| gpt-5.2 | 29/46 | 37.0% | 13.0% | 41.3% | 56 | 13 | 0.28 |
| qwen3-coder-plus | 27/45 | 40.0% | 33.3% | 13.3% | 34 | 41 | 0.91 |
| llama-4-maverick | 24/45 | 46.7% | 42.2% | 4.4% | 29 | 69 | 1.53 |
| grok-4-fast | 17/45 | 62.2% | 26.7% | 6.7% | 20 | 16 | 0.36 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 8/12 | 66.7% | 66.7% | 66.7% | 0.96 |
| gpt-5.2 | 8/12 | 66.7% | 92.9% | 77.6% | 0.91 |
| deepseek-v3-2 | 7/12 | 58.3% | 63.6% | 60.9% | 0.90 |
| gemini-3-pro | 7/12 | 58.3% | 69.2% | 63.3% | 0.99 |
| llama-4-maverick | 7/12 | 58.3% | 37.5% | 45.7% | 0.89 |
| qwen3-coder-plus | 6/12 | 50.0% | 44.4% | 47.1% | 0.93 |
| grok-4-fast | 5/12 | 41.7% | 85.7% | 56.1% | 0.95 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/7 | 57.1% | 53.3% | 55.2% | 0.97 |
| deepseek-v3-2 | 4/7 | 57.1% | 35.7% | 44.0% | 0.95 |
| llama-4-maverick | 4/7 | 57.1% | 33.3% | 42.1% | 0.88 |
| qwen3-coder-plus | 4/7 | 57.1% | 35.7% | 44.0% | 0.95 |
| gemini-3-pro | 3/7 | 42.9% | 50.0% | 46.2% | 0.97 |
| gpt-5.2 | 2/7 | 28.6% | 50.0% | 36.4% | 1.00 |
| grok-4-fast | 1/7 | 16.7% | 33.3% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 5/6 | 83.3% | 78.6% | 80.9% | 0.97 |
| qwen3-coder-plus | 4/6 | 80.0% | 66.7% | 72.7% | 0.93 |
| claude-opus-4-5 | 4/6 | 66.7% | 58.8% | 62.5% | 0.95 |
| llama-4-maverick | 4/6 | 66.7% | 38.5% | 48.8% | 0.93 |
| deepseek-v3-2 | 3/6 | 60.0% | 21.4% | 31.6% | 0.97 |
| gemini-3-pro | 3/6 | 50.0% | 42.9% | 46.2% | 0.97 |
| grok-4-fast | 2/6 | 33.3% | 40.0% | 36.4% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 61.5% | 76.2% | 0.80 |
| deepseek-v3-2 | 5/5 | 100.0% | 58.3% | 73.7% | 0.94 |
| gemini-3-pro | 5/5 | 100.0% | 71.4% | 83.3% | 0.92 |
| qwen3-coder-plus | 5/5 | 100.0% | 71.4% | 83.3% | 0.80 |
| gpt-5.2 | 3/5 | 60.0% | 87.5% | 71.2% | 0.98 |
| llama-4-maverick | 3/5 | 60.0% | 27.3% | 37.5% | 0.90 |
| grok-4-fast | 1/5 | 20.0% | 25.0% | 22.2% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 33.3% | 50.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 60.0% | 75.0% | 0.60 |
| gpt-5.2 | 2/2 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 1/2 | 50.0% | 33.3% | 40.0% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.95 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.60 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.30 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.85 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
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
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.95 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.60 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |

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

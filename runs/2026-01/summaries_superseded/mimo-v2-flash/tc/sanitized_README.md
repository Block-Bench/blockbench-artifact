# TC Sanitized - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 64.4% | 52.3% | 57.7% | 97.8% | 0.95 | 0.94 | 0.92 | 2.4 | 47.7% |
| 2 | llama-4-maverick | 62.8% | 31.4% | 41.8% | 100.0% | 0.84 | 0.78 | 0.82 | 2.4 | 68.6% |
| 3 | qwen3-coder-plus | 60.0% | 51.5% | 55.4% | 97.8% | 0.91 | 0.90 | 0.87 | 1.5 | 48.5% |
| 4 | deepseek-v3-2 | 58.7% | 41.6% | 48.7% | 97.8% | 0.94 | 0.96 | 0.93 | 2.2 | 58.4% |
| 5 | gpt-5.2 | 51.1% | 75.4% | 60.9% | 86.7% | 0.98 | 0.99 | 0.96 | 1.4 | 24.6% |
| 6 | gemini-3-pro | 41.3% | 63.3% | 50.0% | 63.0% | 0.94 | 0.92 | 0.85 | 1.1 | 36.7% |
| 7 | grok-4-fast | 35.6% | 57.1% | 43.8% | 71.1% | 0.97 | 0.97 | 0.96 | 0.9 | 42.9% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 29/45 | 35.6% | 15.6% | 37.8% | 57 | 52 | 1.16 |
| llama-4-maverick | 27/43 | 37.2% | 30.2% | 9.3% | 32 | 70 | 1.63 |
| qwen3-coder-plus | 27/45 | 40.0% | 31.1% | 6.7% | 34 | 32 | 0.71 |
| deepseek-v3-2 | 27/46 | 41.3% | 32.6% | 19.6% | 42 | 59 | 1.28 |
| gpt-5.2 | 23/45 | 48.9% | 13.3% | 42.2% | 49 | 16 | 0.36 |
| gemini-3-pro | 19/46 | 58.7% | 13.0% | 19.6% | 31 | 18 | 0.39 |
| grok-4-fast | 16/45 | 64.4% | 26.7% | 13.3% | 24 | 18 | 0.40 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 8/12 | 72.7% | 45.8% | 56.2% | 0.85 |
| claude-opus-4-5 | 7/12 | 58.3% | 78.3% | 66.8% | 0.96 |
| deepseek-v3-2 | 7/12 | 58.3% | 46.2% | 51.5% | 0.95 |
| gpt-5.2 | 6/12 | 50.0% | 84.6% | 62.9% | 1.00 |
| grok-4-fast | 6/12 | 50.0% | 77.8% | 60.9% | 1.00 |
| gemini-3-pro | 5/12 | 41.7% | 70.0% | 52.2% | 0.98 |
| qwen3-coder-plus | 5/12 | 41.7% | 52.9% | 46.6% | 0.91 |

### Reentrancy (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 6/6 | 100.0% | 46.2% | 63.2% | 0.75 |
| qwen3-coder-plus | 6/6 | 85.7% | 66.7% | 75.0% | 0.88 |
| claude-opus-4-5 | 5/6 | 83.3% | 41.7% | 55.6% | 0.88 |
| deepseek-v3-2 | 3/6 | 42.9% | 30.8% | 35.8% | 1.00 |
| gemini-3-pro | 2/6 | 28.6% | 60.0% | 38.7% | 1.00 |
| gpt-5.2 | 2/6 | 28.6% | 70.0% | 40.6% | 1.00 |
| grok-4-fast | 1/6 | 14.3% | 50.0% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 5/6 | 83.3% | 46.2% | 59.4% | 0.90 |
| claude-opus-4-5 | 4/6 | 66.7% | 50.0% | 57.1% | 0.90 |
| deepseek-v3-2 | 4/6 | 66.7% | 33.3% | 44.4% | 0.93 |
| gpt-5.2 | 4/6 | 66.7% | 100.0% | 80.0% | 0.97 |
| qwen3-coder-plus | 4/6 | 66.7% | 50.0% | 57.1% | 0.95 |
| grok-4-fast | 3/6 | 50.0% | 71.4% | 58.8% | 0.90 |
| gemini-3-pro | 2/6 | 33.3% | 44.4% | 38.1% | 0.65 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 4/5 | 80.0% | 50.0% | 61.5% | 0.93 |
| gpt-5.2 | 3/5 | 75.0% | 100.0% | 85.7% | 1.00 |
| llama-4-maverick | 3/5 | 75.0% | 30.0% | 42.9% | 0.73 |
| claude-opus-4-5 | 3/5 | 60.0% | 38.5% | 46.9% | 0.97 |
| gemini-3-pro | 3/5 | 60.0% | 66.7% | 63.2% | 0.93 |
| deepseek-v3-2 | 2/5 | 40.0% | 28.6% | 33.3% | 0.95 |
| grok-4-fast | 1/5 | 20.0% | 33.3% | 25.0% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 60.0% | 75.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 40.0% | 57.1% | 0.97 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 20.0% | 28.6% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.40 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
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
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 25.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.85 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
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

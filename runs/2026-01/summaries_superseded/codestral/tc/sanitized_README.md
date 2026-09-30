# TC Sanitized - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 69.6% | 81.2% | 75.0% | 97.8% | 0.92 | 0.89 | 0.87 | 2.4 | 18.8% |
| 2 | deepseek-v3-2 | 63.0% | 70.3% | 66.5% | 95.7% | 0.91 | 0.89 | 0.83 | 2.2 | 29.7% |
| 3 | qwen3-coder-plus | 60.9% | 59.4% | 60.1% | 97.8% | 0.90 | 0.88 | 0.85 | 1.5 | 40.6% |
| 4 | gpt-5.2 | 56.5% | 78.8% | 65.8% | 87.0% | 0.91 | 0.90 | 0.83 | 1.4 | 21.2% |
| 5 | llama-4-maverick | 54.3% | 48.1% | 51.0% | 100.0% | 0.90 | 0.84 | 0.80 | 2.3 | 51.9% |
| 6 | gemini-3-pro | 47.8% | 67.3% | 55.9% | 63.0% | 0.96 | 0.82 | 0.78 | 1.1 | 32.7% |
| 7 | grok-4-fast | 39.1% | 67.4% | 49.5% | 71.7% | 0.96 | 0.96 | 0.93 | 0.9 | 32.6% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 32/46 | 30.4% | 13.0% | 67.4% | 91 | 21 | 0.46 |
| deepseek-v3-2 | 29/46 | 37.0% | 15.2% | 50.0% | 71 | 30 | 0.65 |
| qwen3-coder-plus | 28/46 | 39.1% | 30.4% | 13.0% | 41 | 28 | 0.61 |
| gpt-5.2 | 26/46 | 43.5% | 17.4% | 43.5% | 52 | 14 | 0.30 |
| llama-4-maverick | 25/46 | 45.7% | 34.8% | 32.6% | 51 | 55 | 1.20 |
| gemini-3-pro | 22/46 | 52.2% | 10.9% | 17.4% | 33 | 16 | 0.35 |
| grok-4-fast | 18/46 | 60.9% | 28.3% | 13.0% | 29 | 14 | 0.30 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 8/12 | 66.7% | 87.0% | 75.5% | 0.91 |
| deepseek-v3-2 | 8/12 | 66.7% | 84.6% | 74.6% | 0.91 |
| gpt-5.2 | 8/12 | 66.7% | 92.3% | 77.4% | 0.91 |
| llama-4-maverick | 8/12 | 66.7% | 61.5% | 64.0% | 0.88 |
| qwen3-coder-plus | 7/12 | 58.3% | 64.7% | 61.4% | 0.89 |
| gemini-3-pro | 5/12 | 41.7% | 80.0% | 54.8% | 1.00 |
| grok-4-fast | 5/12 | 41.7% | 100.0% | 58.8% | 0.96 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 6/7 | 85.7% | 73.3% | 79.0% | 0.92 |
| llama-4-maverick | 5/7 | 71.4% | 50.0% | 58.8% | 0.94 |
| qwen3-coder-plus | 5/7 | 71.4% | 77.8% | 74.5% | 0.94 |
| deepseek-v3-2 | 3/7 | 42.9% | 53.8% | 47.7% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 80.0% | 42.1% | 1.00 |
| gpt-5.2 | 2/7 | 28.6% | 50.0% | 36.4% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 25.0% | 18.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 6/6 | 100.0% | 84.6% | 91.7% | 0.92 |
| claude-opus-4-5 | 4/6 | 66.7% | 94.4% | 78.2% | 0.95 |
| deepseek-v3-2 | 4/6 | 66.7% | 77.8% | 71.8% | 0.88 |
| gpt-5.2 | 4/6 | 66.7% | 100.0% | 80.0% | 0.90 |
| grok-4-fast | 4/6 | 66.7% | 85.7% | 75.0% | 0.97 |
| qwen3-coder-plus | 4/6 | 66.7% | 70.0% | 68.3% | 0.93 |
| gemini-3-pro | 3/6 | 50.0% | 55.6% | 52.6% | 0.97 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 5/5 | 100.0% | 75.0% | 85.7% | 0.88 |
| gemini-3-pro | 4/5 | 80.0% | 66.7% | 72.7% | 0.95 |
| claude-opus-4-5 | 3/5 | 60.0% | 76.9% | 67.4% | 0.90 |
| gpt-5.2 | 3/5 | 60.0% | 85.7% | 70.6% | 0.90 |
| deepseek-v3-2 | 2/5 | 40.0% | 42.9% | 41.4% | 0.90 |
| llama-4-maverick | 2/5 | 40.0% | 18.2% | 25.0% | 0.85 |
| grok-4-fast | 1/5 | 20.0% | 33.3% | 25.0% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 80.0% | 88.9% | 0.95 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| gemini-3-pro | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
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

# TC Falseprophet - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | qwen3-coder-plus | 67.4% | 61.1% | 64.1% | 100.0% | 0.91 | 0.89 | 0.86 | 1.6 | 38.9% |
| 2 | claude-opus-4-5 | 65.2% | 67.3% | 66.2% | 100.0% | 0.92 | 0.91 | 0.86 | 2.4 | 32.7% |
| 3 | deepseek-v3-2 | 63.0% | 66.0% | 64.5% | 100.0% | 0.91 | 0.89 | 0.84 | 2.2 | 34.0% |
| 4 | gpt-5.2 | 54.3% | 81.7% | 65.3% | 91.3% | 0.92 | 0.92 | 0.87 | 1.5 | 18.3% |
| 5 | gemini-3-pro | 50.0% | 67.7% | 57.5% | 80.4% | 0.97 | 0.96 | 0.90 | 1.4 | 32.3% |
| 6 | llama-4-maverick | 39.1% | 36.2% | 37.6% | 100.0% | 0.88 | 0.84 | 0.77 | 2.0 | 63.8% |
| 7 | grok-4-fast | 32.6% | 53.2% | 40.4% | 71.7% | 0.97 | 0.95 | 0.93 | 1.0 | 46.8% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| qwen3-coder-plus | 31/46 | 32.6% | 30.4% | 21.7% | 44 | 28 | 0.61 |
| claude-opus-4-5 | 30/46 | 34.8% | 21.7% | 60.9% | 74 | 36 | 0.78 |
| deepseek-v3-2 | 29/46 | 37.0% | 23.9% | 50.0% | 66 | 34 | 0.74 |
| gpt-5.2 | 25/46 | 45.7% | 23.9% | 43.5% | 58 | 13 | 0.28 |
| gemini-3-pro | 23/46 | 50.0% | 23.9% | 30.4% | 44 | 21 | 0.46 |
| llama-4-maverick | 18/46 | 60.9% | 56.5% | 17.4% | 34 | 60 | 1.30 |
| grok-4-fast | 15/46 | 67.4% | 32.6% | 10.9% | 25 | 22 | 0.48 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 9/12 | 75.0% | 90.5% | 82.0% | 0.90 |
| claude-opus-4-5 | 7/12 | 58.3% | 56.0% | 57.1% | 0.91 |
| gpt-5.2 | 7/12 | 58.3% | 73.3% | 65.0% | 0.93 |
| llama-4-maverick | 7/12 | 58.3% | 48.0% | 52.7% | 0.87 |
| qwen3-coder-plus | 7/12 | 58.3% | 50.0% | 53.8% | 0.90 |
| gemini-3-pro | 6/12 | 50.0% | 73.3% | 59.5% | 0.95 |
| grok-4-fast | 4/12 | 33.3% | 80.0% | 47.1% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 6/7 | 85.7% | 72.7% | 78.7% | 0.98 |
| claude-opus-4-5 | 5/7 | 71.4% | 61.5% | 66.1% | 1.00 |
| deepseek-v3-2 | 4/7 | 57.1% | 53.3% | 55.2% | 1.00 |
| gemini-3-pro | 3/7 | 42.9% | 72.7% | 53.9% | 0.97 |
| llama-4-maverick | 3/7 | 42.9% | 45.5% | 44.1% | 0.93 |
| gpt-5.2 | 2/7 | 28.6% | 70.0% | 40.6% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 50.0% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 87.5% | 75.7% | 0.93 |
| qwen3-coder-plus | 4/6 | 66.7% | 75.0% | 70.6% | 0.90 |
| gemini-3-pro | 3/6 | 50.0% | 75.0% | 60.0% | 0.97 |
| gpt-5.2 | 3/6 | 50.0% | 90.9% | 64.5% | 0.90 |
| llama-4-maverick | 3/6 | 50.0% | 46.2% | 48.0% | 0.90 |
| deepseek-v3-2 | 2/6 | 33.3% | 40.0% | 36.4% | 0.90 |
| grok-4-fast | 2/6 | 33.3% | 80.0% | 47.1% | 0.90 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 5/5 | 100.0% | 90.9% | 95.2% | 0.90 |
| qwen3-coder-plus | 5/5 | 100.0% | 72.7% | 84.2% | 0.88 |
| gpt-5.2 | 3/5 | 60.0% | 87.5% | 71.2% | 0.93 |
| grok-4-fast | 3/5 | 60.0% | 42.9% | 50.0% | 0.97 |
| llama-4-maverick | 3/5 | 60.0% | 27.3% | 37.5% | 0.83 |
| claude-opus-4-5 | 2/5 | 40.0% | 64.3% | 49.3% | 0.90 |
| gemini-3-pro | 2/5 | 40.0% | 40.0% | 40.0% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.95 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| qwen3-coder-plus | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 75.0% | 60.0% | 0.80 |
| gemini-3-pro | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
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

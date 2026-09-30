# TC Chameleon Medical - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:44:07 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | gemini-3-pro | 58.7% | 56.4% | 57.5% | 97.8% | 0.93 | 0.91 | 0.89 | 1.7 | 43.6% |
| 2 | claude-opus-4-5 | 56.5% | 64.9% | 60.4% | 95.7% | 0.92 | 0.91 | 0.86 | 2.5 | 35.1% |
| 3 | gpt-5.2 | 54.3% | 78.6% | 64.3% | 91.3% | 0.92 | 0.90 | 0.84 | 1.5 | 21.4% |
| 4 | deepseek-v3-2 | 52.2% | 47.3% | 49.6% | 97.8% | 0.89 | 0.87 | 0.83 | 2.4 | 52.7% |
| 5 | grok-4-fast | 32.6% | 60.0% | 42.3% | 67.4% | 0.93 | 0.93 | 0.87 | 1.1 | 40.0% |
| 6 | llama-4-maverick | 30.4% | 18.2% | 22.8% | 100.0% | 0.90 | 0.86 | 0.86 | 2.6 | 81.8% |
| 7 | qwen3-coder-plus | 26.1% | 27.1% | 26.6% | 100.0% | 0.88 | 0.86 | 0.79 | 2.1 | 72.9% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| gemini-3-pro | 27/46 | 41.3% | 34.8% | 30.4% | 44 | 34 | 0.74 |
| claude-opus-4-5 | 26/46 | 43.5% | 17.4% | 56.5% | 74 | 40 | 0.87 |
| gpt-5.2 | 25/46 | 45.7% | 23.9% | 41.3% | 55 | 15 | 0.33 |
| deepseek-v3-2 | 24/46 | 47.8% | 32.6% | 32.6% | 53 | 59 | 1.28 |
| grok-4-fast | 15/46 | 67.4% | 26.1% | 21.7% | 30 | 20 | 0.43 |
| llama-4-maverick | 14/46 | 69.6% | 63.0% | 6.5% | 22 | 99 | 2.15 |
| qwen3-coder-plus | 12/46 | 73.9% | 58.7% | 19.6% | 26 | 70 | 1.52 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 9/12 | 75.0% | 70.4% | 72.6% | 0.90 |
| deepseek-v3-2 | 9/12 | 75.0% | 67.9% | 71.2% | 0.89 |
| gpt-5.2 | 9/12 | 75.0% | 81.2% | 78.0% | 0.91 |
| qwen3-coder-plus | 7/12 | 58.3% | 50.0% | 53.8% | 0.89 |
| gemini-3-pro | 6/12 | 50.0% | 53.8% | 51.9% | 0.92 |
| llama-4-maverick | 5/12 | 41.7% | 23.3% | 29.9% | 0.88 |
| grok-4-fast | 4/12 | 33.3% | 55.6% | 41.7% | 0.97 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/7 | 57.1% | 36.8% | 44.8% | 0.93 |
| llama-4-maverick | 4/7 | 57.1% | 36.8% | 44.8% | 0.88 |
| claude-opus-4-5 | 2/7 | 28.6% | 21.4% | 24.5% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 50.0% | 36.4% | 1.00 |
| gpt-5.2 | 1/7 | 14.3% | 62.5% | 23.3% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 60.0% | 23.1% | 1.00 |
| qwen3-coder-plus | 0/7 | 0.0% | 17.6% | N/A | N/A |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 76.5% | 71.2% | 0.93 |
| gemini-3-pro | 4/6 | 66.7% | 53.8% | 59.6% | 0.90 |
| deepseek-v3-2 | 3/6 | 50.0% | 33.3% | 40.0% | 0.80 |
| grok-4-fast | 3/6 | 50.0% | 44.4% | 47.1% | 0.87 |
| gpt-5.2 | 2/6 | 33.3% | 92.3% | 49.0% | 0.90 |
| llama-4-maverick | 1/6 | 16.7% | 5.9% | 8.7% | 1.00 |
| qwen3-coder-plus | 0/6 | 0.0% | 25.0% | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/5 | 80.0% | 85.7% | 82.8% | 0.97 |
| gpt-5.2 | 4/5 | 80.0% | 87.5% | 83.6% | 0.90 |
| claude-opus-4-5 | 3/5 | 60.0% | 53.8% | 56.8% | 0.97 |
| deepseek-v3-2 | 3/5 | 60.0% | 30.0% | 40.0% | 0.90 |
| grok-4-fast | 3/5 | 60.0% | 85.7% | 70.6% | 0.93 |
| llama-4-maverick | 2/5 | 40.0% | 18.2% | 25.0% | 0.95 |
| qwen3-coder-plus | 1/5 | 20.0% | 9.1% | 12.5% | 0.80 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.90 |
| claude-opus-4-5 | 1/2 | 50.0% | 40.0% | 44.4% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 33.3% | 40.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 20.0% | 28.6% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| gemini-3-pro | 1/2 | 50.0% | 66.7% | 57.1% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 20.0% | 28.6% | 0.90 |
| deepseek-v3-2 | 0/2 | 0.0% | 20.0% | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 25.0% | 40.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
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

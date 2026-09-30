# TC Chameleon Medical - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:44:07 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 53.3% | 46.8% | 49.9% | 95.6% | 0.96 | 0.96 | 0.92 | 2.5 | 53.2% |
| 2 | gemini-3-pro | 51.1% | 53.9% | 52.5% | 97.8% | 0.97 | 0.97 | 0.95 | 1.7 | 46.1% |
| 3 | gpt-5.2 | 48.8% | 79.0% | 60.4% | 90.7% | 0.96 | 0.98 | 0.95 | 1.4 | 21.0% |
| 4 | llama-4-maverick | 32.6% | 16.5% | 21.9% | 100.0% | 0.81 | 0.73 | 0.71 | 2.6 | 83.5% |
| 5 | deepseek-v3-2 | 31.1% | 24.8% | 27.6% | 97.8% | 0.92 | 0.90 | 0.84 | 2.4 | 75.2% |
| 6 | grok-4-fast | 26.1% | 42.0% | 32.2% | 67.4% | 0.96 | 0.96 | 0.92 | 1.1 | 58.0% |
| 7 | qwen3-coder-plus | 22.7% | 13.2% | 16.7% | 100.0% | 0.89 | 0.87 | 0.86 | 2.1 | 86.8% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 24/45 | 46.7% | 26.7% | 42.2% | 52 | 59 | 1.31 |
| gemini-3-pro | 23/45 | 48.9% | 24.4% | 33.3% | 41 | 35 | 0.78 |
| gpt-5.2 | 21/43 | 51.2% | 16.3% | 41.9% | 49 | 13 | 0.30 |
| llama-4-maverick | 15/46 | 67.4% | 60.9% | 6.5% | 20 | 101 | 2.20 |
| deepseek-v3-2 | 14/45 | 68.9% | 53.3% | 15.6% | 27 | 82 | 1.82 |
| grok-4-fast | 12/46 | 73.9% | 30.4% | 17.4% | 21 | 29 | 0.63 |
| qwen3-coder-plus | 10/44 | 77.3% | 75.0% | 2.3% | 12 | 79 | 1.80 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 8/12 | 72.7% | 85.7% | 78.7% | 0.96 |
| claude-opus-4-5 | 8/12 | 66.7% | 70.4% | 68.5% | 0.96 |
| qwen3-coder-plus | 8/12 | 66.7% | 37.5% | 48.0% | 0.88 |
| gemini-3-pro | 7/12 | 58.3% | 69.2% | 63.3% | 0.97 |
| deepseek-v3-2 | 6/12 | 50.0% | 35.7% | 41.7% | 0.93 |
| llama-4-maverick | 6/12 | 50.0% | 20.0% | 28.6% | 0.85 |
| grok-4-fast | 4/12 | 33.3% | 44.4% | 38.1% | 0.95 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 52.9% | 59.0% | 0.95 |
| gemini-3-pro | 3/6 | 50.0% | 38.5% | 43.5% | 0.97 |
| gpt-5.2 | 2/6 | 33.3% | 76.9% | 46.5% | 1.00 |
| grok-4-fast | 1/6 | 16.7% | 44.4% | 24.2% | 1.00 |
| deepseek-v3-2 | 0/6 | 0.0% | 6.7% | N/A | N/A |
| llama-4-maverick | 0/6 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/6 | 0.0% | 10.0% | N/A | N/A |

### Reentrancy (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/6 | 57.1% | 31.6% | 40.7% | 0.90 |
| llama-4-maverick | 4/6 | 57.1% | 21.1% | 30.8% | 0.80 |
| claude-opus-4-5 | 2/6 | 33.3% | 36.4% | 34.8% | 1.00 |
| gemini-3-pro | 2/6 | 33.3% | 30.0% | 31.6% | 1.00 |
| gpt-5.2 | 1/6 | 16.7% | 20.0% | 18.2% | 1.00 |
| grok-4-fast | 1/6 | 14.3% | 20.0% | 16.7% | 0.95 |
| qwen3-coder-plus | 0/6 | 0.0% | N/A | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/5 | 80.0% | 57.1% | 66.7% | 0.97 |
| claude-opus-4-5 | 3/5 | 60.0% | 38.5% | 46.9% | 0.95 |
| deepseek-v3-2 | 3/5 | 60.0% | 30.0% | 40.0% | 0.92 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| grok-4-fast | 3/5 | 60.0% | 85.7% | 70.6% | 0.97 |
| llama-4-maverick | 3/5 | 60.0% | 36.4% | 45.3% | 0.83 |
| qwen3-coder-plus | 0/5 | 0.0% | N/A | N/A | N/A |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 20.0% | 28.6% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 16.7% | 25.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 25.0% | 33.3% | 0.60 |
| grok-4-fast | 0/2 | 0.0% | 20.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 40.0% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| claude-opus-4-5 | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| gpt-5.2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | N/A | N/A | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.40 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
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

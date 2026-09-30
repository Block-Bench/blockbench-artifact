# TC Trojan - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | deepseek-v3-2 | 71.7% | 72.0% | 71.9% | 97.8% | 0.97 | 0.92 | 0.98 | 2.0 | 28.0% |
| 2 | claude-opus-4-5 | 63.0% | 85.0% | 72.4% | 97.8% | 0.98 | 0.96 | 0.99 | 2.3 | 15.0% |
| 3 | llama-4-maverick | 60.9% | 52.0% | 56.1% | 100.0% | 0.95 | 0.86 | 0.95 | 2.1 | 48.0% |
| 4 | qwen3-coder-plus | 60.9% | 66.2% | 63.4% | 100.0% | 0.96 | 0.89 | 0.98 | 1.5 | 33.8% |
| 5 | gemini-3-pro | 50.0% | 95.7% | 65.7% | 82.6% | 1.00 | 0.99 | 1.00 | 1.5 | 4.3% |
| 6 | gpt-5.2 | 48.9% | 95.1% | 64.6% | 88.9% | 0.98 | 0.96 | 0.98 | 1.4 | 4.9% |
| 7 | grok-4-fast | 30.4% | 97.4% | 46.4% | 58.7% | 1.00 | 0.99 | 1.00 | 0.8 | 2.6% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| deepseek-v3-2 | 33/46 | 28.3% | 8.7% | 50.0% | 67 | 26 | 0.57 |
| claude-opus-4-5 | 29/46 | 37.0% | 0.0% | 84.8% | 91 | 16 | 0.35 |
| llama-4-maverick | 28/46 | 39.1% | 17.4% | 41.3% | 51 | 47 | 1.02 |
| qwen3-coder-plus | 28/46 | 39.1% | 17.4% | 32.6% | 47 | 24 | 0.52 |
| gemini-3-pro | 23/46 | 50.0% | 2.2% | 58.7% | 66 | 3 | 0.07 |
| gpt-5.2 | 22/45 | 51.1% | 4.4% | 60.0% | 58 | 3 | 0.07 |
| grok-4-fast | 14/46 | 69.6% | 0.0% | 32.6% | 37 | 1 | 0.02 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 10/12 | 83.3% | 95.7% | 89.1% | 0.99 |
| deepseek-v3-2 | 10/12 | 83.3% | 66.7% | 74.1% | 0.97 |
| llama-4-maverick | 9/12 | 75.0% | 56.0% | 64.1% | 0.96 |
| qwen3-coder-plus | 9/12 | 75.0% | 66.7% | 70.6% | 0.99 |
| gemini-3-pro | 6/12 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 6/12 | 50.0% | 78.6% | 61.1% | 0.97 |
| grok-4-fast | 3/12 | 25.0% | 83.3% | 38.5% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 6/7 | 85.7% | 77.8% | 81.6% | 0.93 |
| llama-4-maverick | 5/7 | 71.4% | 63.6% | 67.3% | 0.92 |
| deepseek-v3-2 | 4/7 | 57.1% | 60.0% | 58.5% | 0.97 |
| claude-opus-4-5 | 2/7 | 28.6% | 60.0% | 38.7% | 1.00 |
| gpt-5.2 | 2/7 | 28.6% | 100.0% | 44.4% | 1.00 |
| gemini-3-pro | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 94.1% | 78.0% | 0.95 |
| llama-4-maverick | 4/6 | 66.7% | 57.1% | 61.5% | 1.00 |
| gemini-3-pro | 3/6 | 50.0% | 83.3% | 62.5% | 1.00 |
| gpt-5.2 | 3/6 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 2/6 | 33.3% | 85.7% | 48.0% | 0.95 |
| qwen3-coder-plus | 1/6 | 16.7% | 66.7% | 26.7% | 1.00 |
| grok-4-fast | 0/6 | 0.0% | 100.0% | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 3/5 | 60.0% | 75.0% | 66.7% | 0.97 |
| gemini-3-pro | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| gpt-5.2 | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| grok-4-fast | 3/5 | 60.0% | 100.0% | 75.0% | 1.00 |
| llama-4-maverick | 3/5 | 60.0% | 50.0% | 54.5% | 0.97 |
| qwen3-coder-plus | 3/5 | 60.0% | 100.0% | 75.0% | 0.93 |
| claude-opus-4-5 | 2/5 | 40.0% | 76.9% | 52.6% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 20.0% | 28.6% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| qwen3-coder-plus | 0/2 | 0.0% | 25.0% | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.70 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 0.70 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.70 |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
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

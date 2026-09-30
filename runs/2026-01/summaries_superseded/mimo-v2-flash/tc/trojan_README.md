# TC Trojan - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | llama-4-maverick | 66.7% | 36.8% | 47.5% | 100.0% | 0.86 | 0.83 | 0.81 | 2.1 | 63.2% |
| 2 | deepseek-v3-2 | 65.9% | 45.1% | 53.5% | 97.7% | 0.95 | 0.93 | 0.91 | 2.1 | 54.9% |
| 3 | qwen3-coder-plus | 60.9% | 45.1% | 51.8% | 100.0% | 0.90 | 0.87 | 0.87 | 1.5 | 54.9% |
| 4 | claude-opus-4-5 | 55.6% | 43.3% | 48.6% | 97.8% | 0.95 | 0.95 | 0.92 | 2.3 | 56.7% |
| 5 | gemini-3-pro | 52.3% | 55.4% | 53.8% | 81.8% | 0.99 | 0.98 | 0.97 | 1.5 | 44.6% |
| 6 | gpt-5.2 | 51.1% | 73.8% | 60.4% | 88.9% | 0.97 | 0.98 | 0.94 | 1.4 | 26.2% |
| 7 | grok-4-fast | 28.3% | 50.0% | 36.1% | 58.7% | 0.98 | 0.99 | 0.97 | 0.8 | 50.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| llama-4-maverick | 30/45 | 33.3% | 33.3% | 8.9% | 35 | 60 | 1.33 |
| deepseek-v3-2 | 29/44 | 34.1% | 27.3% | 13.6% | 41 | 50 | 1.14 |
| qwen3-coder-plus | 28/46 | 39.1% | 39.1% | 2.2% | 32 | 39 | 0.85 |
| claude-opus-4-5 | 25/45 | 44.4% | 31.1% | 24.4% | 45 | 59 | 1.31 |
| gemini-3-pro | 23/44 | 47.7% | 18.2% | 22.7% | 36 | 29 | 0.66 |
| gpt-5.2 | 23/45 | 48.9% | 20.0% | 33.3% | 45 | 16 | 0.36 |
| grok-4-fast | 13/46 | 71.7% | 21.7% | 8.7% | 19 | 19 | 0.41 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 9/12 | 75.0% | 56.5% | 64.5% | 0.93 |
| llama-4-maverick | 9/12 | 75.0% | 52.0% | 61.4% | 0.92 |
| qwen3-coder-plus | 9/12 | 75.0% | 50.0% | 60.0% | 0.89 |
| deepseek-v3-2 | 8/12 | 66.7% | 41.7% | 51.3% | 0.98 |
| gpt-5.2 | 7/12 | 58.3% | 64.3% | 61.2% | 0.96 |
| gemini-3-pro | 5/12 | 45.5% | 55.6% | 50.0% | 1.00 |
| grok-4-fast | 3/12 | 25.0% | 50.0% | 33.3% | 1.00 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/7 | 80.0% | 50.0% | 61.5% | 0.90 |
| llama-4-maverick | 5/7 | 71.4% | 45.5% | 55.6% | 0.82 |
| qwen3-coder-plus | 5/7 | 71.4% | 66.7% | 69.0% | 0.92 |
| claude-opus-4-5 | 4/7 | 57.1% | 33.3% | 42.1% | 0.95 |
| gpt-5.2 | 3/7 | 42.9% | 62.5% | 50.8% | 0.97 |
| gemini-3-pro | 1/7 | 16.7% | 44.4% | 24.2% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 75.0% | 24.0% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/6 | 66.7% | 41.7% | 51.3% | 0.95 |
| llama-4-maverick | 3/6 | 50.0% | 21.4% | 30.0% | 0.90 |
| claude-opus-4-5 | 2/6 | 33.3% | 41.2% | 36.8% | 0.95 |
| gpt-5.2 | 2/6 | 33.3% | 63.6% | 43.7% | 0.95 |
| qwen3-coder-plus | 2/6 | 33.3% | 22.2% | 26.7% | 0.60 |
| deepseek-v3-2 | 1/6 | 16.7% | 21.4% | 18.8% | 0.90 |
| grok-4-fast | 0/6 | 0.0% | N/A | N/A | N/A |

### Arithmetic Error (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 4/4 | 80.0% | 40.0% | 53.3% | 0.85 |
| deepseek-v3-2 | 3/4 | 60.0% | 37.5% | 46.2% | 0.98 |
| gemini-3-pro | 3/4 | 60.0% | 66.7% | 63.2% | 1.00 |
| gpt-5.2 | 3/4 | 60.0% | 75.0% | 66.7% | 1.00 |
| grok-4-fast | 3/4 | 60.0% | 66.7% | 63.2% | 1.00 |
| qwen3-coder-plus | 3/4 | 60.0% | 42.9% | 50.0% | 0.93 |
| claude-opus-4-5 | 1/4 | 25.0% | 10.0% | 14.3% | 1.00 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 40.0% | 57.1% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.97 |
| grok-4-fast | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 20.0% | 28.6% | 0.90 |
| qwen3-coder-plus | 1/2 | 50.0% | 33.3% | 40.0% | 1.00 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 0.97 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.95 |
| gemini-3-pro | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 25.0% | 33.3% | 0.90 |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
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
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 66.7% | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.60 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.70 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
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
| llama-4-maverick | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.60 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
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

# TC Falseprophet - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | qwen3-coder-plus | 61.4% | 49.3% | 54.7% | 100.0% | 0.90 | 0.88 | 0.89 | 1.6 | 50.7% |
| 2 | claude-opus-4-5 | 59.1% | 42.3% | 49.3% | 100.0% | 0.97 | 0.98 | 0.95 | 2.4 | 57.7% |
| 3 | gpt-5.2 | 54.3% | 76.1% | 63.4% | 91.3% | 0.97 | 0.97 | 0.95 | 1.5 | 23.9% |
| 4 | deepseek-v3-2 | 52.3% | 34.0% | 41.2% | 100.0% | 0.95 | 0.95 | 0.92 | 2.1 | 66.0% |
| 5 | gemini-3-pro | 51.1% | 61.9% | 56.0% | 80.0% | 0.99 | 0.98 | 0.97 | 1.4 | 38.1% |
| 6 | llama-4-maverick | 47.7% | 25.6% | 33.3% | 100.0% | 0.81 | 0.76 | 0.76 | 2.0 | 74.4% |
| 7 | grok-4-fast | 35.6% | 54.5% | 43.0% | 71.1% | 0.91 | 0.93 | 0.92 | 1.0 | 45.5% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| qwen3-coder-plus | 27/44 | 38.6% | 29.5% | 11.4% | 34 | 35 | 0.80 |
| claude-opus-4-5 | 26/44 | 40.9% | 29.5% | 31.8% | 44 | 60 | 1.36 |
| gpt-5.2 | 25/46 | 45.7% | 8.7% | 41.3% | 54 | 17 | 0.37 |
| deepseek-v3-2 | 23/44 | 47.7% | 43.2% | 13.6% | 32 | 62 | 1.41 |
| gemini-3-pro | 23/45 | 48.9% | 13.3% | 26.7% | 39 | 24 | 0.53 |
| llama-4-maverick | 21/44 | 52.3% | 47.7% | 4.5% | 23 | 67 | 1.52 |
| grok-4-fast | 16/45 | 64.4% | 24.4% | 13.3% | 24 | 20 | 0.44 |

---

## Performance by Vulnerability Type

### Access Control (11 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 8/11 | 66.7% | 40.0% | 50.0% | 0.75 |
| claude-opus-4-5 | 7/11 | 63.6% | 63.6% | 63.6% | 0.97 |
| qwen3-coder-plus | 6/11 | 60.0% | 63.6% | 61.8% | 0.83 |
| deepseek-v3-2 | 7/11 | 58.3% | 47.6% | 52.4% | 0.97 |
| gpt-5.2 | 7/11 | 58.3% | 80.0% | 67.5% | 0.97 |
| gemini-3-pro | 6/11 | 50.0% | 73.3% | 59.5% | 1.00 |
| grok-4-fast | 4/11 | 36.4% | 57.1% | 44.4% | 0.90 |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| qwen3-coder-plus | 6/7 | 85.7% | 54.5% | 66.7% | 0.95 |
| claude-opus-4-5 | 5/7 | 71.4% | 46.2% | 56.1% | 0.98 |
| deepseek-v3-2 | 4/7 | 66.7% | 41.7% | 51.3% | 0.97 |
| llama-4-maverick | 4/7 | 66.7% | 40.0% | 50.0% | 0.80 |
| gemini-3-pro | 3/7 | 42.9% | 45.5% | 44.1% | 0.97 |
| gpt-5.2 | 2/7 | 28.6% | 70.0% | 40.6% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 50.0% | 22.2% | 1.00 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 3/6 | 50.0% | 58.3% | 53.8% | 1.00 |
| gpt-5.2 | 3/6 | 50.0% | 63.6% | 56.0% | 0.97 |
| llama-4-maverick | 3/6 | 50.0% | 23.1% | 31.6% | 0.97 |
| qwen3-coder-plus | 3/6 | 50.0% | 50.0% | 50.0% | 0.92 |
| claude-opus-4-5 | 2/6 | 33.3% | 31.2% | 32.3% | 0.95 |
| deepseek-v3-2 | 2/6 | 33.3% | 13.3% | 19.0% | 0.75 |
| grok-4-fast | 2/6 | 33.3% | 40.0% | 36.4% | 0.68 |

### Arithmetic Error (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 5/4 | 100.0% | 45.5% | 62.5% | 0.95 |
| qwen3-coder-plus | 5/4 | 100.0% | 45.5% | 62.5% | 0.82 |
| grok-4-fast | 4/4 | 80.0% | 57.1% | 66.7% | 0.90 |
| gpt-5.2 | 3/4 | 60.0% | 87.5% | 71.2% | 0.98 |
| claude-opus-4-5 | 2/4 | 50.0% | 36.4% | 42.1% | 1.00 |
| gemini-3-pro | 2/4 | 40.0% | 60.0% | 48.0% | 0.95 |
| llama-4-maverick | 2/4 | 40.0% | 18.2% | 25.0% | 0.90 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 33.3% | 50.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 66.7% | 80.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 50.0% | 66.7% | 0.95 |
| qwen3-coder-plus | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 75.0% | 60.0% | 1.00 |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.97 |
| claude-opus-4-5 | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 75.0% | 60.0% | 0.90 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 50.0% | 50.0% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.30 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 0.95 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.85 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
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
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.95 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
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
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 33.3% | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 33.3% | 50.0% | 0.95 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
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

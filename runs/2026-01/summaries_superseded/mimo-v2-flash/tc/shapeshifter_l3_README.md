# TC Shapeshifter L3 - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 56.8% | 50.5% | 53.5% | 100.0% | 0.93 | 0.94 | 0.91 | 2.4 | 49.5% |
| 2 | deepseek-v3-2 | 48.9% | 32.3% | 38.9% | 97.8% | 0.87 | 0.87 | 0.84 | 2.2 | 67.7% |
| 3 | gemini-3-pro | 46.7% | 53.6% | 49.9% | 77.8% | 0.99 | 0.98 | 0.97 | 1.2 | 46.4% |
| 4 | gpt-5.2 | 46.7% | 73.4% | 57.1% | 91.1% | 0.95 | 0.97 | 0.96 | 1.4 | 26.6% |
| 5 | llama-4-maverick | 41.3% | 21.0% | 27.8% | 100.0% | 0.80 | 0.73 | 0.70 | 2.3 | 79.0% |
| 6 | qwen3-coder-plus | 39.5% | 28.8% | 33.3% | 97.7% | 0.87 | 0.84 | 0.84 | 1.5 | 71.2% |
| 7 | grok-4-fast | 34.1% | 61.5% | 43.9% | 70.5% | 0.94 | 0.97 | 0.92 | 0.9 | 38.5% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 25/44 | 43.2% | 25.0% | 47.7% | 54 | 53 | 1.20 |
| deepseek-v3-2 | 22/45 | 51.1% | 44.4% | 15.6% | 32 | 67 | 1.49 |
| gemini-3-pro | 21/45 | 53.3% | 17.8% | 17.8% | 30 | 26 | 0.58 |
| gpt-5.2 | 21/45 | 53.3% | 20.0% | 42.2% | 47 | 17 | 0.38 |
| llama-4-maverick | 19/46 | 58.7% | 54.3% | 4.3% | 22 | 83 | 1.80 |
| qwen3-coder-plus | 17/43 | 60.5% | 55.8% | 4.7% | 19 | 47 | 1.09 |
| grok-4-fast | 15/44 | 65.9% | 20.5% | 18.2% | 24 | 15 | 0.34 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 8/12 | 66.7% | 66.7% | 66.7% | 0.88 |
| llama-4-maverick | 8/12 | 66.7% | 33.3% | 44.4% | 0.79 |
| gemini-3-pro | 7/12 | 58.3% | 70.0% | 63.6% | 0.99 |
| deepseek-v3-2 | 6/12 | 50.0% | 43.5% | 46.5% | 0.96 |
| gpt-5.2 | 6/12 | 50.0% | 64.3% | 56.3% | 0.87 |
| qwen3-coder-plus | 6/12 | 50.0% | 37.5% | 42.9% | 0.87 |
| grok-4-fast | 5/12 | 41.7% | 88.9% | 56.7% | 0.92 |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/6 | 66.7% | 41.2% | 50.9% | 0.96 |
| qwen3-coder-plus | 3/6 | 60.0% | 44.4% | 51.1% | 0.90 |
| gemini-3-pro | 3/6 | 50.0% | 37.5% | 42.9% | 0.97 |
| gpt-5.2 | 3/6 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/6 | 16.7% | 11.8% | 13.8% | 0.90 |
| llama-4-maverick | 1/6 | 16.7% | 6.7% | 9.5% | 0.90 |
| grok-4-fast | 0/6 | 0.0% | 25.0% | N/A | N/A |

### Reentrancy (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/6 | 83.3% | 50.0% | 62.5% | 0.92 |
| llama-4-maverick | 5/6 | 71.4% | 41.7% | 52.6% | 0.80 |
| qwen3-coder-plus | 4/6 | 66.7% | 44.4% | 53.3% | 0.78 |
| deepseek-v3-2 | 3/6 | 50.0% | 28.6% | 36.4% | 0.93 |
| grok-4-fast | 2/6 | 33.3% | 37.5% | 35.3% | 0.95 |
| gemini-3-pro | 2/6 | 28.6% | 36.4% | 32.0% | 1.00 |
| gpt-5.2 | 2/6 | 28.6% | 62.5% | 39.2% | 0.97 |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 3/5 | 60.0% | 36.4% | 45.3% | 0.97 |
| gemini-3-pro | 3/5 | 60.0% | 50.0% | 54.5% | 1.00 |
| claude-opus-4-5 | 2/5 | 40.0% | 38.5% | 39.2% | 0.97 |
| gpt-5.2 | 2/5 | 40.0% | 71.4% | 51.3% | 1.00 |
| grok-4-fast | 2/5 | 40.0% | 40.0% | 40.0% | 0.95 |
| llama-4-maverick | 2/5 | 40.0% | 18.2% | 25.0% | 0.60 |
| qwen3-coder-plus | 1/5 | 20.0% | 9.1% | 12.5% | 0.90 |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 1/2 | 50.0% | 25.0% | 33.3% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 25.0% | 33.3% | 0.30 |
| gpt-5.2 | 1/2 | 50.0% | 33.3% | 40.0% | 1.00 |
| gemini-3-pro | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.90 |
| gpt-5.2 | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| claude-opus-4-5 | 1/2 | 50.0% | 75.0% | 60.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 25.0% | 40.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.60 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.95 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.95 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.60 |
| gpt-5.2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.85 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
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

# TC Differential - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | N/A | 64.6% | N/A | 2.2% | N/A | N/A | N/A | 2.5 | 35.4% |
| 2 | deepseek-v3-2 | N/A | 55.6% | N/A | 6.5% | N/A | N/A | N/A | 2.2 | 44.4% |
| 3 | gemini-3-pro | N/A | 72.7% | N/A | 26.7% | N/A | N/A | N/A | 1.2 | 27.3% |
| 4 | gpt-5.2 | N/A | 88.9% | N/A | 22.2% | N/A | N/A | N/A | 1.4 | 11.1% |
| 5 | grok-4-fast | N/A | 80.6% | N/A | 50.0% | N/A | N/A | N/A | 0.8 | 19.4% |
| 6 | llama-4-maverick | N/A | 20.0% | N/A | N/A | N/A | N/A | N/A | 2.2 | 80.0% |
| 7 | qwen3-coder-plus | N/A | 35.1% | N/A | N/A | N/A | N/A | N/A | 1.7 | 64.9% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 0/46 | 100.0% | 2.2% | 78.3% | 73 | 40 | 0.87 |
| deepseek-v3-2 | 0/46 | 100.0% | 6.5% | 69.6% | 55 | 44 | 0.96 |
| gemini-3-pro | 0/45 | 100.0% | 26.7% | 55.6% | 40 | 15 | 0.33 |
| gpt-5.2 | 0/45 | 100.0% | 22.2% | 71.1% | 56 | 7 | 0.16 |
| grok-4-fast | 0/46 | 100.0% | 50.0% | 41.3% | 29 | 7 | 0.15 |
| llama-4-maverick | 0/46 | 100.0% | 0.0% | 32.6% | 20 | 80 | 1.74 |
| qwen3-coder-plus | 0/45 | 100.0% | 0.0% | 40.0% | 27 | 50 | 1.11 |

---

## Performance by Vulnerability Type

### Access Control (12 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/12 | 0.0% | 67.9% | N/A | N/A |
| deepseek-v3-2 | 0/12 | 0.0% | 65.0% | N/A | N/A |
| gemini-3-pro | 0/12 | 0.0% | 45.5% | N/A | N/A |
| gpt-5.2 | 0/12 | 0.0% | 83.3% | N/A | N/A |
| grok-4-fast | 0/12 | 0.0% | 60.0% | N/A | N/A |
| llama-4-maverick | 0/12 | 0.0% | 22.2% | N/A | N/A |
| qwen3-coder-plus | 0/12 | 0.0% | 40.0% | N/A | N/A |

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/7 | 0.0% | 64.3% | N/A | N/A |
| deepseek-v3-2 | 0/7 | 0.0% | 44.4% | N/A | N/A |
| gemini-3-pro | 0/7 | 0.0% | 80.0% | N/A | N/A |
| gpt-5.2 | 0/7 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/7 | 0.0% | 75.0% | N/A | N/A |
| llama-4-maverick | 0/7 | 0.0% | 20.0% | N/A | N/A |
| qwen3-coder-plus | 0/7 | 0.0% | 41.7% | N/A | N/A |

### Price Oracle Manipulation (6 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/6 | 0.0% | 78.9% | N/A | N/A |
| deepseek-v3-2 | 0/6 | 0.0% | 72.2% | N/A | N/A |
| gemini-3-pro | 0/6 | 0.0% | 63.6% | N/A | N/A |
| gpt-5.2 | 0/6 | 0.0% | 84.6% | N/A | N/A |
| grok-4-fast | 0/6 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/6 | 0.0% | 20.0% | N/A | N/A |
| qwen3-coder-plus | 0/6 | 0.0% | 41.7% | N/A | N/A |

### Arithmetic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/5 | 0.0% | 33.3% | N/A | N/A |
| deepseek-v3-2 | 0/5 | 0.0% | 58.3% | N/A | N/A |
| gemini-3-pro | 0/5 | 0.0% | 75.0% | N/A | N/A |
| gpt-5.2 | 0/5 | 0.0% | 80.0% | N/A | N/A |
| grok-4-fast | 0/5 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/5 | 0.0% | 22.2% | N/A | N/A |
| qwen3-coder-plus | 0/5 | 0.0% | 33.3% | N/A | N/A |

### Logic Error (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/2 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/2 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/2 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/2 | 0.0% | 75.0% | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 20.0% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 33.3% | N/A | N/A |

### Oracle Manipulation (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/2 | 0.0% | 75.0% | N/A | N/A |
| deepseek-v3-2 | 0/2 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/2 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/2 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | N/A | N/A | N/A |

### Improper Initialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Governance Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Pool Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Validation Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Reinitialization (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 50.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Accounting Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Signature Verification (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Input Validation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Accounting Error (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Bridge Security (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 50.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Arithmetic Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Price Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
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

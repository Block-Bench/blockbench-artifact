# DS Tier3 - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 83.3% | 83.1% | 83.2% | 96.7% | 0.99 | 0.98 | 0.97 | 2.4 | 16.9% |
| 2 | gemini-3-pro | 63.3% | 95.0% | 76.0% | 96.7% | 1.00 | 1.00 | 0.95 | 1.3 | 5.0% |
| 3 | deepseek-v3-2 | 46.7% | 67.2% | 55.1% | 93.3% | 0.99 | 0.97 | 0.96 | 1.9 | 32.8% |
| 4 | qwen3-coder-plus | 43.3% | 59.6% | 50.2% | 96.7% | 0.98 | 0.95 | 0.89 | 1.6 | 40.4% |
| 5 | llama-4-maverick | 42.9% | 33.3% | 37.5% | 100.0% | 0.97 | 0.95 | 0.86 | 2.1 | 66.7% |
| 6 | gpt-5.2 | 41.4% | 100.0% | 58.5% | 82.8% | 1.00 | 1.00 | 0.92 | 1.2 | 0.0% |
| 7 | grok-4-fast | 33.3% | 95.7% | 49.4% | 66.7% | 0.99 | 0.99 | 0.89 | 0.8 | 4.3% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 25/30 | 16.7% | 0.0% | 63.3% | 59 | 12 | 0.40 |
| gemini-3-pro | 19/30 | 36.7% | 3.3% | 53.3% | 38 | 2 | 0.07 |
| deepseek-v3-2 | 14/30 | 53.3% | 13.3% | 46.7% | 39 | 19 | 0.63 |
| qwen3-coder-plus | 13/30 | 56.7% | 20.0% | 36.7% | 28 | 19 | 0.63 |
| llama-4-maverick | 12/28 | 57.1% | 42.9% | 28.6% | 20 | 40 | 1.43 |
| gpt-5.2 | 12/29 | 58.6% | 0.0% | 55.2% | 34 | 0 | 0.00 |
| grok-4-fast | 10/30 | 66.7% | 3.3% | 36.7% | 22 | 1 | 0.03 |

---

## Performance by Vulnerability Type

### Logic Error (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 6/7 | 85.7% | 91.7% | 88.6% | 0.98 |
| gemini-3-pro | 5/7 | 71.4% | 100.0% | 83.3% | 1.00 |
| deepseek-v3-2 | 4/7 | 57.1% | 50.0% | 53.3% | 1.00 |
| gpt-5.2 | 4/7 | 57.1% | 100.0% | 72.7% | 1.00 |
| qwen3-coder-plus | 4/7 | 57.1% | 71.4% | 63.5% | 0.93 |
| grok-4-fast | 3/7 | 42.9% | 100.0% | 60.0% | 0.97 |
| llama-4-maverick | 3/7 | 42.9% | 44.4% | 43.6% | 1.00 |

### Honeypot (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 81.8% | 90.0% | 0.96 |
| gemini-3-pro | 4/5 | 80.0% | 71.4% | 75.5% | 1.00 |
| gpt-5.2 | 2/5 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 2/5 | 40.0% | 40.0% | 40.0% | 1.00 |
| llama-4-maverick | 1/5 | 20.0% | 18.8% | 19.4% | 0.80 |
| qwen3-coder-plus | 1/5 | 20.0% | 12.5% | 15.4% | 1.00 |
| grok-4-fast | 0/5 | 0.0% | 75.0% | N/A | N/A |

### Unchecked Return (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 94.4% | 97.1% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 25.0% | 30.8% | 1.00 |
| grok-4-fast | 1/5 | 20.0% | 100.0% | 33.3% | 1.00 |
| qwen3-coder-plus | 1/5 | 20.0% | 58.3% | 29.8% | 1.00 |
| deepseek-v3-2 | 0/5 | 0.0% | 85.7% | N/A | N/A |
| gemini-3-pro | 0/5 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/5 | 0.0% | 100.0% | N/A | N/A |

### Unchecked Call (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 60.0% | 75.0% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 0.95 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 2/2 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Reentrancy (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 1/2 | 50.0% | 83.3% | 62.5% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |

### Access Control (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 60.0% | 75.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 83.3% | 62.5% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 75.0% | N/A | N/A |

### Token Incompatibility (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Approval Scam (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Precision Loss (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Unprotected Callback (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Delegatecall Injection (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Front Running (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 33.3% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

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

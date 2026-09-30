# DS Tier3 - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 80.0% | 93.0% | 86.0% | 96.7% | 0.92 | 0.88 | 0.88 | 2.4 | 7.0% |
| 2 | gemini-3-pro | 70.0% | 90.0% | 78.8% | 96.7% | 0.92 | 0.90 | 0.87 | 1.3 | 10.0% |
| 3 | llama-4-maverick | 41.4% | 65.6% | 50.8% | 100.0% | 0.82 | 0.78 | 0.79 | 2.2 | 34.4% |
| 4 | deepseek-v3-2 | 40.0% | 91.4% | 55.6% | 93.3% | 0.88 | 0.87 | 0.85 | 1.9 | 8.6% |
| 5 | qwen3-coder-plus | 40.0% | 100.0% | 57.1% | 96.7% | 0.85 | 0.85 | 0.82 | 1.6 | 0.0% |
| 6 | gpt-5.2 | 36.7% | 97.1% | 53.2% | 83.3% | 0.92 | 0.90 | 0.88 | 1.2 | 2.9% |
| 7 | grok-4-fast | 33.3% | 95.7% | 49.4% | 66.7% | 0.91 | 0.86 | 0.92 | 0.8 | 4.3% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 24/30 | 20.0% | 10.0% | 36.7% | 66 | 5 | 0.17 |
| gemini-3-pro | 21/30 | 30.0% | 16.7% | 26.7% | 36 | 4 | 0.13 |
| llama-4-maverick | 12/29 | 58.6% | 37.9% | 31.0% | 42 | 22 | 0.76 |
| deepseek-v3-2 | 12/30 | 60.0% | 30.0% | 26.7% | 53 | 5 | 0.17 |
| qwen3-coder-plus | 12/30 | 60.0% | 33.3% | 30.0% | 47 | 0 | 0.00 |
| gpt-5.2 | 11/30 | 63.3% | 16.7% | 43.3% | 34 | 1 | 0.03 |
| grok-4-fast | 10/30 | 66.7% | 20.0% | 16.7% | 22 | 1 | 0.03 |

---

## Performance by Vulnerability Type

### Logic Error (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 6/7 | 85.7% | 91.7% | 88.6% | 0.90 |
| gemini-3-pro | 6/7 | 85.7% | 88.9% | 87.3% | 0.90 |
| llama-4-maverick | 5/7 | 71.4% | 88.9% | 79.2% | 0.80 |
| qwen3-coder-plus | 4/7 | 57.1% | 100.0% | 72.7% | 0.88 |
| deepseek-v3-2 | 3/7 | 42.9% | 90.0% | 58.1% | 0.87 |
| gpt-5.2 | 3/7 | 42.9% | 100.0% | 60.0% | 0.90 |
| grok-4-fast | 3/7 | 42.9% | 100.0% | 60.0% | 0.93 |

### Honeypot (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/5 | 80.0% | 90.9% | 85.1% | 0.90 |
| gemini-3-pro | 4/5 | 80.0% | 85.7% | 82.8% | 0.93 |
| deepseek-v3-2 | 2/5 | 40.0% | 100.0% | 57.1% | 0.80 |
| gpt-5.2 | 2/5 | 40.0% | 100.0% | 57.1% | 0.95 |
| llama-4-maverick | 2/5 | 40.0% | 50.0% | 44.4% | 0.80 |
| qwen3-coder-plus | 1/5 | 20.0% | 100.0% | 33.3% | 0.80 |
| grok-4-fast | 0/5 | 0.0% | 100.0% | N/A | N/A |

### Unchecked Return (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 100.0% | 100.0% | 0.96 |
| llama-4-maverick | 2/5 | 40.0% | 31.2% | 35.1% | 0.85 |
| deepseek-v3-2 | 1/5 | 20.0% | 100.0% | 33.3% | 0.90 |
| gemini-3-pro | 1/5 | 20.0% | 100.0% | 33.3% | 0.90 |
| grok-4-fast | 1/5 | 20.0% | 100.0% | 33.3% | 0.90 |
| qwen3-coder-plus | 1/5 | 20.0% | 100.0% | 33.3% | 0.80 |
| gpt-5.2 | 0/5 | 0.0% | 100.0% | N/A | N/A |

### Unchecked Call (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 60.0% | 75.0% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 50.0% | 66.7% | 0.90 |
| qwen3-coder-plus | 2/2 | 100.0% | 100.0% | 100.0% | 0.85 |
| gemini-3-pro | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 100.0% | 66.7% | 0.80 |
| gpt-5.2 | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Reentrancy (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Access Control (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Token Incompatibility (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Approval Scam (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

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
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Delegatecall Injection (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |

### Front Running (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |

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

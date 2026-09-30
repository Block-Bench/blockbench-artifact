# DS Tier3 - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 83.3% | 81.7% | 82.5% | 96.7% | 0.99 | 0.98 | 0.99 | 2.4 | 18.3% |
| 2 | gemini-3-pro | 66.7% | 95.0% | 78.4% | 96.7% | 1.00 | 1.00 | 1.00 | 1.3 | 5.0% |
| 3 | deepseek-v3-2 | 63.3% | 58.6% | 60.9% | 93.3% | 0.90 | 0.88 | 0.93 | 1.9 | 41.4% |
| 4 | qwen3-coder-plus | 53.3% | 48.9% | 51.0% | 93.3% | 0.95 | 0.91 | 0.93 | 1.6 | 51.1% |
| 5 | llama-4-maverick | 46.7% | 29.2% | 35.9% | 100.0% | 0.94 | 0.83 | 0.96 | 2.2 | 70.8% |
| 6 | gpt-5.2 | 40.0% | 91.4% | 55.7% | 83.3% | 1.00 | 1.00 | 1.00 | 1.2 | 8.6% |
| 7 | grok-4-fast | 33.3% | 82.6% | 47.5% | 66.7% | 1.00 | 0.97 | 0.98 | 0.8 | 17.4% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 25/30 | 16.7% | 0.0% | 60.0% | 58 | 13 | 0.43 |
| gemini-3-pro | 20/30 | 33.3% | 3.3% | 50.0% | 38 | 2 | 0.07 |
| deepseek-v3-2 | 19/30 | 36.7% | 13.3% | 30.0% | 34 | 24 | 0.80 |
| qwen3-coder-plus | 16/30 | 46.7% | 23.3% | 23.3% | 23 | 24 | 0.80 |
| llama-4-maverick | 14/30 | 53.3% | 46.7% | 6.7% | 19 | 46 | 1.53 |
| gpt-5.2 | 12/30 | 60.0% | 3.3% | 50.0% | 32 | 3 | 0.10 |
| grok-4-fast | 10/30 | 66.7% | 10.0% | 26.7% | 19 | 4 | 0.13 |

---

## Performance by Vulnerability Type

### Logic Error (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 6/7 | 85.7% | 91.7% | 88.6% | 0.97 |
| gemini-3-pro | 6/7 | 85.7% | 100.0% | 92.3% | 1.00 |
| qwen3-coder-plus | 6/7 | 85.7% | 85.7% | 85.7% | 0.95 |
| deepseek-v3-2 | 5/7 | 71.4% | 60.0% | 65.2% | 0.98 |
| llama-4-maverick | 5/7 | 71.4% | 66.7% | 69.0% | 0.96 |
| gpt-5.2 | 4/7 | 57.1% | 100.0% | 72.7% | 1.00 |
| grok-4-fast | 3/7 | 42.9% | 100.0% | 60.0% | 1.00 |

### Honeypot (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 81.8% | 90.0% | 0.98 |
| deepseek-v3-2 | 4/5 | 80.0% | 40.0% | 53.3% | 0.72 |
| gemini-3-pro | 4/5 | 80.0% | 71.4% | 75.5% | 1.00 |
| gpt-5.2 | 2/5 | 40.0% | 66.7% | 50.0% | 1.00 |
| llama-4-maverick | 1/5 | 20.0% | 6.2% | 9.5% | 0.50 |
| qwen3-coder-plus | 1/5 | 20.0% | 12.5% | 15.4% | 1.00 |
| grok-4-fast | 0/5 | 0.0% | 25.0% | N/A | N/A |

### Unchecked Return (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 5/5 | 100.0% | 83.3% | 90.9% | 1.00 |
| deepseek-v3-2 | 2/5 | 40.0% | 78.6% | 53.0% | 0.65 |
| llama-4-maverick | 2/5 | 40.0% | 12.5% | 19.0% | 1.00 |
| qwen3-coder-plus | 2/5 | 40.0% | 50.0% | 44.4% | 0.75 |
| grok-4-fast | 1/5 | 20.0% | 83.3% | 32.3% | 1.00 |
| gemini-3-pro | 0/5 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/5 | 0.0% | 87.5% | N/A | N/A |

### Unchecked Call (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| qwen3-coder-plus | 2/2 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Reentrancy (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 1/2 | 50.0% | 83.3% | 62.5% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 75.0% | 60.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 33.3% | 40.0% | 1.00 |

### Access Control (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/2 | 50.0% | 16.7% | 25.0% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 25.0% | N/A | N/A |

### Token Incompatibility (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Approval Scam (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
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
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
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
| llama-4-maverick | 0/1 | 0.0% | 66.7% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 50.0% | N/A | N/A |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
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

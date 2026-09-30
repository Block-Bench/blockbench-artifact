# DS Tier4 - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 92.3% | 92.9% | 92.6% | 100.0% | 0.93 | 0.88 | 0.89 | 2.2 | 7.1% |
| 2 | gemini-3-pro | 92.3% | 100.0% | 96.0% | 92.3% | 0.97 | 0.97 | 0.94 | 1.3 | 0.0% |
| 3 | gpt-5.2 | 92.3% | 94.4% | 93.4% | 100.0% | 0.95 | 0.93 | 0.92 | 1.4 | 5.6% |
| 4 | deepseek-v3-2 | 76.9% | 100.0% | 87.0% | 84.6% | 0.91 | 0.85 | 0.87 | 1.6 | 0.0% |
| 5 | llama-4-maverick | 69.2% | 81.0% | 74.6% | 100.0% | 0.93 | 0.91 | 0.92 | 1.6 | 19.0% |
| 6 | qwen3-coder-plus | 61.5% | 89.5% | 72.9% | 92.3% | 0.91 | 0.86 | 0.89 | 1.5 | 10.5% |
| 7 | grok-4-fast | 30.8% | 71.4% | 43.0% | 38.5% | 0.97 | 0.95 | 0.93 | 0.5 | 28.6% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 12/13 | 7.7% | 7.7% | 53.8% | 26 | 2 | 0.15 |
| gemini-3-pro | 12/13 | 7.7% | 0.0% | 15.4% | 17 | 0 | 0.00 |
| gpt-5.2 | 12/13 | 7.7% | 7.7% | 23.1% | 17 | 1 | 0.08 |
| deepseek-v3-2 | 10/13 | 23.1% | 7.7% | 23.1% | 21 | 0 | 0.00 |
| llama-4-maverick | 9/13 | 30.8% | 23.1% | 30.8% | 17 | 4 | 0.31 |
| qwen3-coder-plus | 8/13 | 38.5% | 23.1% | 30.8% | 17 | 2 | 0.15 |
| grok-4-fast | 4/13 | 69.2% | 7.7% | 7.7% | 5 | 2 | 0.15 |

---

## Performance by Vulnerability Type

### Reentrancy (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.85 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| qwen3-coder-plus | 1/2 | 50.0% | 33.3% | 40.0% | 0.90 |
| grok-4-fast | 0/2 | 0.0% | N/A | N/A | N/A |

### Signature Replay (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 83.3% | 90.9% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gpt-5.2 | 2/2 | 100.0% | 80.0% | 88.9% | 0.95 |
| llama-4-maverick | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| grok-4-fast | 1/2 | 50.0% | 50.0% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |

### Storage Collision (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 100.0% | 66.7% | 0.80 |
| deepseek-v3-2 | 0/2 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 100.0% | N/A | N/A |

### Integer Issues (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| qwen3-coder-plus | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |

### Weak Randomness (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 0.95 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| grok-4-fast | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| llama-4-maverick | 1/2 | 50.0% | 66.7% | 57.1% | 1.00 |
| qwen3-coder-plus | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |

### Oracle Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Inflation Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Flash Loan Attack (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |

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

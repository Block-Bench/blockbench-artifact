# DS Tier2 - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 83.8% | 93.9% | 88.6% | 91.9% | 0.94 | 0.91 | 0.92 | 1.8 | 6.1% |
| 2 | gemini-3-pro | 83.8% | 97.9% | 90.3% | 97.3% | 0.96 | 0.97 | 0.95 | 1.3 | 2.1% |
| 3 | deepseek-v3-2 | 73.0% | 94.8% | 82.5% | 94.6% | 0.93 | 0.91 | 0.90 | 1.6 | 5.2% |
| 4 | gpt-5.2 | 73.0% | 95.2% | 82.6% | 86.5% | 0.95 | 0.94 | 0.93 | 1.1 | 4.8% |
| 5 | qwen3-coder-plus | 56.8% | 89.8% | 69.6% | 89.2% | 0.92 | 0.91 | 0.89 | 1.3 | 10.2% |
| 6 | llama-4-maverick | 54.1% | 62.8% | 58.1% | 97.3% | 0.90 | 0.90 | 0.85 | 2.1 | 37.2% |
| 7 | grok-4-fast | 38.9% | 95.7% | 55.3% | 52.8% | 0.97 | 0.96 | 0.94 | 0.6 | 4.3% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 31/37 | 16.2% | 5.4% | 32.4% | 62 | 4 | 0.11 |
| gemini-3-pro | 31/37 | 16.2% | 13.5% | 18.9% | 46 | 1 | 0.03 |
| deepseek-v3-2 | 27/37 | 27.0% | 8.1% | 21.6% | 55 | 3 | 0.08 |
| gpt-5.2 | 27/37 | 27.0% | 8.1% | 16.2% | 40 | 2 | 0.05 |
| qwen3-coder-plus | 21/37 | 43.2% | 18.9% | 18.9% | 44 | 5 | 0.14 |
| llama-4-maverick | 20/37 | 45.9% | 37.8% | 21.6% | 49 | 29 | 0.78 |
| grok-4-fast | 14/36 | 61.1% | 13.9% | 2.8% | 22 | 1 | 0.03 |

---

## Performance by Vulnerability Type

### Logic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/5 | 60.0% | 100.0% | 75.0% | 0.90 |
| deepseek-v3-2 | 3/5 | 60.0% | 100.0% | 75.0% | 0.90 |
| gpt-5.2 | 3/5 | 60.0% | 80.0% | 68.6% | 0.90 |
| llama-4-maverick | 2/5 | 40.0% | 75.0% | 52.2% | 0.90 |
| gemini-3-pro | 1/5 | 20.0% | 80.0% | 32.0% | 0.80 |
| grok-4-fast | 1/5 | 20.0% | 100.0% | 33.3% | 0.90 |
| qwen3-coder-plus | 1/5 | 20.0% | 60.0% | 30.0% | 0.80 |

### Dos (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 0.97 |
| gpt-5.2 | 4/4 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 4/4 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 3/4 | 75.0% | 100.0% | 85.7% | 0.90 |
| deepseek-v3-2 | 3/4 | 75.0% | 100.0% | 85.7% | 0.93 |
| llama-4-maverick | 3/4 | 75.0% | 80.0% | 77.4% | 0.90 |
| grok-4-fast | 1/4 | 33.3% | 100.0% | 50.0% | 1.00 |

### Access Control (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/4 | 100.0% | 100.0% | 100.0% | 0.95 |
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 3/4 | 75.0% | 100.0% | 85.7% | 0.97 |
| llama-4-maverick | 2/4 | 50.0% | 50.0% | 50.0% | 0.95 |
| qwen3-coder-plus | 2/4 | 50.0% | 100.0% | 66.7% | 0.95 |

### Integer Issues (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 3/4 | 75.0% | 100.0% | 85.7% | 1.00 |
| qwen3-coder-plus | 3/4 | 75.0% | 100.0% | 85.7% | 1.00 |
| grok-4-fast | 2/4 | 50.0% | 100.0% | 66.7% | 1.00 |

### Weak Randomness (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 0.93 |
| gpt-5.2 | 3/3 | 100.0% | 100.0% | 100.0% | 0.93 |
| grok-4-fast | 3/3 | 100.0% | 100.0% | 100.0% | 0.97 |
| llama-4-maverick | 3/3 | 100.0% | 75.0% | 85.7% | 0.87 |
| qwen3-coder-plus | 3/3 | 100.0% | 100.0% | 100.0% | 0.93 |

### Unchecked Return (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 88.9% | 94.1% | 0.87 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 2/3 | 66.7% | 100.0% | 80.0% | 0.95 |
| deepseek-v3-2 | 1/3 | 33.3% | 100.0% | 50.0% | 0.90 |
| qwen3-coder-plus | 1/3 | 33.3% | 83.3% | 47.6% | 0.80 |
| grok-4-fast | 0/3 | 0.0% | 80.0% | N/A | N/A |
| llama-4-maverick | 0/3 | 0.0% | 37.5% | N/A | N/A |

### Front Running (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 0/2 | 0.0% | 80.0% | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 66.7% | N/A | N/A |

### Timestamp Dependency (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 0.90 |
| deepseek-v3-2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.85 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 0.90 |
| llama-4-maverick | 2/2 | 100.0% | 71.4% | 83.3% | 0.85 |
| qwen3-coder-plus | 1/2 | 50.0% | 75.0% | 60.0% | 0.80 |

### Selfdestruct (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Storage Misuse (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Data Exposure (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Tx Origin Auth (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Oracle Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Contract Check Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Reentrancy (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| claude-opus-4-5 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | 100.0% | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Variable Shadowing (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |

### Forced Ether (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 75.0% | 85.7% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Short Address (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

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

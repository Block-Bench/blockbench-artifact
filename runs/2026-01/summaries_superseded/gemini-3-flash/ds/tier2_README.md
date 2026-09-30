# DS Tier2 - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 83.8% | 81.8% | 82.8% | 91.9% | 1.00 | 1.00 | 1.00 | 1.8 | 18.2% |
| 2 | gemini-3-pro | 83.8% | 100.0% | 91.2% | 97.3% | 0.98 | 0.98 | 1.00 | 1.3 | 0.0% |
| 3 | deepseek-v3-2 | 75.7% | 72.4% | 74.0% | 94.6% | 0.98 | 0.97 | 0.99 | 1.6 | 27.6% |
| 4 | gpt-5.2 | 70.3% | 92.9% | 80.0% | 86.5% | 0.98 | 0.99 | 0.99 | 1.1 | 7.1% |
| 5 | qwen3-coder-plus | 64.9% | 71.4% | 68.0% | 89.2% | 0.96 | 0.96 | 0.93 | 1.3 | 28.6% |
| 6 | llama-4-maverick | 62.2% | 35.9% | 45.5% | 97.3% | 0.94 | 0.93 | 0.93 | 2.1 | 64.1% |
| 7 | grok-4-fast | 37.8% | 100.0% | 54.9% | 54.1% | 1.00 | 1.00 | 0.99 | 0.6 | 0.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 31/37 | 16.2% | 0.0% | 37.8% | 54 | 12 | 0.32 |
| gemini-3-pro | 31/37 | 16.2% | 0.0% | 37.8% | 47 | 0 | 0.00 |
| deepseek-v3-2 | 28/37 | 24.3% | 2.7% | 18.9% | 42 | 16 | 0.43 |
| gpt-5.2 | 26/37 | 29.7% | 2.7% | 27.0% | 39 | 3 | 0.08 |
| qwen3-coder-plus | 24/37 | 35.1% | 13.5% | 18.9% | 35 | 14 | 0.38 |
| llama-4-maverick | 23/37 | 37.8% | 27.0% | 8.1% | 28 | 50 | 1.35 |
| grok-4-fast | 14/37 | 62.2% | 0.0% | 18.9% | 24 | 0 | 0.00 |

---

## Performance by Vulnerability Type

### Logic Error (5 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 4/5 | 80.0% | 80.0% | 80.0% | 1.00 |
| claude-opus-4-5 | 3/5 | 60.0% | 85.7% | 70.6% | 1.00 |
| gemini-3-pro | 2/5 | 40.0% | 100.0% | 57.1% | 1.00 |
| gpt-5.2 | 2/5 | 40.0% | 80.0% | 53.3% | 1.00 |
| llama-4-maverick | 2/5 | 40.0% | 62.5% | 48.8% | 0.95 |
| qwen3-coder-plus | 2/5 | 40.0% | 80.0% | 53.3% | 0.75 |
| grok-4-fast | 0/5 | 0.0% | 100.0% | N/A | N/A |

### Dos (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 4/4 | 100.0% | 71.4% | 83.3% | 1.00 |
| claude-opus-4-5 | 3/4 | 75.0% | 100.0% | 85.7% | 1.00 |
| deepseek-v3-2 | 3/4 | 75.0% | 60.0% | 66.7% | 1.00 |
| gpt-5.2 | 3/4 | 75.0% | 83.3% | 78.9% | 0.87 |
| llama-4-maverick | 3/4 | 75.0% | 30.0% | 42.9% | 1.00 |
| grok-4-fast | 2/4 | 50.0% | 100.0% | 66.7% | 1.00 |

### Access Control (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/4 | 100.0% | 85.7% | 92.3% | 1.00 |
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 3/4 | 75.0% | 83.3% | 78.9% | 1.00 |
| qwen3-coder-plus | 2/4 | 50.0% | 40.0% | 44.4% | 1.00 |
| llama-4-maverick | 1/4 | 25.0% | 10.0% | 14.3% | 1.00 |

### Integer Issues (4 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 4/4 | 100.0% | 80.0% | 88.9% | 1.00 |
| deepseek-v3-2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 4/4 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 3/4 | 75.0% | 75.0% | 75.0% | 1.00 |
| qwen3-coder-plus | 3/4 | 75.0% | 100.0% | 85.7% | 1.00 |
| grok-4-fast | 2/4 | 50.0% | 100.0% | 66.7% | 1.00 |

### Weak Randomness (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 3/3 | 100.0% | 60.0% | 75.0% | 1.00 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 3/3 | 100.0% | 37.5% | 54.5% | 1.00 |
| qwen3-coder-plus | 3/3 | 100.0% | 80.0% | 88.9% | 1.00 |

### Unchecked Return (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 77.8% | 87.5% | 1.00 |
| gemini-3-pro | 2/3 | 66.7% | 100.0% | 80.0% | 1.00 |
| gpt-5.2 | 2/3 | 66.7% | 100.0% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/3 | 33.3% | 71.4% | 45.5% | 1.00 |
| llama-4-maverick | 1/3 | 33.3% | 12.5% | 18.2% | 0.70 |
| qwen3-coder-plus | 1/3 | 33.3% | 66.7% | 44.4% | 0.50 |
| grok-4-fast | 0/3 | 0.0% | 100.0% | N/A | N/A |

### Front Running (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gemini-3-pro | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| gpt-5.2 | 1/2 | 50.0% | 100.0% | 66.7% | 1.00 |
| deepseek-v3-2 | 0/2 | 0.0% | 40.0% | N/A | N/A |
| grok-4-fast | 0/2 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/2 | 0.0% | 14.3% | N/A | N/A |
| qwen3-coder-plus | 0/2 | 0.0% | 33.3% | N/A | N/A |

### Timestamp Dependency (2 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 2/2 | 100.0% | 80.0% | 88.9% | 1.00 |
| deepseek-v3-2 | 2/2 | 100.0% | 50.0% | 66.7% | 1.00 |
| gemini-3-pro | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 2/2 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 2/2 | 100.0% | 42.9% | 60.0% | 1.00 |
| qwen3-coder-plus | 2/2 | 100.0% | 75.0% | 85.7% | 1.00 |

### Selfdestruct (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Storage Misuse (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Data Exposure (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Tx Origin Auth (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |

### Oracle Manipulation (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Contract Check Bypass (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Reentrancy (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| claude-opus-4-5 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 66.7% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | 100.0% | N/A | N/A |
| llama-4-maverick | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | 100.0% | N/A | N/A |

### Variable Shadowing (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Forced Ether (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.50 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.50 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 25.0% | 40.0% | 0.30 |
| qwen3-coder-plus | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

### Short Address (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 0/1 | 0.0% | 50.0% | N/A | N/A |
| deepseek-v3-2 | 0/1 | 0.0% | 33.3% | N/A | N/A |
| gemini-3-pro | 0/1 | 0.0% | 100.0% | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
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

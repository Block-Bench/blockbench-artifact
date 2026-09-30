# DS Tier1 - Combined Summary

**Judge Model:** mimo-v2-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 100.0% | 89.1% | 94.3% | 100.0% | 0.97 | 0.92 | 0.98 | 2.3 | 10.9% |
| 2 | gemini-3-pro | 75.0% | 100.0% | 85.7% | 100.0% | 1.00 | 1.00 | 1.00 | 1.6 | 0.0% |
| 3 | llama-4-maverick | 75.0% | 39.3% | 51.6% | 100.0% | 0.94 | 0.90 | 0.94 | 3.0 | 60.7% |
| 4 | deepseek-v3-2 | 65.0% | 76.2% | 70.2% | 100.0% | 0.98 | 0.96 | 0.98 | 2.1 | 23.8% |
| 5 | qwen3-coder-plus | 65.0% | 67.6% | 66.3% | 95.0% | 0.97 | 0.96 | 0.92 | 1.7 | 32.4% |
| 6 | gpt-5.2 | 60.0% | 100.0% | 75.0% | 80.0% | 1.00 | 1.00 | 1.00 | 1.0 | 0.0% |
| 7 | grok-4-fast | 40.0% | 95.2% | 56.3% | 80.0% | 0.99 | 1.00 | 0.99 | 1.1 | 4.8% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 20/20 | 0.0% | 0.0% | 60.0% | 41 | 5 | 0.25 |
| gemini-3-pro | 15/20 | 25.0% | 0.0% | 50.0% | 32 | 0 | 0.00 |
| llama-4-maverick | 15/20 | 25.0% | 15.0% | 30.0% | 24 | 37 | 1.85 |
| deepseek-v3-2 | 13/20 | 35.0% | 10.0% | 70.0% | 32 | 10 | 0.50 |
| qwen3-coder-plus | 13/20 | 35.0% | 5.0% | 45.0% | 23 | 11 | 0.55 |
| gpt-5.2 | 12/20 | 40.0% | 0.0% | 35.0% | 20 | 0 | 0.00 |
| grok-4-fast | 8/20 | 60.0% | 0.0% | 45.0% | 20 | 1 | 0.05 |

---

## Performance by Vulnerability Type

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 91.7% | 95.7% | 0.99 |
| gemini-3-pro | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 6/7 | 85.7% | 91.7% | 88.6% | 1.00 |
| llama-4-maverick | 6/7 | 85.7% | 44.4% | 58.5% | 1.00 |
| qwen3-coder-plus | 6/7 | 85.7% | 100.0% | 92.3% | 1.00 |
| grok-4-fast | 4/7 | 57.1% | 100.0% | 72.7% | 1.00 |

### Unchecked Return (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 85.7% | 92.3% | 0.97 |
| deepseek-v3-2 | 4/7 | 57.1% | 82.4% | 67.5% | 0.95 |
| llama-4-maverick | 3/7 | 42.9% | 40.0% | 41.4% | 0.90 |
| qwen3-coder-plus | 3/7 | 42.9% | 64.3% | 51.4% | 0.93 |
| gemini-3-pro | 2/7 | 28.6% | 100.0% | 44.4% | 1.00 |
| gpt-5.2 | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |

### Access Control (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 3/3 | 100.0% | 33.3% | 50.0% | 0.83 |
| grok-4-fast | 2/3 | 66.7% | 100.0% | 80.0% | 0.95 |
| qwen3-coder-plus | 2/3 | 66.7% | 33.3% | 44.4% | 0.95 |
| deepseek-v3-2 | 1/3 | 33.3% | 42.9% | 37.5% | 1.00 |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Integer Issues (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.90 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Interface Mismatch (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.70 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |

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

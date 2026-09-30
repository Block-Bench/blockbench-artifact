# DS Tier1 - Combined Summary

**Judge Model:** gemini-3-flash  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 95.0% | 93.5% | 94.2% | 100.0% | 1.00 | 0.99 | 0.99 | 2.3 | 6.5% |
| 2 | gemini-3-pro | 75.0% | 100.0% | 85.7% | 100.0% | 1.00 | 0.99 | 1.00 | 1.6 | 0.0% |
| 3 | llama-4-maverick | 75.0% | 42.6% | 54.4% | 100.0% | 0.93 | 0.89 | 0.99 | 3.0 | 57.4% |
| 4 | deepseek-v3-2 | 70.0% | 66.7% | 68.3% | 100.0% | 0.96 | 0.94 | 0.99 | 2.1 | 33.3% |
| 5 | qwen3-coder-plus | 70.0% | 70.6% | 70.3% | 90.0% | 0.93 | 0.90 | 0.96 | 1.7 | 29.4% |
| 6 | gpt-5.2 | 60.0% | 100.0% | 75.0% | 80.0% | 1.00 | 1.00 | 1.00 | 1.0 | 0.0% |
| 7 | grok-4-fast | 40.0% | 90.5% | 55.5% | 80.0% | 1.00 | 1.00 | 1.00 | 1.1 | 9.5% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 19/20 | 5.0% | 5.0% | 65.0% | 43 | 3 | 0.15 |
| gemini-3-pro | 15/20 | 25.0% | 0.0% | 50.0% | 32 | 0 | 0.00 |
| llama-4-maverick | 15/20 | 25.0% | 5.0% | 35.0% | 26 | 35 | 1.75 |
| deepseek-v3-2 | 14/20 | 30.0% | 15.0% | 40.0% | 28 | 14 | 0.70 |
| qwen3-coder-plus | 14/20 | 30.0% | 10.0% | 40.0% | 24 | 10 | 0.50 |
| gpt-5.2 | 12/20 | 40.0% | 0.0% | 35.0% | 20 | 0 | 0.00 |
| grok-4-fast | 8/20 | 60.0% | 10.0% | 40.0% | 19 | 2 | 0.10 |

---

## Performance by Vulnerability Type

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 91.7% | 95.7% | 1.00 |
| deepseek-v3-2 | 7/7 | 100.0% | 66.7% | 80.0% | 0.96 |
| gemini-3-pro | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 7/7 | 100.0% | 50.0% | 66.7% | 0.97 |
| qwen3-coder-plus | 6/7 | 85.7% | 80.0% | 82.8% | 1.00 |
| grok-4-fast | 4/7 | 57.1% | 100.0% | 72.7% | 1.00 |

### Unchecked Return (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 4/7 | 57.1% | 94.1% | 71.1% | 1.00 |
| qwen3-coder-plus | 3/7 | 42.9% | 71.4% | 53.6% | 1.00 |
| gemini-3-pro | 2/7 | 28.6% | 100.0% | 44.4% | 1.00 |
| llama-4-maverick | 2/7 | 28.6% | 44.0% | 34.6% | 0.75 |
| gpt-5.2 | 1/7 | 14.3% | 100.0% | 25.0% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 88.9% | 24.6% | 1.00 |

### Access Control (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 3/3 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 3/3 | 100.0% | 33.3% | 50.0% | 0.93 |
| qwen3-coder-plus | 3/3 | 100.0% | 66.7% | 80.0% | 0.90 |
| grok-4-fast | 2/3 | 66.7% | 66.7% | 66.7% | 1.00 |
| deepseek-v3-2 | 1/3 | 33.3% | 28.6% | 30.8% | 1.00 |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 1.00 |

### Integer Issues (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 1.00 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Interface Mismatch (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| deepseek-v3-2 | 1/1 | 100.0% | 50.0% | 66.7% | 0.70 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 50.0% | 66.7% | 0.30 |
| claude-opus-4-5 | 0/1 | 0.0% | N/A | N/A | N/A |
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

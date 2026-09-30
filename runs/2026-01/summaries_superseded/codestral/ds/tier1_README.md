# DS Tier1 - Combined Summary

**Judge Model:** codestral  
**Generated:** 2026-01-05 19:29:12 UTC  
**Total Models:** 7

---

## Model Rankings (by Target Detection Rate)

| Rank | Detector | TDR | Precision | F1 | Verdict Acc | RCIR | AVA | FSV | Findings | FP Rate |
|:----:|:---------|----:|----------:|---:|------------:|-----:|----:|----:|---------:|--------:|
| 1 | claude-opus-4-5 | 100.0% | 93.5% | 96.6% | 100.0% | 0.95 | 0.91 | 0.94 | 2.3 | 6.5% |
| 2 | llama-4-maverick | 85.0% | 47.5% | 61.0% | 100.0% | 0.89 | 0.86 | 0.86 | 3.0 | 52.5% |
| 3 | gemini-3-pro | 75.0% | 87.5% | 80.8% | 100.0% | 0.97 | 0.97 | 0.97 | 1.6 | 12.5% |
| 4 | deepseek-v3-2 | 70.0% | 83.3% | 76.1% | 100.0% | 0.92 | 0.90 | 0.92 | 2.1 | 16.7% |
| 5 | qwen3-coder-plus | 65.0% | 79.4% | 71.5% | 95.0% | 0.92 | 0.92 | 0.92 | 1.7 | 20.6% |
| 6 | gpt-5.2 | 60.0% | 95.0% | 73.5% | 80.0% | 0.96 | 0.96 | 0.94 | 1.0 | 5.0% |
| 7 | grok-4-fast | 40.0% | 81.0% | 53.5% | 80.0% | 0.97 | 0.99 | 0.96 | 1.1 | 19.0% |

### Detailed Metrics

| Detector | Found | Miss Rate | Lucky Guess | Bonus Disc | TP | FP | FAD |
|:---------|------:|----------:|------------:|-----------:|---:|---:|----:|
| claude-opus-4-5 | 20/20 | 0.0% | 0.0% | 45.0% | 43 | 3 | 0.15 |
| llama-4-maverick | 17/20 | 15.0% | 15.0% | 10.0% | 29 | 32 | 1.60 |
| gemini-3-pro | 15/20 | 25.0% | 10.0% | 35.0% | 28 | 4 | 0.20 |
| deepseek-v3-2 | 14/20 | 30.0% | 15.0% | 35.0% | 35 | 7 | 0.35 |
| qwen3-coder-plus | 13/20 | 35.0% | 30.0% | 25.0% | 27 | 7 | 0.35 |
| gpt-5.2 | 12/20 | 40.0% | 0.0% | 35.0% | 19 | 1 | 0.05 |
| grok-4-fast | 8/20 | 60.0% | 20.0% | 25.0% | 17 | 4 | 0.20 |

---

## Performance by Vulnerability Type

### Reentrancy (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 91.7% | 95.7% | 0.99 |
| gemini-3-pro | 7/7 | 100.0% | 100.0% | 100.0% | 1.00 |
| gpt-5.2 | 7/7 | 100.0% | 100.0% | 100.0% | 0.99 |
| llama-4-maverick | 7/7 | 100.0% | 44.4% | 61.5% | 0.97 |
| deepseek-v3-2 | 6/7 | 85.7% | 91.7% | 88.6% | 1.00 |
| qwen3-coder-plus | 6/7 | 85.7% | 90.0% | 87.8% | 0.98 |
| grok-4-fast | 4/7 | 57.1% | 71.4% | 63.5% | 1.00 |

### Unchecked Return (7 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 7/7 | 100.0% | 95.2% | 97.6% | 0.93 |
| llama-4-maverick | 5/7 | 71.4% | 48.0% | 57.4% | 0.80 |
| deepseek-v3-2 | 4/7 | 57.1% | 88.2% | 69.4% | 0.85 |
| qwen3-coder-plus | 4/7 | 57.1% | 57.1% | 57.1% | 0.85 |
| gemini-3-pro | 2/7 | 28.6% | 73.3% | 41.1% | 0.90 |
| gpt-5.2 | 1/7 | 14.3% | 83.3% | 24.4% | 1.00 |
| grok-4-fast | 1/7 | 14.3% | 77.8% | 24.1% | 1.00 |

### Access Control (3 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 3/3 | 100.0% | 100.0% | 100.0% | 0.90 |
| gemini-3-pro | 3/3 | 100.0% | 100.0% | 100.0% | 0.93 |
| gpt-5.2 | 3/3 | 100.0% | 100.0% | 100.0% | 0.90 |
| deepseek-v3-2 | 2/3 | 66.7% | 57.1% | 61.5% | 0.85 |
| grok-4-fast | 2/3 | 66.7% | 100.0% | 80.0% | 0.90 |
| llama-4-maverick | 2/3 | 66.7% | 55.6% | 60.6% | 0.90 |
| qwen3-coder-plus | 1/3 | 33.3% | 100.0% | 50.0% | 0.90 |

### Weak Randomness (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| gpt-5.2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
| grok-4-fast | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 66.7% | 80.0% | 1.00 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |

### Integer Issues (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| deepseek-v3-2 | 0/1 | 0.0% | N/A | N/A | N/A |
| gpt-5.2 | 0/1 | 0.0% | N/A | N/A | N/A |
| grok-4-fast | 0/1 | 0.0% | N/A | N/A | N/A |
| qwen3-coder-plus | 0/1 | 0.0% | N/A | N/A | N/A |

### Interface Mismatch (1 samples)

| Detector | Found | Rate | Precision | F1 | RCIR |
|:---------|------:|-----:|----------:|---:|-----:|
| claude-opus-4-5 | 1/1 | 100.0% | 50.0% | 66.7% | 0.90 |
| deepseek-v3-2 | 1/1 | 100.0% | 100.0% | 100.0% | 0.80 |
| gemini-3-pro | 1/1 | 100.0% | 100.0% | 100.0% | 1.00 |
| llama-4-maverick | 1/1 | 100.0% | 33.3% | 50.0% | 0.80 |
| qwen3-coder-plus | 1/1 | 100.0% | 100.0% | 100.0% | 0.90 |
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

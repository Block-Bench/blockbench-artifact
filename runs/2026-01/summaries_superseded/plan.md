# ACL Paper Visualization Plan

**Working Title:** LLM-Based Smart Contract Vulnerability Detection: A Comprehensive Benchmark

**Last Updated:** 2026-01-05

---

## Tables

### Table 1: Detection Results (DS + TC Benchmarks)
| Model | DS-T1 | DS-T2 | DS-T3 | DS-T4 | DS-Avg | TC-San | TC-MinSan | TC-Shape | TC-Avg |
|-------|-------|-------|-------|-------|--------|--------|-----------|----------|--------|

- **Rows:** 7 LLM detectors + Slither + Mythril
- **Purpose:** Shows detection across difficulty tiers (DS) and obfuscation variants (TC)
- **Key insights:**
  - DS: How detection degrades with contract complexity
  - TC: Which models rely on memorization vs genuine understanding
- **Note:** DS is pre-cutoff (before 2023), TC is post-cutoff with sanitization/obfuscation

### Table 2: Prompt Protocol Results (GS Benchmark)
| Model | Direct | Context | CoT | CoT-Adversarial | CoT-Naturalistic |
|-------|--------|---------|-----|-----------------|------------------|

- **Rows:** 7 LLM detectors
- **Purpose:** Shows how prompt engineering affects detection on gold standard samples
- **Key insight:** CoT helps weaker models, may hurt stronger ones (overthinking?)
- **Note:** All use same 34 gold standard samples with different prompt strategies

### Table 3: Quality Metrics (Overall)
| Model | RCIR | AVA | FSV | Lucky Guess % | False Alarm Rate |
|-------|------|-----|-----|---------------|------------------|

- **Rows:** 7 LLM detectors
- **Purpose:** Deeper quality analysis beyond just detection rate
- **Key insight:** High TDR doesn't always mean high quality explanations
- **Aggregation:** Combined across ALL datasets (DS + TC + GS) where model found target
- **Metrics:**
  - RCIR: Root Cause Identification Rate (0-1) - did model explain WHY correctly?
  - AVA: Attack Vector Accuracy (0-1) - was the attack scenario valid?
  - FSV: Fix Suggestion Validity (0-1) - would the suggested fix work?
  - Lucky Guess %: Found target but wrong root cause (PARTIAL_MATCH / total found)
  - False Alarm Rate: Invalid findings per sample (HALLUCINATED + MISCHARACTERIZED)

### Table 4: Judge Agreement Analysis
| Detector | Codestral | Gemini-Flash | MIMO | GLM | Mistral | Fleiss-κ |
|----------|-----------|--------------|------|-----|---------|----------|

- **Purpose:** Shows inter-judge reliability
- **Key insight:** Evaluation variance and the need for multiple judges
- **Note:** Fleiss-κ for overall inter-rater agreement

---

## Figures (Main Paper - 5 Key Figures)

### Figure 1: TC Obfuscation Resistance (Line Chart)
- **X-axis:** TC variants ordered by obfuscation level (Sanitized → MinimalSan → NoComments → ShapeShifter → Trojan → FalseProphet)
- **Y-axis:** TDR (0-100%)
- **Format:** SWE-Bench style multi-line chart
- **Purpose:** Shows which models degrade gracefully when memorization is blocked
- **Key insight:** Steep drops indicate memorization reliance; flat lines indicate genuine understanding
- **Visual Style:**
  - One colored line per model with circular markers at each data point
  - Distinct colors: Claude (purple), GPT (green), Gemini (blue), Llama (orange), DeepSeek (red), Grok (cyan), Qwen (pink)
  - Light grid background for readability
  - Legend on right side or bottom
  - Clean, modern aesthetic (minimal clutter)
  - Line thickness: 2px, marker size: 8px
- **Tool:** matplotlib with seaborn styling

### Figure 2: GS Protocol Effect (Grouped Bar Chart)
- **X-axis:** Models (7 LLMs)
- **Groups:** Direct, Context, CoT, CoT-Adversarial, CoT-Naturalistic
- **Y-axis:** TDR (0-100%)
- **Purpose:** Shows how prompt engineering affects detection
- **Key insight:** CoT helps weaker models, may hurt stronger ones (overthinking?)
- **Visual Style:**
  - Vertical grouped bars, one color per protocol
  - Protocol colors: Direct (gray), Context (light blue), CoT (blue), CoT-Adv (orange), CoT-Nat (green)
  - Slight gap between model groups, bars within group touching
  - Value labels on top of bars (optional)
  - Legend at top or bottom
- **Tool:** matplotlib grouped bar

### Figure 3: CodeAct Paradox Plot (Scatter) - NOVEL CONTRIBUTION
- **X-axis:** Location match rate (found the right code lines) 0-100%
- **Y-axis:** Root cause match rate (explained it correctly) 0-100%
- **Format:** Scatter with diagonal reference line (y=x)
- **Purpose:** Visualizes "finds code but can't explain" phenomenon
- **Key insight:** Points below diagonal = models that locate vulnerable code but fail to articulate why
- **Visual Style:**
  - Diagonal dashed line (gray) representing "perfect understanding" (y=x)
  - Large circular markers, one per model
  - Each point labeled with model name (offset to avoid overlap)
  - Point size proportional to total samples OR uniform
  - Color by model family or uniform with labels
  - Shaded region below diagonal = "location > understanding" zone
  - Grid lines for both axes
- **Tool:** matplotlib scatter with annotations

### Figure 4: Vulnerability Type Heatmap
- **X-axis:** Vulnerability types (reentrancy, access_control, oracle_manipulation, arithmetic_error, price_oracle, etc.)
- **Y-axis:** Models (7 LLMs + Slither + Mythril)
- **Color:** TDR intensity (0-100%)
- **Purpose:** Reveals model specializations and blind spots
- **Key insight:** Some models excel at reentrancy, others at access control; ensemble may be beneficial
- **Visual Style:**
  - Sequential colormap: white (0%) → dark blue (100%) or viridis
  - Annotate each cell with TDR value (e.g., "45%")
  - Bold/highlight highest value per column (best model for that vuln type)
  - Clear cell borders
  - Rotated x-axis labels if needed
- **Tool:** seaborn heatmap with annotations

### Figure 5: Differential Detection Advantage (Bar Chart)
- **X-axis:** Models (7 LLMs)
- **Y-axis:** TDR (0-100%)
- **Format:** Paired bars per model (Single-code TDR vs Differential TDR)
- **Purpose:** Shows whether seeing the fix helps models understand the vulnerability
- **Key insight:** Large gaps indicate models benefit from comparative context
- **Visual Style:**
  - Two bars per model: Single (gray/light) vs Differential (colored/dark)
  - Delta annotation above bar pairs showing improvement (e.g., "+12%")
  - Consistent model ordering (alphabetical or by performance)
  - Legend: "Single Code" vs "Differential (with fix)"
- **Tool:** matplotlib grouped bar

---

## Figures (Appendix/Supplementary)

### Figure A1: DS Difficulty Scaling (Line Chart)
- **X-axis:** Tier 1 → Tier 4
- **Y-axis:** TDR
- **Format:** One line per model (LLMs + Slither + Mythril)
- **Purpose:** Shows how detection degrades with contract complexity
- **Tool:** matplotlib line plot

### Figure A2: Judge Agreement Heatmap
- **Format:** Confusion matrix style showing judge pair agreement rates
- **Purpose:** Quantifies inter-judge reliability
- **Tool:** seaborn heatmap with annotations

### Figure A3: Radar/Spider Chart - Top Model Comparison
- **Axes:** TDR, RCIR, AVA, FSV, Precision
- **Format:** One polygon per top 4-5 models
- **Purpose:** Shows strengths/weaknesses at a glance
- **Tool:** matplotlib radar chart

---

## Methodology Flowchart (TODO - Discuss Later)
- Full pipeline visualization: Data Collection → Annotation → Transformations → Detection → Evaluation → Results
- TikZ implementation, flow.io aesthetic
- Too complex to finalize now - defer to later discussion

---

## CodeAct Visualization (Main Paper - Small Figure)

### Interpretability-Style Code Snippet
Show a small vulnerable function with colored line-level annotations:

```
┌─────────────────────────────────────────────────────────────┐
│ function withdraw(uint amount) public {                     │
│   require(balances[msg.sender] >= amount); ████ PREREQ      │ ← gray
│                                                             │
│   msg.sender.call{value: amount}("");      ████ ROOT_CAUSE  │ ← red
│   require(success);                                         │
│                                                             │
│   balances[msg.sender] -= amount;          ████ SECONDARY   │ ← orange
│                                                             │
│   emit Withdrawal(msg.sender, amount);     ████ BENIGN      │ ← green
│ }                                                           │
└─────────────────────────────────────────────────────────────┘
```

**Visual Style:**
- Syntax-highlighted code snippet (small, ~10 lines max)
- Colored sidebar/tags for each annotated line
- Compact legend: 🔴 ROOT_CAUSE | 🟠 SECONDARY | ⚫ PREREQ | 🟢 BENIGN
- Clean, minimal - fits in a column width
- Purpose: Shows how we annotate code for fine-grained evaluation

**Implementation:** LaTeX listings package with custom color rules, or TikZ overlay

---

## Tables Layout (Squeeze to 1 Page)

Target: All 4 tables on single page using:
- Smaller font (8pt)
- Abbreviated headers (T1, T2, T3, T4 instead of Tier 1, etc.)
- Two-column layout where possible
- Minimal vertical spacing

---

## Case Studies (Qualitative Boxes)

### Case Study 1: The Beanstalk Paradox (ms_tc_002)
- **Content:**
  - Ground truth: governance_attack via flash loan
  - Llama's detection: "Flash Loan Attack" (correct understanding!)
  - Codestral verdict: NOT FOUND (terminology mismatch)
  - MIMO verdict: FOUND (more lenient)
- **Purpose:** Illustrates judge variance and terminology sensitivity
- **Format:** Side-by-side code + JSON snippets

### Case Study 2: True Understanding Failure
- **Sample:** Pick from "both judges rejected" list (ms_tc_011, ms_tc_015, etc.)
- **Content:** Show where model flagged right lines but completely wrong explanation
- **Purpose:** Contrast with Case Study 1 - legitimate failures exist
- **Format:** Code snippet with annotations

### Case Study 3: Traditional Tool Limitation
- **Content:** Contract that LLMs detect but Slither/Mythril miss
- **Purpose:** Motivates LLM approach
- **Format:** Code + tool outputs comparison

---

## Appendix Tables

### Table A1: Full Per-Sample Results
- Complete detection matrix for reproducibility
- Format: CSV or supplementary material

### Table A2: Prompt Templates
- System prompts for detection
- Judge evaluation prompts
- Protocol context templates

### Table A3: CodeAct Annotation Schema
- Security function definitions (ROOT_CAUSE, SECONDARY_VULN, PREREQ, BENIGN, etc.)
- Code act type taxonomy

### Table A4: Cost and Latency Comparison
| Model | Avg Latency (ms) | Cost per 1K tokens | Total Benchmark Cost |
|-------|------------------|--------------------|--------------------|

### Table A5: Dataset Statistics
- Samples per tier/variant
- Vulnerability type distribution
- Contract complexity metrics (LOC, functions, etc.)

---

## Key Narrative Points

1. **LLMs outperform traditional tools** on complex vulnerabilities but with important caveats

2. **Judge variance is significant** - single-judge evaluation is unreliable, need ensemble

3. **The Paradox Discovery:** Line-level understanding ≠ Explanation quality
   - Models can identify vulnerable code but fail to articulate the vulnerability correctly
   - This is a fundamental limitation for practical deployment

4. **Temporal contamination matters** - sanitization significantly drops performance
   - Suggests memorization plays a role in some models

5. **CoT has differential effects**
   - Helps weaker models (deepseek, llama) significantly
   - Can hurt stronger models (gemini-pro) - overthinking?

6. **Vulnerability type specialization exists**
   - Some models better at reentrancy, others at access control
   - Ensemble approaches may be beneficial

7. **Quality beyond detection**
   - RCIR/AVA/FSV metrics reveal explanation quality varies widely
   - High TDR with low quality = limited practical value

---

## TODO

- [ ] Generate actual data for all tables
- [ ] Create visualization scripts in `scripts/visualize_*.py`
- [ ] Run statistical significance tests
- [ ] Collect cost/latency data
- [ ] Write case study narratives
- [ ] Design figure color scheme (colorblind-friendly)

---

## Notes

- ACL format: 8 pages + references + appendix
- Focus on 4-5 key figures for main paper
- Move detailed tables to appendix
- Emphasize novel contributions: CodeAct paradox analysis, multi-judge evaluation

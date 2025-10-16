# SU_RA_Tasks

A comprehensive research portfolio investigating Large Language Model (LLM) behavior, bias detection, ethical implications, and decision-making systems. This umbrella repository compiles investigative research across multiple domains of AI ethics and data analysis.

## Overview

This research portfolio documents systematic investigations into how LLMs process data, generate narratives, and make decisions. The work spans from foundational data analysis through advanced bias detection and ethical evaluation, providing both methodological frameworks and empirical findings on LLM trustworthiness.

**Research Institution:** Syracuse University 

---

## Research Projects

### [Task 03: Descriptive Statistics Analysis](./SU_RA_Task_03_Descriptive_Stats)

Foundational data analysis and descriptive statistics using real-world datasets. This task establishes baseline statistical methods and data visualization techniques used throughout the portfolio.

**Key Focus:**
- Exploratory data analysis (EDA)
- Descriptive statistics computation
- Data visualization and interpretation
- Dataset documentation and cleaning

**Skills Developed:** Pandas, NumPy, Matplotlib, statistical reasoning

---

### [Task 05: Descriptive Statistics with Sports Data](./SU_RA_Task_05_Descriptive_Stats)

Extension of descriptive statistics applied to sports performance datasets. Develops domain-specific analysis methods for athlete performance evaluation and team dynamics.

**Key Focus:**
- Sports data acquisition and cleaning
- Performance metrics calculation
- Comparative statistical analysis
- Data-driven insights generation

**Skills Developed:** Domain-specific analysis, sports analytics, comparative metrics

---

### [Task 06: Deep Fake Detection & Synthetic Media Analysis](./SU_RA_Task_06_Deep_Fake)

Investigation into detection and implications of synthetic media, including deepfakes and AI-generated content. Examines the intersection of LLM-generated text and visual media authenticity verification.

**Key Focus:**
- Deepfake detection methodologies
- Synthetic media identification
- Media literacy and verification strategies
- Ethical implications of generative AI

**Skills Developed:** Media analysis, detection algorithms, synthetic data evaluation

---

### [Task 07: LLM-Assisted Decision Making & Ethical Implications](./SU_RA_Task_07_Decision_Making)

Systematic analysis of how LLMs influence human decision-making processes. Investigates whether and how LLM recommendations bias human choices across multiple domains.

**Key Focus:**
- LLM recommendation influence on human decisions
- Ethical considerations in AI-assisted workflows
- Decision quality assessment
- Human-AI collaboration patterns
- Risk assessment for delegation to LLMs

**Skills Developed:** User study design, qualitative analysis, ethical frameworks, decision science

---

### [Task 08: Bias Detection in LLM Data Narratives](./SU_RA_Task_08_Bias_Detection)

**Status:** In Progress (Phase 2 - Data Collection)

Controlled experimental investigation of systematic biases in LLM-generated data narratives. Tests whether identical datasets produce different analyses based on prompt framing and demographic information presentation.

**Key Focus:**
- Framing effects in LLM analysis
- Demographic bias in recommendations
- Confirmation bias detection
- Selection bias and cherry-picking patterns
- Cross-model bias comparison (Claude, GPT-4, Gemini)

**Hypotheses:**
- H1: Positive vs negative framing changes recommendations
- H2: Demographic information affects coaching/resource allocation suggestions
- H3: Question framing (deficit vs opportunity) produces different narratives
- H4: LLMs selectively cite evidence to support primed conclusions

**Experimental Design:** 195 LLM responses (13 prompts × 3 models × 5 samples)

**Skills Developed:** Experimental design, statistical testing, NLP analysis, API integration, research methodology

---

## Research Progression & Themes

The portfolio follows a deliberate progression from foundational to advanced:

```
Task 03-05: Data Analysis Foundation
    ↓
Task 06: Synthetic Media & Authenticity
    ↓
Task 07: LLM Decision-Making Influence
    ↓
Task 08: Systematic Bias Detection
```

**Overarching Themes:**
- **Trustworthiness**: Can we rely on LLM outputs?
- **Bias & Fairness**: How do LLMs systematically distort analysis?
- **Ethics & Accountability**: What are the implications of LLM decision support?
- **Transparency**: Can we understand why LLMs produce specific narratives?
- **Methodology**: How do we rigorously test LLM behavior?

---

## Shared Research Infrastructure

### Ethical Standards Across Projects

All projects adhere to strict ethical guidelines:

✅ **Data Privacy:** All personally identifying information is anonymized  
✅ **Informed Consent:** Human subjects studies include proper IRB considerations  
✅ **Transparency:** All methodologies are fully documented and reproducible  
✅ **Reproducibility:** Code, data, and results can be independently verified  
✅ **Null Results:** Negative findings are reported alongside positive results  

### Technical Stack

**Core Languages & Libraries:**
- Python 3.9+ (primary analysis language)
- Pandas (data manipulation)
- NumPy (numerical computing)
- Matplotlib/Seaborn (visualization)
- SciPy (statistical testing)
- NLTK/TextBlob (NLP analysis)

**LLM APIs:**
- Anthropic Claude (via Syracuse Enterprise License)
- OpenAI GPT-4
- Google Gemini

**Documentation & Version Control:**
- Git/GitHub
- Markdown documentation
- Jupyter Notebooks for exploratory analysis
  
---

## Key Findings & Insights

### Emerging Patterns Across Projects

1. **Data Narrative Malleability**: LLMs generate substantially different interpretations of identical data depending on prompt framing (Task 08 preliminary findings)

2. **Decision Influence**: LLM recommendations affect human decision-making, but effect magnitude varies by domain and expertise (Task 07)

3. **Synthetic Media Complexity**: Deepfake detection requires multi-modal approaches; text and visual analysis must be integrated (Task 06)

4. **Data Quality Matters**: Foundational statistical accuracy is critical for any downstream LLM analysis (Tasks 03-05)

---

## Research Timeline

| Task | Status | Completion | Primary Foci |
|------|--------|-----------|---|
| Task 03 | ✅ Complete | Sept 2025 | Foundational statistics |
| Task 05 | ✅ Complete | Sept 2025 | Sports analytics |
| Task 06 | ✅ Complete | Oct 2025 | Deepfake detection |
| Task 07 | ✅ Complete | Oct 2025 | Decision-making influence |

---

## Ethical Use & Attribution

If you use findings, methodologies, or code from this portfolio in your own research:

1. **Cite appropriately** by project and task number
2. **Preserve anonymization** - never expose sanitized data
3. **Follow ethical guidelines** outlined in each project
4. **Report results transparently** including null findings
5. **Acknowledge collaboration** with Syracuse University

---

## Limitations & Future Work

### Known Limitations Across Portfolio

- Models tested represent snapshot of LLM landscape (October 2025)
- Sports data domain may not generalize to other decision contexts
- Small sample sizes in some analyses (addressed in Task 08)
- Limited cross-cultural evaluation

### Future Research Directions

- [ ] Temporal stability: Do LLM biases persist over time?
- [ ] Fine-tuned models: How does domain-specific training affect bias?
- [ ] Multimodal analysis: Integration of text, image, and audio LLMs
- [ ] Real-world deployment: Bias detection in production systems
- [ ] Intervention strategies: Testing debiasing techniques at scale
- [ ] Cross-cultural bias: Non-English language model analysis

---

## References & Resources

**Foundational Bias Research:**
- Bolukbasi et al. (2016): Bias and Fairness in Word Embeddings
- Buolamwini & Buolamwini (2018): Gender Shades
- Mitchell et al. (2019): Model Cards for Model Reporting

**LLM Ethics Literature:**
- Bender et al. (2021): On the Dangers of Stochastic Parrots
- Weidinger et al. (2021): Ethical and Social Risks of Harms from Language Models
- Caswell et al. (2023): Quality at a Glance: An Audit of Web-Crawled Multilingual Datasets

**Methods & Tools:**
- VADER Sentiment Analysis: https://github.com/cjhutto/vaderSentiment
- Fairness Indicators: https://github.com/tensorflow/fairness-indicators
- Statistical Testing: https://docs.scipy.org/doc/scipy/reference/stats.html

---

## License & Acknowledgments

**Institution:** Syracuse University  
**Program:** Research Assistantship (RA)  
**Data Privacy:** All data anonymized and sanitized per institutional review

---

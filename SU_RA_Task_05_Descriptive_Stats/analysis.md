# Evaluating LLM Performance on Syracuse Women's Lacrosse Data (2023–2025)

## 1. Overview

This research evaluates the ability of three Large Language Models (LLMs)—ChatGPT, Claude, and Google AI Search—to process structured sports statistics and answer natural language questions about the Syracuse Women's Lacrosse team from the 2023, 2024, and 2025 seasons. Data was sourced from [cuse.com](https://cuse.com/sports/2013/1/16/WLAX_0116134638) and provided as PDFs for testing.

The study aims to:

- Measure factual accuracy in retrieving data
- Evaluate reasoning capabilities for derived metrics
- Assess performance on analytical or predictive questions
- Identify limitations caused by unstructured formats and OCR parsing

---

## 2. Dataset

- **Seasons:** 2023, 2024, 2025
- **Format:** PDF files
- **Content:**
  - Team-level statistics: games played, goals, shots, saves, turnovers
  - Player-level statistics: available in 2023, partially in 2025, missing in 2024
  - Game-by-game results with opponent rankings

### Limitations

- 2024 data lacked individual player breakdowns
- 2025 data partially incomplete, OCR errors possible
- Data layout varied season to season, affecting consistency

---

## 3. Methodology

Three levels of questions were tested:

1. **Basic factual retrieval:** Direct lookups (games played, win-loss records)
2. **Intermediate reasoning:** Requires aggregation or filtering (highest total points in a season)
3. **Advanced analytical insights:** Multi-factor judgment calls (impact per minute played, performance vs top-10 opponents)

Each model was queried with identical prompts and responses were manually validated against the dataset.

---

## 4. Results

### 4.1 Basic Retrieval

| Question | ChatGPT | Claude | Google | Ground Truth |
|----------|---------|--------|--------|--------------|
| Games played (2023–2025) | 21, 22, 19 | 21, 22, 19 | 21, 22, 19 | 21, 22, 19 |
| Win-loss record | 18-3, 16-6, 10-9 | 18-3, 16-6, 10-9 | 18-3, 16-6, 10-9 | 18-3, 16-6, 10-9 |
| Top scorer each season | Incorrect 2023, none for 24-25 | Correct 2023 only | Correct all years | Meaghan Tyrrell (2023), Emma Tyrrell (2024), Emma Ward (2025) |

**Observation:** Google outperformed due to possible access to structured external data. ChatGPT and Claude had parsing difficulties from image-based PDFs.

---

### 4.2 Intermediate Reasoning

**Question:** Who had the highest total points (G+A) in 2024?

- **ChatGPT:** Unable to compute due to missing player-level stats
- **Claude:** Same limitation
- **Google:** Emma Tyrrell with 92 points (70G, 22A)

LLMs struggled without structured stats input; only Google supplemented missing data.

---

### 4.3 Advanced Analytical Insight

**Question:** How did Syracuse's performance vs top-10 teams evolve?

- **ChatGPT:** 5-3 (2023), 6-5 (2024), 3-5 (2025)
- **Claude:** 5-2, 5-3, 2-5
- **Google:** 7-3, 3-4, 2-5 with detailed breakdowns

All identified a declining trend, but discrepancies highlighted interpretation errors.

---

## 5. Expanded Analysis of LLM Limitations

1. **OCR Parsing Errors:** Image-based data lost table structure, causing misread values
2. **Incomplete Data:** Missing stats in 2024 led to skipped or fabricated answers
3. **Format Sensitivity:** Structured CSV/JSON likely yields better results
4. **Multi-step Reasoning Weakness:** Models failed at chained calculations without explicit steps
5. **External Knowledge Bias:** Google had advantage but may mix external info with provided dataset
6. **Ranking Ambiguity:** Determining top-10 opponents manually caused inconsistencies
7. **Context Window Issues:** Long PDFs caused data to be ignored or truncated
8. **Cross-table Linking Gaps:** Models struggled to combine player stats, minutes, and outcomes for impact metrics
9. **Numeric Arithmetic Errors:** LLMs occasionally miscalculated percentages or ratios
10. **Noise Interpretation:** Non-data text misread as stats

---

## 6. Prompt Engineering Strategies

To improve LLM responses:

- Explicitly specify table structure and relevant columns
- Request data extraction first, then calculations in a second step
- Instruct fallback handling for missing data instead of guessing
- Provide filtering rules clearly (e.g., min 20 shots)
- Ask for intermediate results and source references for transparency
- Format expected answer as JSON or table for consistency
- Use context-limited prompts focusing on a single table at a time
- If possible, preprocess PDFs to CSV for reliable parsing

---

## 7. Recommendations and Future Work

- Provide structured machine-readable data to all models for fair testing
- Compare zero-shot, few-shot, and chain-of-thought prompting to test reasoning improvement
- Investigate hallucination behavior under missing or ambiguous data conditions
- Introduce post-processing scripts to verify LLM answers against ground truth
- Extend tests to predictive and prescriptive analytics once base factual reliability is ensured
- Evaluate domain-specific fine-tuned LLMs for sports analytics against general-purpose models

---

## 8. Conclusion

Google performed best overall, likely due to external data access, while ChatGPT and Claude underperformed due to OCR errors, unstructured input, and missing player-level stats. Improving data quality, prompt specificity, and introducing structured formats is expected to significantly enhance LLM accuracy in similar sports analytics tasks.

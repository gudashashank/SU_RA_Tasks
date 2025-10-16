# SU_RA_Task_03_Descriptive_Stats

This project involved analyzing social media advertising datasets related to the 2024 U.S. Presidential Election using three different approaches: **Pure Python**, **Pandas**, and **Polars**. Each method aimed to generate core descriptive statistics at both the dataset level and grouped levels (e.g., `page_id`, `ad_id`). Below is a breakdown of what each script does, how to run them, key insights, and reflections.

---

## Script Descriptions

### 1. `pure_python_stats.py`
- Uses only the Python standard library.
- Computes descriptive statistics: count, mean, min, max, standard deviation.
- Handles non-numeric columns via unique value counts and most frequent value.
- Aggregates statistics grouped by `page_id` and (`page_id`, `ad_id`), if available.
- Saves output as: `<filename>_pure_python_stats.csv`.

### 2. `pandas_stats.py`
- Leverages Pandas for efficient data analysis.
- Performs `.describe()` for numeric columns, `.value_counts()` for categorical.
- Aggregates by `page_id` and (`page_id`, `ad_id`).
- Saves output as multiple files:
  - `<filename>_pandas_stats.csv`
  - `<filename>_categorical_pandas_stats.csv`
  - `<filename>_groupby1_pandas_stats.csv`, etc.

### 3. `polars_stats.py`
- Uses Polars for high-performance analysis.
- Computes the same statistics as Pandas but faster on large datasets.
- Includes value counts for categorical columns and group-based aggregations.
- Outputs:
  - `<filename>_polars_stats_summary.csv`
  - `<filename>_categorical_polars_stats.csv`
  - `<filename>_groupby1_polars_stats.csv`, etc.

---

## How to Run

1. Place the script and the dataset in the same folder.
2. Open a terminal and run:
```bash
python <script_name>.py
```
3. When prompted, enter the name of your dataset CSV file.
4. Output files are generated in the same directory.

---
### Dataset Compatibility

Each of the three scripts, `pure_python_stats.py`, `pandas_stats.py`, and `polars_stats.py`—is designed to be **dataset-agnostic** and can process all three provided CSV datasets:

- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_fb_ads_congress_scored_anon.csv`

The scripts detect key group identifiers such as `page_id`, `ad_id`, `Facebook_Id`, `post_id`, etc., dynamically and apply appropriate descriptive statistics and group-level aggregations.

To run the analysis, simply place the desired CSV file in the same directory as the script and follow the command-line prompt to input the file name.

---
## General Insights Across All Datasets

The datasets collectively capture a wide range of advertising and social media activity from the 2024 U.S. Presidential Election.

- Key columns like `estimated_spend`, `estimated_impressions`, and `estimated_audience_size` provide insight into campaign scale and budgetary trends.
- Several categorical fields (e.g., `advocacy_msg_type_illuminating`, `election_integrity_Truth_illuminating`) highlight nuanced messaging strategies around governance, health, immigration, and technology.
- **Total Ads Analyzed**: 246,745
- **Platform**: Facebook + Instagram (multi-platform majority)
- **Top Metrics**:
  - **Mean Estimated Spend**: $1,061.29
  - **Spend Range**: $49.00 to $474,999.00
  - **Average Impressions**: 45,602
  - **Maximum Impressions**: 1,000,000

---

## Method-Specific Insights

### Pure Python Approach
- Achieved full statistics using only built-in libraries.
- Slower and more verbose, especially for grouped computations.
- Valuable for understanding the underlying logic of statistics calculations.

### Pandas-Based Analysis
- Fast and intuitive for both numeric and categorical summaries.
- Grouped analysis revealed:
  - A few political pages drove the bulk of ad impressions and spend.
  - Shared ad IDs across pages suggested cross-page coordination.
- Strong integration with visualization and EDA tools.

### Polars-Based Analysis
- Fastest approach, particularly effective with large datasets.
- More verbose in syntax, especially for non-numeric summaries.
- Ideal for performance-critical, large-scale pipelines.

---

## Challenges and Reflections

**Was it a challenge to produce identical results?**  
Yes. The main challenge was that different libraries handle missing or non-numeric values differently. Pure Python required manual handling of each case, while Pandas and Polars had built-in mechanisms that varied slightly in how they skipped nulls or coerced data types. Consistency was ensured by enforcing type conversions and filtering nulls explicitly.

**Which approach was easiest or most performant?**  
- Easiest: **Pandas** clean syntax, intuitive operations, wide adoption.
- Most performant: **Polars** highly optimized for speed but more verbose.
- Most transparent: **Pure Python** instructive, but not efficient.

**Advice for a junior data analyst?**  
Start with **Pandas**. It provides the best balance of usability and capability, and is widely supported in tutorials, documentation, and job roles. Learn Polars for performance-critical work and explore pure Python for a deeper understanding.

**Can AI like ChatGPT help?**  
Yes. Tools like ChatGPT can generate starter code for all three approaches, provide explanations, and help debug errors. This accelerates learning and boosts confidence, especially in areas like data type handling, group-by logic, and file I/O.

**What do AI tools recommend by default? Do you agree?**  
ChatGPT typically recommends **Pandas** by default for descriptive statistics — a recommendation I agree with. It's mature, readable, and integrates seamlessly with the data science ecosystem. That said, it’s good practice to evaluate Polars or PySpark for scalability.

---
**What’s New (July 1–15, 2025)**
- Performance Benchmarks added across Pure Python, Pandas, and Polars.
- Improved Notebook Documentation for clearer storytelling and stakeholder facing presentations.
- Modular Code Refactoring for better readability and reuse.

## Conclusion

This multi-method exploration highlighted how the same statistical task can be achieved through different lenses. While pure Python enhances understanding, Pandas remains the go-to for practical analysis, and Polars offers an edge for large-scale, high-performance workflows.



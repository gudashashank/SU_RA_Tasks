import polars as pl
import os
import time

def detect_group_keys(columns):
    if "page_id" in columns and "ad_id" in columns:
        return ["page_id"], ["page_id", "ad_id"]
    elif "Facebook_Id" in columns and "post_id" in columns:
        return ["Facebook_Id"], ["Facebook_Id", "post_id"]
    elif "id" in columns and "month_year" in columns:
        return ["id"], ["id", "month_year"]
    else:
        return [], []

def get_categorical_summary(df):
    cat_summary = {}
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            vc = df[col].value_counts()
            count_col = [c for c in vc.columns if "count" in c.lower()][0]
            value_col = [c for c in vc.columns if c != count_col][0]
            most_common_value = vc.sort(count_col, descending=True).limit(1)[0, value_col] if vc.height > 0 else None

            cat_summary[col] = {
                "unique": df[col].n_unique(),
                "most_common": str(most_common_value)
            }

    records = [{"column": k, "unique": v["unique"], "most_common": v["most_common"]} for k, v in cat_summary.items()]
    return pl.DataFrame(records)

def make_aggs(cols):
    aggs = []
    for col in cols:
        aggs.extend([
            pl.col(col).count().alias(f"{col}_count"),
            pl.col(col).mean().alias(f"{col}_mean"),
            pl.col(col).min().alias(f"{col}_min"),
            pl.col(col).max().alias(f"{col}_max")
        ])
    return aggs

def describe_dataset_polars(file_path):
    base_filename = os.path.splitext(file_path)[0]

    print("\nLoading file...")
    start = time.time()
    df = pl.read_csv(file_path)
    end = time.time()
    print(f"✅ File loaded in {round(end - start, 2)} seconds.")
    print(f"Columns: {df.columns}")

    print("\nGenerating basic descriptive statistics...")
    numeric_df = df.select([pl.col(col) for col in df.columns if df[col].dtype in (pl.Int64, pl.Float64)])
    summary_stats = numeric_df.describe()
    summary_file = f"{base_filename}_polars_stats_summary.csv"
    summary_stats.write_csv(summary_file)
    print(f"✅ Saved: {summary_file}")

    print("\nGenerating categorical statistics...")
    cat_summary = get_categorical_summary(df)
    cat_file = f"{base_filename}_categorical_polars_stats.csv"
    cat_summary.write_csv(cat_file)
    print(f"✅ Saved: {cat_file}")

    key1, key2 = detect_group_keys(df.columns)
    numeric_cols = [col for col in df.columns if df[col].dtype in (pl.Int64, pl.Float64)]

    if key1:
        print(f"\nGrouping by {key1}...")
        grouped1 = df.group_by(key1).agg(make_aggs(numeric_cols))
        group1_file = f"{base_filename}_groupby_{'_'.join(key1)}_polars_stats.csv"
        grouped1.write_csv(group1_file)
        print(f"✅ Saved: {group1_file}")

    if key2:
        print(f"\nGrouping by {key2}...")
        grouped2 = df.group_by(key2).agg(make_aggs(numeric_cols))
        group2_file = f"{base_filename}_groupby_{'_'.join(key2)}_polars_stats.csv"
        grouped2.write_csv(group2_file)
        print(f"✅ Saved: {group2_file}")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ").strip()
    if os.path.exists(file_path):
        describe_dataset_polars(file_path)
    else:
        print("❌ File not found. Please check the path and try again.")
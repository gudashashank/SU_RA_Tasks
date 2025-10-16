import pandas as pd
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

def describe_dataframe(df, base_filename):
    print("\nGenerating summary statistics...")

    numeric_stats = df.describe(include=[float, int]).transpose()
    cat_stats = df.describe(include=['object']).transpose()

    summary_csv = f"{base_filename}_pandas_stats_summary.csv"
    numeric_stats.to_csv(summary_csv)
    print(f"✅ Summary statistics saved to: {summary_csv}")

    key1, key2 = detect_group_keys(df.columns)
    numeric_cols = df.select_dtypes(include=['number']).columns

    if key1:
        print(f"\nGrouping by {key1}...")
        if len(numeric_cols) > 0:
            group1 = df.groupby(key1)[numeric_cols].agg(['count', 'mean', 'min', 'max'])
            group1_csv = f"{base_filename}_groupby_{'_'.join(key1)}_pandas_stats.csv"
            group1.to_csv(group1_csv)
            print(f"✅ Grouped summary saved to: {group1_csv}")
        else:
            print("⚠️ No numeric columns to aggregate.")

    if key2:
        print(f"\nGrouping by {key2}...")
        if len(numeric_cols) > 0:
            group2 = df.groupby(key2)[numeric_cols].agg(['count', 'mean', 'min', 'max'])
            group2_csv = f"{base_filename}_groupby_{'_'.join(key2)}_pandas_stats.csv"
            group2.to_csv(group2_csv)
            print(f"✅ Grouped summary saved to: {group2_csv}")
        else:
            print("⚠️ No numeric columns to aggregate.")

def run_analysis(file_path):
    base_filename = os.path.splitext(file_path)[0]

    print("\nLoading file...")
    start = time.time()
    df = pd.read_csv(file_path)
    end = time.time()
    print(f"✅ File loaded in {round(end - start, 2)} seconds.")

    print(f"Columns detected: {list(df.columns)}")

    total_cols = len(df.columns)
    print(f"\nAnalyzing {total_cols} columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"Processing column {i}/{total_cols} ({round((i/total_cols)*100)}%) - {col}")

    describe_dataframe(df, base_filename)

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ").strip()
    if os.path.exists(file_path):
        run_analysis(file_path)
    else:
        print("❌ File not found. Please check the path and try again.")
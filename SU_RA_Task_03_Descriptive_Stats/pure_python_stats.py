import csv
import math
import os
import pandas as pd
from collections import defaultdict, Counter
from statistics import mean

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def summarize_column(data):
    numeric = [float(x) for x in data if is_float(x)]
    non_numeric = [x for x in data if not is_float(x)]
    summary = {}

    if numeric:
        summary['count'] = len(numeric)
        summary['mean'] = round(sum(numeric) / len(numeric), 2)
        summary['min'] = min(numeric)
        summary['max'] = max(numeric)
        if len(numeric) > 1:
            avg = summary['mean']
            variance = sum((x - avg) ** 2 for x in numeric) / (len(numeric) - 1)
            summary['std_dev'] = round(math.sqrt(variance), 2)
    if non_numeric:
        counter = Counter(non_numeric)
        summary['unique'] = len(counter)
        summary['most_common'] = counter.most_common(1)[0]

    return summary

def aggregate_by_keys(data, keys):
    groups = defaultdict(list)
    for row in data:
        try:
            key = tuple(row[k] for k in keys)
            groups[key].append(row)
        except KeyError:
            continue  # Skip if key not found
    return groups

def detect_group_keys(columns):
    if "page_id" in columns and "ad_id" in columns:
        return ["page_id"], ["page_id", "ad_id"]
    elif "Facebook_Id" in columns and "post_id" in columns:
        return ["Facebook_Id"], ["Facebook_Id", "post_id"]
    elif "id" in columns and "month_year" in columns:
        return ["id"], ["id", "month_year"]
    else:
        return [], []

def export_summary_to_csv(summary_dict, output_file):
    df = pd.DataFrame.from_dict(summary_dict, orient='index')
    df.to_csv(output_file)
    print(f"✅ Saved: {output_file}")

def describe_dataset(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    columns = reader.fieldnames
    base_filename = os.path.splitext(path)[0]

    print("Generating summary statistics...\n")

    # Full dataset summary
    full_summary = {}
    for col in columns:
        col_data = [row[col] for row in rows if row[col] != '']
        full_summary[col] = summarize_column(col_data)

    export_summary_to_csv(full_summary, f"{base_filename}_pure_python_stats_summary.csv")

    # Grouped summaries
    key1, key2 = detect_group_keys(columns)

    if key1:
        print(f"Processing group by {key1}...")
        grouped_summary = {}
        page_groups = aggregate_by_keys(rows, key1)
        for group, group_rows in page_groups.items():
            for col in columns:
                col_data = [r[col] for r in group_rows if r[col] != '']
                grouped_summary[(group, col)] = summarize_column(col_data)

        df_group1 = pd.DataFrame.from_dict(grouped_summary, orient='index')
        df_group1.to_csv(f"{base_filename}_groupby_{'_'.join(key1)}_pure_python_stats.csv")
        print(f"✅ Saved: {base_filename}_groupby_{'_'.join(key1)}_pure_python_stats.csv")

    if key2:
        print(f"Processing group by {key2}...")
        grouped_summary2 = {}
        combo_groups = aggregate_by_keys(rows, key2)
        for group, group_rows in combo_groups.items():
            for col in columns:
                col_data = [r[col] for r in group_rows if r[col] != '']
                grouped_summary2[(group, col)] = summarize_column(col_data)

        df_group2 = pd.DataFrame.from_dict(grouped_summary2, orient='index')
        df_group2.to_csv(f"{base_filename}_groupby_{'_'.join(key2)}_pure_python_stats.csv")
        print(f"✅ Saved: {base_filename}_groupby_{'_'.join(key2)}_pure_python_stats.csv")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ").strip()
    if os.path.exists(file_path):
        describe_dataset(file_path)
    else:
        print("❌ File not found. Please check the path and try again.")
import csv
import os


def count_rows(folder_path):
    row_counts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                row_count = sum(1 for row in reader)
                row_counts[filename] = row_count
        if row_count != 8640 and row_count != 8928 and row_count != 8064 and row_count != 8352:
            print(f"{filename} has {row_counts[filename]} rows")
    return row_counts


folder = "./data/BTCUSDT/5m"

count_rows(folder)

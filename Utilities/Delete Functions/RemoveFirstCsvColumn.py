import csv
import os


def remove_first_column(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            with open(os.path.join(directory, filename), 'r') as f_in:
                reader = csv.reader(f_in)
                rows = [row[1:] for row in reader]
            with open(os.path.join(directory, filename), 'w', newline='') as f_out:
                writer = csv.writer(f_out)
                writer.writerows(rows)


remove_first_column("./data/BTCUSDT/5m")

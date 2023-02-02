import csv
import os
from datetime import datetime, timezone


def unix_ms_to_iso_gmt(unix_timestamp_ms):
    unix_timestamp = unix_timestamp_ms / 1000
    iso_time = datetime.fromtimestamp(
        unix_timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return iso_time


def check_csv(folder, row_limit):
    for file in os.listdir(folder):
        #print("Opened: " + file)
        if file.endswith(".csv"):
            with open(os.path.join(folder, file), "r") as csvfile:
                reader = csv.reader(csvfile)

                row_count = 0
                for row in reader:
                    row_count += 1

                try:
                    timestamp = int(row[0])
                    date = unix_ms_to_iso_gmt(timestamp)
                except ValueError:
                    print(f"{file} has invalid timestamp format. Row: {row_count}")

                if row_count > row_limit:
                    print(f"{file} has more rows than {row_limit}.")

                if row_count == 1 and date[11:] != "00:00:00":
                    print(f"{file} doesn't start at midnight.")

                if row_count % 288 == 0 and date[11:] != "23:55:00":
                    print(f"{file} doesn't end at 23:55:00.")


# Example usage of the function
check_csv("./data/BTCUSDT/5m", 288)

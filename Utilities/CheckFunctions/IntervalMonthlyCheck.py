import datetime
import csv
import os
from datetime import datetime, timezone


def unix_ms_to_iso_gmt(unix_timestamp_ms):
    unix_timestamp = unix_timestamp_ms / 1000
    iso_time = datetime.fromtimestamp(
        unix_timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return iso_time


def check_timestamps(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        timestamps = [row[0] for row in reader]
        for i in range(1, len(timestamps)):

            ts1 = unix_ms_to_iso_gmt(int(timestamps[i-1]))
            ts2 = unix_ms_to_iso_gmt(int(timestamps[i]))

            ts3 = timestamps[i-1]
            ts4 = timestamps[i]

            if float(ts4) - float(ts3) != float(300000):
                print(
                    f"Timestamps {unix_ms_to_iso_gmt(int(ts3))} and {unix_ms_to_iso_gmt(int(ts4))} are not 5 minutes apart. {float(ts4) - float(ts3)} Row: {i}")
            else:
                test = 0


def check_csv(folder, monthRows30days, monthRows31days):
    for file in os.listdir(folder):
        # print("--------------------")
        """ if file.endswith(".csv"):
            with open(os.path.join(folder, file), "r") as csvfile:
                reader = csv.reader(csvfile)

                row_count = 0
                for row in reader:
                    if row_count % monthRows30days in [0, 1] or row_count % monthRows31days in [0, 1]:
                        try:
                            timestamp = int(row[0])
                            date = unix_ms_to_iso_gmt(timestamp)
                        except ValueError:
                            print(
                                f"{file} has invalid timestamp format. Row: {row_count}")

                        if row_count == 1 and date[11:] != "00:00:00":
                            print(f"{file} doesn't start at midnight.")

                        if row_count % monthRows30days == 0 and date[11:] != "23:55:00" or row_count % monthRows31days == 0 and date[11:] != "23:55:00":
                            print(f"{file} doesn't end at 23:55:00.")
                    row_count += 1

                if row_count > monthRows30days or row_count > monthRows31days:
                    print(
                        f"{file} has more rows than {monthRows30days} or {monthRows31days}.")

                if row_count < monthRows30days or row_count < monthRows31days:
                    print(
                        f"{file} has less rows than {monthRows30days} or {monthRows31days}.")
 """
        if file.endswith(".csv"):
            check_timestamps(os.path.join(folder, file))


monthRows30days = 8_640
monthRows31days = 8_928

# Example usage of the function
check_csv("./data/BTCUSDT/5m", monthRows30days, monthRows31days)

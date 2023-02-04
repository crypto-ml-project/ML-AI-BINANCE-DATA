import configparser
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
                    # f"Timestamps {unix_ms_to_iso_gmt(int(ts3))} and {unix_ms_to_iso_gmt(int(ts4))} are not 5 minutes apart. {float(ts4) - float(ts3)} Row: {i}")
                    f"File: {ts1}. Timestamps {ts3} and {ts4} are not 5 minutes apart. {float(ts4) - float(ts3)} Row: {i}")


config = configparser.ConfigParser()
config.read(r'database.ini')
# Example usage:
symbol = config['postgresql']['currencySymbol']

folder = f"./data/{symbol}/5m"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        check_timestamps(os.path.join(folder, file))


import sys
import datetime
import requests
import zipfile
import io
import os


def curl_endpoint(symbol, interval, date, save_path):
    url = f"https://data.binance.vision/data/spot/monthly/klines/{symbol}/{interval}/{symbol}-{interval}-{date}.zip"
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status code {response.status_code}")

    # Create the directory if it does not exist
    os.makedirs(save_path, exist_ok=True)

    # Unzip the content of the response
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(save_path)

    # Find the csv file in the extracted files
    for filename in z.namelist():
        if filename.endswith(".csv"):
            csv_file = os.path.join(save_path, filename)
            break

    return csv_file


def get_and_save_kline_data_range(symbol, interval, start_date, end_date, save_path):

    # Check if the start date is before the end date
    if start_date > end_date:
        raise Exception("Start date is after end date")

    # Call the curl endpoint function for each month in the range
    current_date = datetime.datetime.strptime(start_date, "%Y-%m")
    current_end_date = datetime.datetime.strptime(end_date, "%Y-%m")
    while current_date <= current_end_date:
        # Get the kline data for the current date
        curl_endpoint(
            symbol, interval, current_date.strftime("%Y-%m"), save_path)

        # Check if end of year is reached
        if current_date.month == 12:
            # Set month to January
            current_date = datetime.datetime(
                current_date.year, 1, current_date.day)
            # Add 1 year
            current_date += datetime.timedelta(days=365)
        # if not end of year, add 1 month
        else:
            current_date += datetime.timedelta(days=31)

        print(f"Queried: {current_date}")


# Example usage:
symbol = "BTCUSDT"
interval = "5m"
start_date = "2022-12"
end_date = "2023-01"
save_path = f"./data/{symbol}/{interval}"

get_and_save_kline_data_range(
    symbol, interval, start_date, end_date, save_path)

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

    # Unzip the content of the response
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(save_path)

    # Find the csv file in the extracted files
    for filename in z.namelist():
        if filename.endswith(".csv"):
            csv_file = os.path.join(save_path, filename)
            break

    return csv_file


symbol = "BTCUSDT"
interval = "5m"
date = "2022-11"
save_path = f"newdata/{symbol}/{interval}"

test = curl_endpoint(symbol, interval, date, save_path)

testtt = 0

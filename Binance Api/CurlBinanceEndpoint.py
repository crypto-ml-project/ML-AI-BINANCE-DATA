import io
import requests
import zipfile
import csv
import os

def get_and_save_kline_data(symbol, interval, date, destination):
  # Set the base URL for the Binance Vision API
  base_url = f"https://data.binance.vision/data/spot/daily/klines/{symbol}/{interval}/{symbol}-{interval}-{date}.zip"

  # Make the request to the API
  response = requests.get(base_url)

  # Check the status code of the response to make sure the request was successful
  if response.status_code == 200:
    # Extract the kline data from the zip file
    zip_data = zipfile.ZipFile(io.BytesIO(response.content))
    kline_data = zip_data.read(f"{symbol}-{interval}-{date}.csv").decode("utf-8").split("\n")
    
    # Remove the quotation marks from the kline data
    kline_data = [row.strip('"') for row in kline_data]

    # Split the kline data into rows and columns
    kline_data = [row.split(",") for row in kline_data]

    # Create the destination folder if it does not exist
    if not os.path.exists(destination):
      os.makedirs(destination)

    # Open the file for writing
    with open(f"{destination}/{symbol}-{interval}-{date}.csv", "w", newline="") as csv_file:
      # Create a CSV writer
      writer = csv.writer(csv_file)
      # Write the data to the CSV file
      writer.writerows(kline_data)

""" # Example usage:
symbol = "RAYUSDT"
interval = "1s"
date = "2022-12-27"
destination = f"data/{symbol}/{interval}"
get_and_save_kline_data(symbol, interval, date, destination) """

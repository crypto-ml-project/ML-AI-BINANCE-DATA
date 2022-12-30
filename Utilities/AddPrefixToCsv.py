import os
import csv

def modify_csv_files(folder, id):
  # Iterate over the files in the folder
  for filename in os.listdir(folder):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
      # Open the file in read mode
      with open(os.path.join(folder, filename), 'r') as csvfile:
        # Read the contents of the file into memory
        rows = csvfile.readlines()
      # Remove the final row
      rows = rows[:-1]
      # Add the ID column to each row
      rows = [f"{id},{row}" for row in rows]
      # Open the file in write mode
      with open(os.path.join(folder, filename), 'w') as csvfile:
        # Write the modified rows back to the file
        csvfile.writelines(rows)

# Example usage:
folder = "./data/BTCUSDT"
id = 1
modify_csv_files(folder, id)

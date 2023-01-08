import csv
import os

# Set the path to the folder containing the CSV files
path = "./data/BTCUSDT/1s"

# Loop through each file in the folder
for file in os.listdir(path):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
        # Open the CSV file
        with open(os.path.join(path, file)) as f:
            # Create a CSV reader object
            reader = csv.reader(f)
            # Create a new list to store the rows that we want to keep
            rows_to_keep = []
            # Iterate through each row in the CSV file
            for i, row in enumerate(reader):
                # If the row number is a multiple of 300, add it to the list
                if i % 300 == 0:
                    rows_to_keep.append(row)
            # Close the CSV file
            f.close()

        # Open the CSV file in write mode
        with open(os.path.join(path, file), "w", newline="") as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            # Write the rows that we want to keep to the CSV file
            for row in rows_to_keep:
                writer.writerow(row)
            # Close the CSV file
            f.close()

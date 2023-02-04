import configparser
import os
import csv


def modify_csv_files(folder, id):
    # Iterate over the files in the folder
    for filename in os.listdir(folder):
        #print("Opened: " + filename)
        # Check if the file is a CSV file
        if filename.endswith(".csv"):
            # Open the file in read mode
            with open(os.path.join(folder, filename), 'r') as csvfile:
                # Read the contents of the file into memory
                rows = csvfile.readlines()
            # Remove the final row
            if rows[-1][0] != "1":
                rows = rows[:-1]
                print("Removed final row")
            # Check if the row count is not 86400
            # row_count = len(rows)
            # if row_count != 8640 and row_count != 8928 and row_count != 8064 and row_count != 8352:
            #     print(f"{filename} has {len(rows)} rows")
            #     os.remove(os.path.join(folder, filename))
            #     continue
            # Add the ID column to each row
            rows = [f"{id},{row}" for row in rows]
            # Open the file in write mode
            with open(os.path.join(folder, filename), 'w') as csvfile:
                # Write the modified rows back to the file

                csvfile.writelines(rows)


config = configparser.ConfigParser()
config.read(r'database.ini')
# Example usage:
symbol = config['postgresql']['currencySymbol']

# Example usage:
folder = f"./data/{symbol}/5m"
id = 3
modify_csv_files(folder, id)

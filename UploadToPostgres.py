import csv
import os
import psycopg2
import configparser
config = configparser.ConfigParser()
config.read(r'database.ini')

def connect_to_db(host, port, database, user, password):
    """Connect to a PostgreSQL database and return a connection object."""
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        return conn
    except psycopg2.Error as e:
        print(e)
        return None

def upload_csv_to_db(conn, table_name, file_path):
    """Upload the contents of a CSV file to a table in a PostgreSQL database."""
    try:
        # Open the CSV file for reading
        with open(file_path, 'r') as csv_file:
            # Create a cursor object
            cursor = conn.cursor()
            # Create a string of placeholders for the values in the CSV file
            placeholders = ', '.join(['%s'] * len(next(csv.reader(csv_file))))
            # Reset the file pointer to the beginning of the file
            csv_file.seek(0)
            # Execute the COPY command to insert the data from the CSV file into the table
            cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", csv_file, size=8192)
            # Commit the changes to the database
            conn.commit()
        return True
    except psycopg2.Error as e:
        print(e)
        return False

def upload_csvs_to_db(folder_path, host, port, database, user, password, table_name):
    """Loop through all CSV files in a folder structure and upload them to a PostgreSQL database."""
    # Connect to the database
    conn = connect_to_db(host, port, database, user, password)
    if conn:
        # Loop through all files in the specified folder
        for file_name in os.listdir(folder_path):
            # Check if the file is a CSV
            if file_name.endswith(".csv"):
                # Get the full path to the file
                file_path = os.path.join(folder_path, file_name)
                # Upload the CSV file to the database
                success = upload_csv_to_db(conn, table_name, file_path)
                print(f"File {file_name}: {'Success' if success else 'Failed'}")
        # Close the connection to the database
        conn.close()
    else:
        print("Unable to connect to the database.")


upload_csvs_to_db(
    "./data/BTCUSDT",
    config['postgresql']['host'],
    config['postgresql']['port'],
    config['postgresql']['database'],
    config['postgresql']['user'],
    config['postgresql']['password'],
    "historic_klines"
)

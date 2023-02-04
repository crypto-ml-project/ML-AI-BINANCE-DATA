import csv
import os
import psycopg2
import configparser
config = configparser.ConfigParser()
config.read(r'database.ini')

import csv
import psycopg2

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
    """Upload a CSV file to a table in a PostgreSQL database."""
    try:
        # Open the CSV file for reading
        with open(file_path, 'r') as csv_file:
            # Create a cursor object
            cursor = conn.cursor()
            # Execute the COPY command to insert the data from the CSV file into the table
            cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", csv_file, size=8192)
            # Commit the changes to the database
            conn.commit()
        return True
    except psycopg2.Error as e:
        print(e)
        return False

def upload_csv(file_path, host, port, database, user, password, table_name):
    """Upload a CSV file to a remote PostgreSQL database."""
    # Connect to the database
    conn = connect_to_db(host, port, database, user, password)
    if conn:
        # Upload the CSV file to the database
        success = upload_csv_to_db(conn, table_name, file_path)
        print(f"File {file_path}: {'Success' if success else 'Failed'}")
        # Close the connection to the database
        conn.close()
    else:
        print("Unable to connect to the database.")

# Example usage:
#upload_csv("/path/to/file.csv", "localhost", 5432, "mydatabase", "user", "password", "mytable")

upload_csv(
    "./data/NEARUSDT/NEARUSDT-1s-2020-10-14.csv",
    config['postgresql']['host'],
    config['postgresql']['port'],
    config['postgresql']['database'],
    config['postgresql']['user'],
    config['postgresql']['password'],
    "historic_klines"
)

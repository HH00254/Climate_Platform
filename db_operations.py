"""
Description: Weather Data Table
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Description: Weather Data Table
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Updates:
"""

import sqlite3
from dbcm import DBCM

class DBOperations:
    """Class to perform database operations"""

    def __init__(self, db_file):
        """
        Initialize DBOperations object.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_file = db_file

    def initialize_db(self):
        """
        Initializes the database.

        This method creates the necessary table if it doesn't already exist.
        """
        try:
            with DBCM(self.db_file) as cur:
                cur.execute("""
                            CREATE TABLE IF NOT EXISTS weather_data (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                sample_date TEXT NOT NULL,
                                location TEXT NOT NULL,
                                province TEXT NOT NULL,
                                min_temp REAL NOT NULL,
                                max_temp REAL NOT NULL,
                                avg_temp REAL NOT NULL,
                                UNIQUE (sample_date, location)
                            );
                            """)
        except sqlite3.Error as e:
            print("Error initializing database:", e)

    def save_data(self, data):
        """
        Save new data to the database.

        Args:
            data (tuple): A tuple containing the data to be inserted.
        """
        try:
            with DBCM(self.db_file) as cur:
                cur.execute("SELECT id FROM weather_data WHERE sample_date = ? AND location = ?;",
                             (data[0], data[1]))
                existing_data = cur.fetchone()

                if not existing_data:
                    cur.execute("""
                                INSERT INTO weather_data (sample_date, location, province, min_temp, max_temp, avg_temp)
                                VALUES (?, ?, ?, ?, ?, ?);
                                """, (data[0], data[1], data[2], data[3],
                                      data[4], data[5]))
        except sqlite3.Error as e:
            print("Error saving data to database:", e)

    def purge_data(self):
        """
        Purge all data from the database.
        """
        try:
            with DBCM(self.db_file) as cur:
                cur.execute("DELETE FROM weather_data;")
        except sqlite3.Error as e:
            print("Error purging data from database:", e)

    def fetch_data(self):
        """
        Fetch all data from the database.

        Returns:
            list: A list of tuples containing the fetched data.
        """
        try:
            with DBCM(self.db_file) as cur:
                cur.execute("SELECT * FROM weather_data;")
                return cur.fetchall()
        except sqlite3.Error as e:
            print("Error fetching data from database:", e)

    def insert_sample_data(self):
        """
        Insert sample data into the weather_data table.
        """
        sample_data = [
            {'sample_date': '2024-03-25', 'location': 'City A', 'province': 'Province A',
              'min_temp': 10.0, 'max_temp': 20.0, 'avg_temp': 15.0},
            {'sample_date': '2024-03-25', 'location': 'City B', 'province': 'Province B',
             'min_temp': 12.0, 'max_temp': 22.0, 'avg_temp': 17.0},
        ]
        try:
            for data in sample_data:
                self.save_data((
                    data['sample_date'],
                    data['location'],
                    data['province'],
                    data['min_temp'],
                    data['max_temp'],
                    data['avg_temp']
                ))
        except sqlite3.Error as e:
            print("Error inserting sample data:", e)

# Test DB
if __name__ == "__main__":
    db_operations = DBOperations("test.db")
    db_operations.initialize_db()
    db_operations.insert_sample_data()
    fetched_data = db_operations.fetch_data()
    print("Test DB data results:", fetched_data)

"""
Description: Weather Data Table
Author: Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Updates:
"""

import sqlite3
from contextlib import contextmanager

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
        with self._get_cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS weather_data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sample_date TEXT NOT NULL,
                            location TEXT NOT NULL,
                            min_temp REAL NOT NULL,
                            max_temp REAL NOT NULL,
                            avg_temp REAL NOT NULL,
                            UNIQUE (sample_date, location)
                        );
                        """)

    def save_data(self, data):
        """
        Save new data to the database.

        Args:
            data (tuple): A tuple containing the data to be inserted.
        """
        with self._get_cursor() as cur:
            cur.execute("SELECT id FROM weather_data WHERE sample_date = ? AND location = ?;",
                         (data['sample_date'], data['location']))
            existing_data = cur.fetchone()

            if not existing_data:
                cur.execute("""
                            INSERT INTO weather_data (sample_date, location, min_temp, max_temp, avg_temp)
                            VALUES (?, ?, ?, ?, ?);
                            """, (data['sample_date'], data['location'], data['min_temp'],
                                  data['max_temp'], data['avg_temp']))

    def purge_data(self):
        """
        Purge all data from the database.
        """
        with self._get_cursor() as cur:
            cur.execute("DELETE FROM weather_data;")

    def fetch_data(self):
        """
        Fetch all data from the database.

        Returns:
            list: A list of tuples containing the fetched data.
        """
        with self._get_cursor() as cur:
            cur.execute("SELECT * FROM weather_data;")
            return cur.fetchall()

    @contextmanager
    def _get_cursor(self):
        """
        Context manager to get a cursor for executing SQL queries.

        Yields:
            cursor: A cursor object.
        """
        conn = sqlite3.connect(self.db_file)
        try:
            cur = conn.cursor()
            yield cur
        finally:
            conn.commit()
            cur.close()
            conn.close()

"""
Description:
Author:
Section Number:
Date Created:
Credit:
Updates:
"""

import sqlite3
conn = sqlite3.connect("weather.sqlite")
print("Opened the database successfully.")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    sample_date TEXT UNIQUE NOT NULL,
    location TEXT NOT NULL,
    min_temp REAL NOT NULL,
    max_temp REAL NOT NULL,
    avg_temp REAL NOT NULL,
    UNIQUE (sample_date, location);""")
print("Table created successfully.")
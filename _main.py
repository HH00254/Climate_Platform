"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:
"""

from db_operations import DBOperations
import _scrape_weather

# Initialize database
db_operations = DBOperations('weather_data.sqlite')
db_operations.initialize_db()

# Run the weather data scraping process.
_scrape_weather.main()

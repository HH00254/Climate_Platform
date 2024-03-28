"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:
"""
from pprint import pprint
from time import time
from db_operations import DBOperations
import scrape_weather

def main() -> None:
    """
    Main function for the Weather Processing App.

    This function orchestrates the weather data processing workflow:
        1. Initializes database operations.
        2. Initiates web scraping to retrieve weather data.
        3. Calculates the time taken for web scraping.
        4. Prints the retrieved data.
        5. Saves the data into the SQLite database.`

    Raises:
        Any exceptions encountered during the execution.

    Returns:
        None
    """
    db_operations = DBOperations('weather_data.sqlite')
    db_operations.initialize_db()
    now = time()
    insert_values = scrape_weather.web_scrape_call()
    print('then')
    then = time()
    print(f'It took {now - then}')

    for entry in enumerate(insert_values):
        for index in range(len(insert_values[entry])):
          print(insert_values[entry][index[0]])
          db_operations.save_data(entry)

    pprint(insert_values)

if __name__ == '__main__':
    main()
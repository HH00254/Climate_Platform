from db_operations import DBOperations
import scrape_weather
from pprint import pprint
from time import time

def main() -> None:
    """
    Summary:
    - Main body were we execute our code.
    """
    db_operations = DBOperations('weather_data.sqlite')
    insert_values = scrape_weather.web_scrape_call()

    for entry in insert_values:
        db_operations.save_data(entry)

if __name__ == '__main__':
    main()
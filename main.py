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
    db_operations.initialize_db()
    db_operations.purge_data()
    insert_values = scrape_weather.web_scrape_call()

    for month_collection in insert_values:
        for row in month_collection:
            db_operations.save_data(row)

if __name__ == '__main__':
    main()
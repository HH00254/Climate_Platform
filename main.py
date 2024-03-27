from db_operations import DBOperations
import scrape_weather
from pprint import pprint
from time import time

def main() -> None:
    db_operations = DBOperations('weather_data.sqlite')
    now = time()
    insert_values = scrape_weather.web_scrape_call()
    print('then')
    then = time()
    print(f'It took {now - then}')

    pprint(insert_values)

    for entry in insert_values:
        db_operations.save_data(entry)

if __name__ == '__main__':
    main()
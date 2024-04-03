import concurrent.futures
from datetime import datetime
from time import time
from db_operations import DBOperations
from scrape_weather import ScrapeWeather

def main() -> None:
    """
    Summary:
    - Main body were we execute our code.
    """
    start = time()
    selected_time = datetime.now()
    new_scrape = ScrapeWeather(selected_time)
    insert_items = []
    year_range   = []

    range_leng = selected_time.year - new_scrape.end_year

    for subtraction_value in range(range_leng + 1):
        year_range.append(selected_time.year - subtraction_value)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results            = executor.submit(new_scrape.web_scrape_call, selected_time.year, selected_time.month)
        results_collection = [executor.submit(new_scrape.web_scrape_call, current_year, 12) for current_year in year_range ]

        for f in concurrent.futures.as_completed(results_collection):
            insert_items.append(new_scrape.get_xpath_page_values(f.result()))

        insert_items.append(new_scrape.get_xpath_page_values(results.result()))

    db_operations = DBOperations('weather_data.sqlite')
    db_operations.initialize_db()
    db_operations.purge_data()
    
    for yearr in (insert_items):
        for month in yearr:
            db_operations.save_data(month)

    end = time()
    print(f'\nCompleted in {end - start}\n')

if __name__ == '__main__':
    main()
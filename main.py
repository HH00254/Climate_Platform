import concurrent.futures
from datetime import datetime
from time import time
from db_operations import DBOperations
from scrape_weather import ScrapeWeather

# def main() -> None:
#     """
#     Summary:
#     - Main body were we execute our code.
#     """
#     start = time()
#     selected_time = datetime.now()
#     new_scrape = ScrapeWeather(selected_time)
#     insert_items = []
#     year_range   = []

#     range_leng = selected_time.year - new_scrape.end_year

#     for subtraction_value in range(range_leng + 1):
#         year_range.append(selected_time.year - subtraction_value)

#     # See if I can chuck the requests down and then check last finish item to then send more threads or STOP!    
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results            = executor.submit(new_scrape.web_scrape_call, selected_time.year, selected_time.month)
#         results_collection = [executor.submit(new_scrape.web_scrape_call, current_year, 12) for current_year in year_range]

#         for f in concurrent.futures.as_completed(results_collection):
#             insert_items.append(new_scrape.get_xpath_page_values(f.result()))

#         insert_items.append(new_scrape.get_xpath_page_values(results.result()))

#     db_operations = DBOperations('weather_data.sqlite')
#     db_operations.initialize_db()
#     db_operations.purge_data()
    
#     for year in (insert_items):
#         for month in year:
#             db_operations.save_data(month)

#     end = time()
#     print(f'\nCompleted in {end - start}\n')

# def update_weather_data() -> None:
#     insert_items = []
#     selected_time = datetime.now()
#     new_scrape = ScrapeWeather(selected_time)

#     missing_range_end = datetime(2023, 10, 1)

#     year_items = new_scrape.web_scrape_call(data_end_point=missing_range_end)

#     for month in year_items:
#         insert_items.append(new_scrape.get_xpath_page_values(month))

#     db_operations = DBOperations('weather_data.sqlite')
#     db_operations.initialize_db()
#     db_operations.purge_data()
    
#     for year in (insert_items):
#         for month in year:
#             db_operations.save_data(month)


if __name__ == '__main__':
    pass
    # main()
    # update_weather_data()
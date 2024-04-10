"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:

"""
import concurrent.futures
from datetime import datetime
from db_operations import DBOperations
from scrape_weather import ScrapeWeather
from plot_operations import PlotOperations
from prod_util import ProdUtil

class WeatherProcessor:
    """
    Handles user interaction and menu display, and calls the appropriate functions for downloading
    weather data, updating weather data, and generating plots.
    """
    def __init__(self, db_file):
        self.db_operations = DBOperations(db_file)
        self.db_operations.initialize_db()

    def start(self):
        """
        Start the weather processing application and display the main menu.
        """
        while True:
            choice = self.display_menu()
            if choice == '1':
                self.download_weather_data()
            elif choice == '2':
                self.update_weather_data()
            elif choice == '3':
                self.generate_box_plot()
            elif choice == '4':
                self.generate_line_plot()
            elif choice == '5':
                self.delete_year()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def delete_year(self):
        year = int(input("Enter the year to delete: "))
        self.db_operations.delete_data_for_year(year)

    def display_menu(self):
        """
        Display the main menu and prompt the user for their choice.

        Returns:
        - str: The user's menu choice.
        """
        print("\nMenu (1-5):")
        print("1. Download weather data")
        print("2. Update weather data")
        print("3. Generate box plot for year range")
        print("4. Generate line plot for month and year")
        print("5. Delete data from a year")
        print("6. Exit")
        return input("Enter your choice: ")

    def download_weather_data(self):
        """
        Download weather data using the scrape_weather module.
        """
        selected_time = datetime.now()
        new_scrape = ScrapeWeather(selected_time)
        insert_items = []
        year_range   = []

        range_leng = selected_time.year - int(new_scrape.end_year)

        for subtraction_value in range(range_leng + 1):
            year_range.append(selected_time.year - subtraction_value)

        # See if I can chuck the requests down
        # and then check last finish item to then send more threads or STOP!
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.submit(
                    new_scrape.web_scrape_call, selected_time.year, selected_time.month)

                results_collection = (
                    [executor.submit(new_scrape.web_scrape_call, current_year, 12)
                    for current_year in year_range])

                for f in concurrent.futures.as_completed(results_collection):
                    insert_items.append(new_scrape.get_xpath_page_values(f.result()))

                insert_items.append(new_scrape.get_xpath_page_values(results.result()))

            self.db_operations.initialize_db()
            self.db_operations.purge_data()

            for year in (insert_items):
                for month in year:
                    self.db_operations.save_data(month)

        except concurrent.futures.TimeoutError as e:
            ProdUtil.system_log(e, e.args)

        except IndexError as e:
            ProdUtil.system_log(e, e.args)

        print('\nCompleted\n')

    def update_weather_data(self):
        """
        Update weather data using the scrape_weather module.
        """
        try:
            self.db_operations.initialize_db()
            latest_date_str =  self.db_operations.get_latest_date()
            latest_date =   datetime.strptime(latest_date_str, '%Y-%m-%d')

            new_scrape = ScrapeWeather()
            year_items =  new_scrape.web_scrape_call(data_end_point=latest_date)

            insert_items = []
            for month in year_items:
                insert_items.append(new_scrape.get_xpath_page_values(month))

            for row in insert_items[0]:
                self.db_operations.save_data(row)

        except IndexError as e:
            ProdUtil.system_log(e, e.args)

    def generate_box_plot(self):
        """
        Generate a box plot for a specified year range.
        """
        start_year = int(input("Enter the start year: "))
        end_year   = int(input("Enter the end year: "))

        if end_year < start_year:
            print("Error: End year cannot be before start year.")
            return

        weather_data = self.db_operations.fetch_data_for_year_range(start_year, end_year)

        if weather_data:
            plot_operations = PlotOperations(weather_data)
            plot_operations.create_boxplot()
        else:
            print("No data found for the specified year range.")

    def generate_line_plot(self):
        """
        Generate a line plot for a specified month and year.
        """
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))

        weather_data = self.db_operations.fetch_data_for_year_and_month(year, month)

        if weather_data:
            plot_operations = PlotOperations(weather_data)
            plot_operations.create_lineplot(month, year)
        else:
            print("No data found for the specified date selection.")

if __name__ == "__main__":
    wp = WeatherProcessor("weather_data.sqlite")
    wp.start()
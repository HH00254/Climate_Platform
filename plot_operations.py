"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:
"""

import calendar
import matplotlib.pyplot as plt

class PlotOperations:
    """
    Handles plotting operations for generating box plots and line plots of weather data.

    Methods:
    - create_boxplot(): Generates a box plot for mean temperatures for each month
      of each year in the weather data.
    - create_lineplot(month, year): Generates a line plot for mean daily temperatures
      of a specified month and year.
    """
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def create_boxplot(self):
        """
        Generates a box plot for mean temperatures for each month of each year in the weather data.
        """
        # Dictionary to store mean temperatures for each year and month
        yearly_monthly_temps = {}

        #needs to be more general
        for year_data in self.weather_data:
            year = year_data[0][:4]  # Extract year from sample date (2023-12-12  returns '2023')
            month = int(year_data[0][5:7])  # Extract month from sample date (2023-12-12  returns 12)
            if year in yearly_monthly_temps:
                yearly_monthly_temps[year][month - 1].append(year_data[5])  # Append mean temperature for the month
            else:
                yearly_monthly_temps[year] = [[] for _ in range(12)]  # Initialize list with mean temperature for each month
                yearly_monthly_temps[year][month - 1].append(year_data[5])  # Append mean temperature for the month

        # Create a separate boxplot for each year
        #need to refactor so no need for loop
        for year, monthly_temps in yearly_monthly_temps.items():
            plt.figure()
            plt.boxplot(monthly_temps)
            plt.title(f'Mean Temperatures Boxplot - {year}')
            plt.xlabel('Months')
            plt.ylabel('Mean Temperature (°C)')
            plt.xticks(range(1, 13), [str(i) for i in range(1, 13)])  # Set x-axis labels to the months
            plt.show()

    def create_lineplot(self, month, year):
        """
        Generates a line plot for mean daily temperatures of a specified month and year.

        Args:
        - month (int): The month for which to generate the line plot.
        - year (int): The year for which to generate the line plot.
        """
        monthly_weather_data = [data for data in self.weather_data if str(data[0]).startswith(f"{year}-{month:02}")]

        # Create a list to store mean temperatures for each day of the selected month
        daily_temperatures = []

        # Calculate the number of days in the selected month
        num_days_in_month = calendar.monthrange(year, month)[1]

        # Iterate over each day of the month
        for day in range(1, num_days_in_month + 1):
            # Filter the weather data for the current day
            day_data = [data for data in monthly_weather_data if str(data[0]).startswith(f"{year}-{month:02}-{day:02}")]

            # If data is available for the current day, calculate the mean temperature
            if day_data:
                # Calculate the mean temperature for the current day
                mean_temp = sum(data[5] for data in day_data) / len(day_data)
                # Append the mean temperature to the daily_temperatures list
                daily_temperatures.append(mean_temp)
            else:
                # If no data is available for the current day, append None to maintain the day-to-day mapping
                daily_temperatures.append(None)

        # Plot the line plot
        plt.figure()
        plt.plot(range(1, num_days_in_month + 1), daily_temperatures, marker='o')
        plt.title(f'Mean Daily Temperatures Lineplot - {calendar.month_name[month]} {year}')
        plt.xlabel('Day')
        plt.ylabel('Mean Temperature (°C)')
        plt.xticks(range(1, num_days_in_month + 1))  # Set x-axis ticks to show the days of the month
        plt.grid(True)
        plt.show()
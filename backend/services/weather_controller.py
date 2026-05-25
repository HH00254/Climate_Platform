"""
Description: Weather API Service
Author: Al Hochbaum
"""

from backend.database.db_operations import DBOperations

from backend.services.scrape_weather import ScrapeWeather

from backend.services.plot_operations import PlotOperations

from backend.models.location import Location

from backend.models.weather_record import WeatherRecord

class WeatherProcessor:
    """
    Summary:
    - Coordinates weather services
      and database operations.
    """

    def __init__(self):

        self.db_operations = (
            DBOperations()
        )

    def download_weather_data(self):
        """
        Summary:
        - Downloads all weather data
          and stores it using Django ORM.
        """

        scraper = ScrapeWeather()

        weather_rows = (

            scraper.download_all_weather_data()

        )

        location, _ = (

            Location.objects.get_or_create(

                city="Winnipeg",

                province="Manitoba",

                station_id=27174

            )

        )

        for row in weather_rows:

            WeatherRecord.objects.update_or_create(

                sample_date=row[
                    "sample_date"
                ],

                defaults={

                    "location": location,

                    "min_temp": row[
                        "min_temp"
                    ],

                    "max_temp": row[
                        "max_temp"
                    ],

                    "avg_temp": row[
                        "avg_temp"
                    ]

                }

            )

        print(
            f"\nTOTAL SAVED: "
            f"{len(weather_rows)}\n"
        )

    def generate_box_plot(
            self,
            start_year,
            end_year):
        """
        Summary:
        - Generates a box plot for average
          monthly temperatures over a year range.
        
        Args:
        - start_year: Starting year (inclusive).
        - end_year: Ending year (inclusive).
        """

        weather_data = (

            self.db_operations
            .fetch_data_for_year_range(

                start_year,
                end_year

            )

        )

        plot_operations = PlotOperations(
            weather_data
        )

        plot_operations.create_boxplot()

    def generate_line_plot(
            self,
            month,
            year):
        """
        Summary:
            - Generates a line plot for daily temperatures in a specific month/year.
          Args:
            - month: Month (1-12)
            - year: Year (e.g., 2020)
            """

        weather_data = (

            self.db_operations
            .fetch_data_for_year_and_month(

                year,
                month

            )

        )

        plot_operations = PlotOperations(
            weather_data
        )

        plot_operations.create_lineplot(
            month,
            year
        )
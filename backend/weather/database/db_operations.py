"""
Description: Database Operations
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
"""

from weather.model_definitions import (
    Location,
    WeatherRecord
)

class DBOperations:
    """
    Summary:
    - Handles database operations
      using the Django ORM.

    Features:
    - Save weather records
    - Fetch weather records
    - Delete weather records
    - Retrieve latest weather date
    """

    def __init__(self):
        """
        Initialize DBOperations.
        """

        print(
            "\nDJANGO ORM INITIALIZED\n"
        )

    def initialize_db(self):
        """
        Summary:
        - Placeholder method.

        Notes:
        - Django handles table creation
          automatically through migrations.
        """

        print(
            "\nDATABASE MANAGED "
            "BY DJANGO MIGRATIONS\n"
        )

    def purge_data(self):
        """
        Summary:
        - Deletes all weather data.
        """

        deleted_count, _ = (
            WeatherRecord.objects.all().delete()
        )

        print(
            f"\nPURGED ROWS: "
            f"{deleted_count}\n"
        )

    def save_data(
            self,
            weather_record):
        """
        Summary:
        - Saves or updates a weather record.

        Args:
        - weather_record:
            WeatherRecord domain object.
        """

        try:

            print(
                f"\nATTEMPTING INSERT:\n"
                f"{weather_record}\n"
            )

            # =====================================
            # GET OR CREATE LOCATION
            # =====================================

            location, _ = (

                Location.objects.get_or_create(

                    city=weather_record.location.city,

                    province=weather_record.location.province,

                    station_id=weather_record.location.station_id

                )

            )

            # =====================================
            # INSERT OR UPDATE WEATHER RECORD
            # =====================================

            WeatherRecord.objects.update_or_create(

                sample_date=weather_record.sample_date,

                defaults={

                    "location": location,

                    "min_temp": weather_record.min_temp,

                    "max_temp": weather_record.max_temp,

                    "avg_temp": weather_record.avg_temp

                }

            )

            print(
                f"\nINSERTED: "
                f"{weather_record.sample_date}\n"
            )

        except Exception as e:

            print(
                f"\nINSERT ERROR: "
                f"{e}\n"
            )

    def fetch_all(self):
        """
        Summary:
        - Fetch all weather records.

        Return:
        - QuerySet:
            All WeatherRecord objects.
        """

        weather_records = (
            WeatherRecord.objects.all()
        )

        print(
            f"\nFETCHED ROWS: "
            f"{weather_records.count()}\n"
        )

        return weather_records

    def get_latest_date(self):
        """
        Summary:
        - Retrieves the latest
          sample date in the database.

        Return:
        - date | None
        """

        latest_record = (

            WeatherRecord.objects.order_by(
                "-sample_date"
            ).first()

        )

        if latest_record:

            print(
                f"\nLATEST DATE: "
                f"{latest_record.sample_date}\n"
            )

            return latest_record.sample_date

        print(
            "\nNO WEATHER RECORDS FOUND\n"
        )

        return None

    def delete_data_for_year(
            self,
            year):
        """
        Summary:
        - Deletes weather data
          for a specific year.

        Args:
        - year (int)
        """

        deleted_count, _ = (

            WeatherRecord.objects.filter(

                sample_date__year=year

            ).delete()

        )

        print(
            f"\nDELETED ROWS: "
            f"{deleted_count}\n"
        )

    def fetch_data_for_year_range(
            self,
            start_year,
            end_year):
        """
        Summary:
        - Retrieves weather data
          between a year range.

        Args:
        - start_year (int)
        - end_year (int)

        Return:
        - QuerySet
        """

        weather_records = (

            WeatherRecord.objects.filter(

                sample_date__year__gte=start_year,

                sample_date__year__lte=end_year

            ).order_by(
                "sample_date"
            )

        )

        print(
            f"\nYEAR RANGE ROWS: "
            f"{weather_records.count()}\n"
        )

        return weather_records

    def fetch_data_for_year_and_month(
            self,
            year,
            month):
        """
        Summary:
        - Retrieves weather data
          for a specific month/year.

        Args:
        - year (int)
        - month (int)

        Return:
        - QuerySet
        """

        weather_records = (

            WeatherRecord.objects.filter(

                sample_date__year=year,

                sample_date__month=month

            ).order_by(
                "sample_date"
            )

        )

        print(
            f"\nMONTH ROWS: "
            f"{weather_records.count()}\n"
        )

        return weather_records
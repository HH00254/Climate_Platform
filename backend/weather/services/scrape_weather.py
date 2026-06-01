"""
Description:
- Environment Canada weather ingestion service.

Responsibilities:
1. Build download URLs for a weather station.
2. Download monthly CSV weather files.
3. Parse CSV data safely.
4. Convert raw text values into Python types.
5. Save or update WeatherRecord objects.

This service follows an ETL pattern:

Extract:
    Download CSV data from Environment Canada.

Transform:
    Clean dates, numbers, and missing values.

Load:
    Store records in the database.
"""


import csv
import requests

from datetime import datetime

from weather.models import WeatherRecord


class ScrapeWeather:
    """
    Summary:
    - Service responsible for importing weather data.

    One ScrapeWeather instance represents
    one Environment Canada station.

    Example:
        ScrapeWeather(27174)

    Represents:
        WINNIPEG A CS
    """


    def __init__(
            self,
            station_id):

        self.station_id = station_id

        self.base_url = (
            "https://climate.weather.gc.ca/"
            "climate_data/bulk_data_e.html"
        )


    def build_url(
            self,
            year,
            month):
        """
        Summary:
        - Builds the Environment Canada CSV URL.
        """

        return (
            f"{self.base_url}"
            f"?format=csv"
            f"&stationID={self.station_id}"
            f"&Year={year}"
            f"&Month={month}"
            f"&Day=14"
            f"&timeframe=2"
        )


    def download_year(
            self,
            location,
            year):
        """
        Summary:
        - Controls the yearly import workflow.

        Process:
        1. Check if data exists.
        2. Download missing CSV files.
        3. Locate weather data.
        4. Convert CSV columns.
        5. Save records.
        """

        for month in range(1, 13):

            if self.month_exists(
                location,
                year,
                month
            ):

                print(
                    f"{year}-{month}: skipped"
                )

                continue


            print(
                f"Downloading {year}-{month}"
            )


            rows = self.download_csv(
                year,
                month
            )


            if not rows:

                continue


            headers = self.find_headers(
                rows
            )


            if not headers:

                print(
                    f"{year}-{month}: no data"
                )

                continue


            columns = self.build_columns(
                headers
            )


            start_index = (
                rows.index(headers)
                +
                1
            )


            for row in rows[start_index:]:

                self.save_record(
                    location,
                    row,
                    columns
                )


    def month_exists(
            self,
            location,
            year,
            month):
        """
        Summary:
        - Checks if a month already exists.

        We check total_precipitation because
        older imports may contain incomplete rows.

        28 records are used because February
        is the shortest complete month.
        """

        records = (
            WeatherRecord.objects.filter(
                location=location,
                recorded_date__year=year,
                recorded_date__month=month,
                total_precipitation__isnull=False
            )
            .count()
        )

        return records >= 28


    def download_csv(
            self,
            year,
            month):
        """
        Summary:
        - Downloads CSV data and converts
          it into Python rows.
        """

        response = requests.get(
            self.build_url(
                year,
                month
            )
        )

        response.raise_for_status()

        return list(
            csv.reader(
                response.text.splitlines()
            )
        )


    def find_headers(
            self,
            rows):
        """
        Summary:
        - Finds where the real weather table starts.

        Environment Canada includes metadata:

            Station Name
            Latitude
            Longitude

        before:

            Date/Time, Temp, Rain...
        """

        for row in rows:

            for column in row:

                if "Date/Time" in column:

                    return row


        return None


    def build_columns(
            self,
            headers):
        """
        Summary:
        - Maps CSV headers to internal names.
        """

        return {

            "date":
                self.get_column_index(
                    headers,
                    "Date/Time"
                ),

            "max_temp":
                self.get_column_index(
                    headers,
                    "Max Temp"
                ),

            "min_temp":
                self.get_column_index(
                    headers,
                    "Min Temp"
                ),

            "mean_temp":
                self.get_column_index(
                    headers,
                    "Mean Temp"
                ),

            "rain":
                self.get_column_index(
                    headers,
                    "Total Rain"
                ),

            "snow":
                self.get_column_index(
                    headers,
                    "Total Snow"
                ),

            "precipitation":
                self.get_column_index(
                    headers,
                    "Total Precip"
                ),

            "snow_ground":
                self.get_column_index(
                    headers,
                    "Snow on Grnd"
                ),

            "wind":
                self.get_column_index(
                    headers,
                    "Spd of Max Gust"
                ),
        }


    def get_column_index(
            self,
            headers,
            search):
        """
        Summary:
        - Finds CSV columns dynamically.

        Avoids hard coded indexes:

            row[5]

        because column ordering can change.
        """

        for index, header in enumerate(headers):

            if search.lower() in header.lower():

                return index


        return None


    def get_value(
            self,
            row,
            columns,
            field):
        """
        Summary:
        - Safely converts CSV strings.

        Examples:

            "12.5" -> 12.5

            "" -> None
        """

        index = columns.get(
            field
        )


        if index is None:

            return None


        try:

            value = (
                row[index]
                .strip()
            )


            if value == "":

                return None


            return float(
                value
            )


        except Exception:

            return None


    def save_record(
            self,
            location,
            row,
            columns):
        """
        Summary:
        - Creates or updates WeatherRecord rows.

        update_or_create makes this importer
        idempotent.

        Meaning:

        Run once:
            creates data

        Run again:
            updates existing data

        No duplicate records.
        """

        try:

            recorded_date = (
                datetime.strptime(
                    row[
                        columns[
                            "date"
                        ]
                    ],
                    "%Y-%m-%d"
                )
                .date()
            )


        except Exception:

            return


        WeatherRecord.objects.update_or_create(

            location=location,

            recorded_date=recorded_date,

            defaults={

                "max_temperature":
                    self.get_value(
                        row,
                        columns,
                        "max_temp"
                    ),

                "min_temperature":
                    self.get_value(
                        row,
                        columns,
                        "min_temp"
                    ),

                "mean_temperature":
                    self.get_value(
                        row,
                        columns,
                        "mean_temp"
                    ),

                "total_rain":
                    self.get_value(
                        row,
                        columns,
                        "rain"
                    ),

                "total_snow":
                    self.get_value(
                        row,
                        columns,
                        "snow"
                    ),

                "total_precipitation":
                    self.get_value(
                        row,
                        columns,
                        "precipitation"
                    ),

                "snow_on_ground":
                    self.get_value(
                        row,
                        columns,
                        "snow_ground"
                    ),

                "max_wind_speed":
                    self.get_value(
                        row,
                        columns,
                        "wind"
                    ),
            }
        )
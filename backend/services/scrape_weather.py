"""
Description: Weather Scraper
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
"""

from datetime import datetime

import requests
import csv

from io import StringIO


class ScrapeWeather:
    """
    Summary:
    - Downloads and parses weather
      data from Environment Canada.
    """

    def __init__(self):

        self.station_id = 27174

    def web_scrape_call(
            self,
            year,
            month):

        try:

            url = (

                "https://climate.weather.gc.ca/"
                "climate_data/bulk_data_e.html?"

                "format=csv"

                f"&stationID={self.station_id}"

                f"&Year={year}"

                f"&Month={month}"

                "&Day=1"

                "&timeframe=2"

                "&submit=Download+Data"

            )

            print(
                f"\nREQUEST URL:\n{url}\n"
            )

            response = requests.get(
                url
            )

            if response.status_code != 200:

                raise Exception(
                    "FAILED TO DOWNLOAD CSV"
                )

            csv_reader = csv.reader(

                StringIO(
                    response.text
                )

            )

            rows = list(csv_reader)

            header_index = None

            for i, row in enumerate(rows):

                if "Date/Time" in row:

                    header_index = i

                    break

            if header_index is None:

                return None

            headers = rows[header_index]

            date_index = headers.index(
                "Date/Time"
            )

            max_index = headers.index(
                "Max Temp (°C)"
            )

            min_index = headers.index(
                "Min Temp (°C)"
            )

            mean_index = headers.index(
                "Mean Temp (°C)"
            )

            parsed_rows = []

            for row in rows[header_index + 1:]:

                try:

                    if len(row) <= mean_index:

                        continue

                    sample_date = row[
                        date_index
                    ].strip()

                    max_temp = row[
                        max_index
                    ].strip()

                    min_temp = row[
                        min_index
                    ].strip()

                    mean_temp = row[
                        mean_index
                    ].strip()

                    if (

                        not sample_date
                        or
                        not max_temp
                        or
                        not min_temp
                        or
                        not mean_temp

                    ):

                        continue

                    parsed_rows.append({

                        "sample_date": sample_date,

                        "max_temp": float(max_temp),

                        "min_temp": float(min_temp),

                        "avg_temp": float(mean_temp)

                    })

                except Exception as e:

                    print(
                        f"\nROW PARSE ERROR: "
                        f"{e}\n"
                    )

            return parsed_rows

        except Exception as e:

            print(
                f"\nSCRAPER ERROR: "
                f"{e}\n"
            )

            return []

    def download_all_weather_data(self):
        """
        Summary:
        - Iterates through years and months,
          downloading and parsing weather data
          until 5 consecutive years have no data.
          Return: List[Dict[str, Union[str, float]]]
        """
        all_weather_rows = []

        current_year = datetime.now().year

        no_data_counter = 0

        for year in range(
                current_year,
                1800,
                -1):

            print(
                f"\nPROCESSING YEAR: "
                f"{year}\n"
            )

            year_had_data = False

            for month in range(1, 13):

                parsed_rows = self.web_scrape_call(
                    year,
                    month
                )

                if parsed_rows:

                    year_had_data = True

                    all_weather_rows.extend(
                        parsed_rows
                    )

            if not year_had_data:

                no_data_counter += 1

            else:

                no_data_counter = 0

            if no_data_counter >= 5:

                break

        return all_weather_rows
"""
Description:
- Imports Environment Canada daily weather data.
"""


import csv
import requests


from datetime import (
    datetime
)


from weather.models import (
    WeatherRecord
)




class ScrapeWeather:
    """
    Summary:
    - Downloads and stores Environment Canada weather data.
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


        for month in range(
                1,
                13):


            existing_records = (

                WeatherRecord.objects.filter(

                    location=location,

                    recorded_date__year=year,

                    recorded_date__month=month,

                    total_precipitation__isnull=False

                )
                .count()

            )



            if existing_records >= 28:


                print(
                    f"{year}-{month}: skipped"
                )


                continue





            print(
                f"Downloading {year}-{month}"
            )



            response = requests.get(

                self.build_url(
                    year,
                    month
                )

            )


            response.raise_for_status()




            rows = list(

                csv.reader(

                    response.text.splitlines()

                )

            )



            if not rows:


                continue






            headers = None



            for row in rows:


                for column in row:


                    if (

                        "Date/Time"

                        in

                        column

                    ):


                        headers = row


                        break



                if headers:


                    break






            if not headers:


                print(
                    f"{year}-{month}: no weather data"
                )


                continue






            start_index = (

                rows.index(
                    headers
                )

                +

                1

            )







            def get_index(
                    search):


                for index, header in enumerate(
                        headers):


                    if (

                        search.lower()

                        in

                        header.lower()

                    ):


                        return index



                return None







            columns = {


                "date":
                    get_index(
                        "Date/Time"
                    ),


                "max_temp":
                    get_index(
                        "Max Temp"
                    ),


                "min_temp":
                    get_index(
                        "Min Temp"
                    ),


                "mean_temp":
                    get_index(
                        "Mean Temp"
                    ),


                "rain":
                    get_index(
                        "Total Rain"
                    ),


                "snow":
                    get_index(
                        "Total Snow"
                    ),


                "precipitation":
                    get_index(
                        "Total Precip"
                    ),


                "snow_ground":
                    get_index(
                        "Snow on Grnd"
                    ),


                "wind":
                    get_index(
                        "Spd of Max Gust"
                    ),

            }








            def get_value(
                    row,
                    field):


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








            for row in rows[
                start_index:
            ]:



                if not row:


                    continue





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


                    continue








                WeatherRecord.objects.update_or_create(


                    location=location,


                    recorded_date=recorded_date,


                    defaults={


                        "max_temperature":
                            get_value(
                                row,
                                "max_temp"
                            ),



                        "min_temperature":
                            get_value(
                                row,
                                "min_temp"
                            ),



                        "mean_temperature":
                            get_value(
                                row,
                                "mean_temp"
                            ),



                        "total_rain":
                            get_value(
                                row,
                                "rain"
                            ),



                        "total_snow":
                            get_value(
                                row,
                                "snow"
                            ),



                        "total_precipitation":
                            get_value(
                                row,
                                "precipitation"
                            ),



                        "snow_on_ground":
                            get_value(
                                row,
                                "snow_ground"
                            ),



                        "max_wind_speed":
                            get_value(
                                row,
                                "wind"
                            ),

                    }

                )
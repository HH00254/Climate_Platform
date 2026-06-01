"""
Description:
- Climate calculations used by AI.
"""


from django.db.models import (
    Avg,
    Sum
)


from weather.models import (
    WeatherRecord
)




class ClimateAnalysis:
    """
    Summary:
    - Analyzes stored weather data.
    """



    def precipitation_summary(
            self,
            station_id,
            year):
        """
        Summary:
        - Returns yearly precipitation
          and temperature information.
        """


        result = (

            WeatherRecord.objects.filter(

                location__station_id=station_id,

                recorded_date__year=year

            )
            .aggregate(


                total_precipitation=
                    Sum(
                        "total_precipitation"
                    ),


                average_temperature=
                    Avg(
                        "mean_temperature"
                    ),


                average_snow_depth=
                    Avg(
                        "snow_on_ground"
                    )

            )

        )



        return {

            "station_id":
                station_id,


            "year":
                year,


            "precipitation_mm":
                result[
                    "total_precipitation"
                ],


            "average_temperature":
                result[
                    "average_temperature"
                ],


            "average_snow_depth_cm":
                result[
                    "average_snow_depth"
                ],

        }
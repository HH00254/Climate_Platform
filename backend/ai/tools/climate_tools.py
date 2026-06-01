"""
Summary:
- Climate tools available to AI.
"""


from weather.services.climate_analysis import (
    ClimateAnalysis
)


class ClimateTools:
    """
    Summary:
    - Provides climate functions
      available to AI.
    """



    def get_precipitation(
            self,
            station_id,
            year):


        return (

            ClimateAnalysis()
            .precipitation_summary(

                station_id=station_id,

                year=year

            )

        )
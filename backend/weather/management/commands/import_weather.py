"""
Description:
- Management command to import
  Environment Canada weather data.
"""

from datetime import datetime


from django.core.management.base import (
    BaseCommand
)


from weather.models import (
    Location
)


from weather.services.scrape_weather import (
    ScrapeWeather
)


class Command(BaseCommand):
    """
    Summary:
    - Imports historical weather data
      for a selected station.
    """


    help = (
        "Imports weather data for a station"
    )



    def add_arguments(
            self,
            parser):
        """
        Summary:
        - Defines CLI arguments.
        """


        parser.add_argument(

            "--station",

            type=int,

            required=True,

            help=(
                "Environment Canada "
                "station id"
            )

        )


        parser.add_argument(

            "--years",

            type=int,

            default=10,

            help=(
                "Number of years "
                "to import"
            )

        )



    def handle(
            self,
            *args,
            **options):
        """
        Summary:
        - Executes weather import.
        """


        station_id = options[
            "station"
        ]


        years = options[
            "years"
        ]



        try:

            location = (

                Location.objects.get(
                    station_id=station_id
                )

            )


        except Location.DoesNotExist:


            self.stdout.write(

                self.style.ERROR(

                    f"Station {station_id} "
                    "does not exist."

                )

            )


            return



        scraper = ScrapeWeather(

            station_id=station_id

        )



        current_year = (

            datetime
            .now()
            .year

        )



        start_year = (

            current_year
            -
            years

        )



        for year in range(

                start_year,

                current_year + 1):


            self.stdout.write(

                f"Importing {year}"

            )



            scraper.download_year(

                location=location,

                year=year

            )



        self.stdout.write(

            self.style.SUCCESS(

                "Weather import complete"

            )

        )
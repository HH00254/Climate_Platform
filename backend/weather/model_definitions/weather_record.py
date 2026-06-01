"""
Description:
- Weather record model.
"""


from django.db import models


from weather.model_definitions.location import (
    Location
)




class WeatherRecord(models.Model):
    """
    Summary:
    - Daily climate information.
    """


    location = models.ForeignKey(

        Location,

        on_delete=models.CASCADE,

        related_name="weather_records"

    )


    recorded_date = models.DateField()



    max_temperature = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        null=True,

        blank=True

    )


    min_temperature = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        null=True,

        blank=True

    )


    mean_temperature = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        null=True,

        blank=True

    )


    total_rain = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )


    total_snow = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )


    total_precipitation = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )


    snow_on_ground = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )


    max_wind_speed = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    updated_at = models.DateTimeField(

        auto_now=True

    )



    class Meta:

        ordering = [

            "-recorded_date"

        ]


        constraints = [

            models.UniqueConstraint(

                fields=[

                    "location",

                    "recorded_date"

                ],

                name="unique_station_daily_record"

            )

        ]



    def __str__(self):

        return (

            f"{self.location.station_name} | "

            f"{self.recorded_date} | "

            f"{self.mean_temperature}°C | "

            f"{self.total_precipitation} mm"

        )
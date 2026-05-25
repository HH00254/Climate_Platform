"""
Description: Django Weather Record Model
Author: Al Hochbaum
"""

from django.db import models

class WeatherRecord(models.Model):
    """
    Summary:
    - Stores historical weather data.
    """

    sample_date = models.DateField(
        unique=True
    )

    location = models.ForeignKey(

        "weather.location",

        on_delete=models.CASCADE,

        related_name="weather_records"

    )

    min_temp = models.FloatField(
        null=True,
        blank=True
    )

    max_temp = models.FloatField(
        null=True,
        blank=True
    )

    avg_temp = models.FloatField(
        null=True,
        blank=True
    )

    class Meta:
        """
        Summary:
        - Django model configuration.
        """

        ordering = [
            "sample_date"
        ]

        verbose_name = (
            "Weather Record"
        )

        verbose_name_plural = (
            "Weather Records"
        )

    def __str__(self):
        """
        Summary:
        - String representation
          of weather record.
        """

        return (
            f"{self.sample_date} | "
            f"{self.location} | "
            f"AVG: {self.avg_temp}°C"
        )
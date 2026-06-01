"""
Summary:
- Stores Environment Canada weather stations.
"""

from django.db import models


class Location(models.Model):
    """
    Summary:
    - Represents a weather station/location.
    """

    station_id = models.IntegerField(
        unique=True
    )

    station_name = models.CharField(
        max_length=150
    )

    province = models.CharField(
        max_length=50
    )

    climate_identifier = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    elevation = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    first_year = models.IntegerField(
        null=True,
        blank=True
    )

    last_year = models.IntegerField(
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
        """
        Summary:
        - Django configuration for Location.
        """

        ordering = [
            "province",
            "station_name"
        ]

        verbose_name = (
            "Weather Station"
        )

        verbose_name_plural = (
            "Weather Stations"
        )

        indexes = [
            models.Index(
                fields=[
                    "station_id"
                ]
            ),

            models.Index(
                fields=[
                    "province"
                ]
            )
        ]


    def __str__(self):
        """
        Summary:
        - String representation.
        """

        return (
            f"{self.station_name} "
            f"{self.station_id}"
            f"({self.province})"
        )
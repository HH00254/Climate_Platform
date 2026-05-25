"""
Description: Django Weather Models
Author: Al Hochbaum
"""

from multiprocessing.managers import BaseManager

from django.db import models

@BaseManager 
class Location(models.Model):
    """
    Summary:
    - Stores weather station
      location information.
    """

    city = models.CharField(
        max_length=100
    )

    province = models.CharField(
        max_length=100
    )

    station_id = models.IntegerField(
        unique=True
    )

    class Meta:
        """
        Summary:
        - Django model configuration.
        """

        ordering = [
            "province",
            "city"
        ]

        verbose_name = "Location"

        verbose_name_plural = "Locations"

    def __str__(self):
        """
        Summary:
        - String representation
          of the location.
        """

        return (
            f"{self.city}, "
            f"{self.province}"
        )
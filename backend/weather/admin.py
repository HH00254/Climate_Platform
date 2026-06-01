"""
Summary:
- Django admin configuration for weather app.
"""

from django.contrib import admin

from weather.models import (
    Location,
    WeatherRecord
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Summary:
    - Admin settings for weather stations.
    """

    list_display = [
        "station_id",
        "station_name",
        "province",
        "first_year",
        "last_year",
    ]


    list_filter = [
        "province",
    ]


    search_fields = [
        "station_name",
        "station_id",
        "climate_identifier",
    ]


    ordering = [
        "province",
        "station_name",
    ]


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    """
    Summary:
    - Admin settings for weather records.
    """

    list_display = [
        "location",
        "recorded_date",
        "max_temperature",
        "min_temperature",
        "mean_temperature",
    ]


    list_filter = [
        "recorded_date",
        "location__province",
    ]


    search_fields = [
        "location__station_name",
        "location__station_id",
    ]


    ordering = [
        "-recorded_date",
    ]
"""
Summary:
- Serializers for weather application.
"""

from rest_framework import serializers

from weather.models import (
    Location,
    WeatherRecord
)


class LocationSerializer(serializers.ModelSerializer):
    """
    Summary:
    - Serializer for weather stations.
    """

    class Meta:
        """
        Summary:
        - Serializer configuration.
        """

        model = Location

        fields = [
            "id",
            "station_id",
            "station_name",
            "province",
            "latitude",
            "longitude",
            "elevation",
            "climate_identifier",
            "first_year",
            "last_year",
        ]


class WeatherRecordSerializer(serializers.ModelSerializer):
    """
    Summary:
    - Serializer for daily weather records.
    """

    station = serializers.CharField(
        source="location.station_name",
        read_only=True
    )


    class Meta:
        """
        Summary:
        - Serializer configuration.
        """

        model = WeatherRecord

        fields = [
            "id",
            "location",
            "station",
            "recorded_date",
            "max_temperature",
            "min_temperature",
            "mean_temperature",
            "total_rain",
            "total_snow",
            "total_precipitation",
        ]
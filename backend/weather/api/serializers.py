from rest_framework import serializers

from weather.model_definitions.location import Location  # pyright: ignore[reportMissingImports]

from weather.model_definitions.weather_record import WeatherRecord  # pyright: ignore[reportMissingImports]

class LocationSerializer(serializers.ModelSerializer):
    """
    Summary:
    - Serializer for Location model.
    """

    class Meta:
        """
        Summary:
        - Configuration for Location serializer.
        """

        model = Location

        fields = [
            "id",
            "city",
            "province",
            "station_id"
        ]

class WeatherRecordSerializer(serializers.ModelSerializer):
    """
    Summary:
    - Serializer for WeatherRecord model.
    """

    location = LocationSerializer(
        read_only=True
    )

    class Meta:
        """
        Summary:
        - Configuration for WeatherRecord serializer.
        """

        model = WeatherRecord

        fields = [
            "id",
            "sample_date",
            "location",
            "min_temp",
            "max_temp",
            "avg_temp"
        ]

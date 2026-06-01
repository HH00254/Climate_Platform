"""
Summary:
- Weather API views.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from weather.models import (
    Location,
    WeatherRecord
)

from weather.api.serializers import (
    LocationSerializer,
    WeatherRecordSerializer
)


class LocationsView(APIView):
    """
    Summary:
    - Handles weather stations.
    """

    def get(self, request):

        locations = Location.objects.all()

        serializer = LocationSerializer(
            locations,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class LocationView(APIView):
    """
    Summary:
    - Handles weather stations.
    """

    def get(
            self,
            request,
            station_id):


        location = Location.objects.get(
            station_id=station_id
        )


        serializer = LocationSerializer(
            location
        )


        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class WeatherRecordView(APIView):
    """
    Summary:
    - Handles weather records.
    """

    def get(
            self,
            request,
            station_id):

        records = WeatherRecord.objects.filter(
            location__station_id=station_id
        )


        serializer = WeatherRecordSerializer(
            records,
            many=True
        )


        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )



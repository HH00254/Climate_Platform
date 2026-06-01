from django.urls import path

from weather.api.views import (
    LocationView,
    LocationsView,
    WeatherRecordView
)

urlpatterns = [
    
    path(
        "stations/<int:station_id>/",
        LocationView.as_view(),
        name="station-detail"
    ),

    path(
        "stations/",
        LocationsView.as_view(),
        name="stations"
    ),

    path(
        "stations/<int:station_id>/weather/",
        WeatherRecordView.as_view(),
        name="station-weather"
    ),
]
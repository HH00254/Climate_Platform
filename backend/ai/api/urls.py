from django.urls import path

from ai.api.views import (
    ClimateAssistantView
)


urlpatterns = [

    path(
        "ask/",
        ClimateAssistantView.as_view(),
        name="ask-ai"
    ),

]
from rest_framework.views import APIView
from rest_framework.response import Response

from ai.services.assistant import (
    ClimateAssistant
)


class ClimateAssistantView(APIView):
    """
    Summary:
    - AI question endpoint.
    """


    def post(
            self,
            request):


        question = request.data.get(
            "question"
        )


        answer = (
            ClimateAssistant()
            .ask(
                question
            )
        )


        return Response(
            {
                "answer": answer
            }
        )
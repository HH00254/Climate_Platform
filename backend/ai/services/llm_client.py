"""
Summary:
- Handles communication with OpenAI LLM.
"""

from openai import OpenAI

from django.conf import settings


class LLMClient:
    """
    Summary:
    - Wrapper around OpenAI client.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )


    def ask(
            self,
            prompt):
        """
        Summary:
        - Sends prompt to LLM.
        """

        response = self.client.chat.completions.create(

            model="gpt-5.1",

            messages=[

                {
                    "role": "system",

                    "content": (
                        "You are a climate data analyst. "
                        "Answer questions using provided "
                        "weather and climate data. "
                        "Do not make up measurements."
                    )
                },


                {
                    "role": "user",

                    "content": prompt
                }

            ]

        )


        return (
            response
            .choices[0]
            .message
            .content
        )
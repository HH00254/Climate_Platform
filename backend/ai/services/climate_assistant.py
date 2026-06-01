"""
Summary:
- Climate AI assistant.
"""


from ai.services.llm_client import (
    LLMClient
)


from ai.tools.climate_tools import (
    ClimateTools
)




class ClimateAssistant:
    """
    Summary:
    - Creates climate prompts
      for the LLM.
    """



    def ask(
            self,
            question,
            station_id,
            year):


        climate_data = (

            ClimateTools()
                    .get_precipitation(

                station_id,

                year

            )

        )



        prompt = f"""
You are a climate data assistant.

Use the provided Environment Canada
weather station data to answer.

Do not invent measurements.

Explain possible relationships between:
- precipitation
- snowpack
- temperature
- drought
- water levels
- forest fires
- dry seasons


User question:

{question}


Weather station data:

{climate_data}
"""


        return (

            LLMClient()
            .ask(

                prompt

            )

        )
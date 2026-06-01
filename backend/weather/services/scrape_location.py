"""
Description:
- Imports Environment Canada weather stations.
"""

import requests

from weather.models import Location


class LocationImporter:
    """
    Summary:
    - Downloads Environment Canada stations.
    """

    def __init__(self):
        """
        Summary:
        - Initialize Environment Canada API URL.
        """

        self.url = (
            "https://api.weather.gc.ca/"
            "collections/climate-stations/items"
            "?lang=en"
            "&limit=10000"
        )


    def download_locations(self):
        """
        Summary:
        - Calls Environment Canada API.
        """

        response = requests.get(
            self.url
        )

        response.raise_for_status()

        return response.json()


    def get_year(
            self,
            value):
        """
        Summary:
        - Extracts year from API date string.
        """

        if not value:

            return None


        return int(
            value[:4]
        )


    def convert_coordinate(
            self,
            value):
        """
        Summary:
        - Converts Environment Canada coordinates.
        """

        if not value:

            return None


        return (
            float(value)
            /
            10000000
        )


    def import_locations(self):
        """
        Summary:
        - Inserts or updates stations.
        """

        data = self.download_locations()


        count = 0


        for station in data[
            "features"
        ]:


            properties = station[
                "properties"
            ]


            station_id = properties.get(
                "STN_ID"
            )


            if not station_id:

                continue


            Location.objects.update_or_create(

                station_id=station_id,


                defaults={

                    "station_name":
                        properties.get(
                            "STATION_NAME"
                        ),


                    "province":
                        properties.get(
                            "PROV_STATE_TERR_CODE"
                        ),


                    "latitude":
                        self.convert_coordinate(
                            properties.get(
                                "LATITUDE"
                            )
                        ),


                    "longitude":
                        self.convert_coordinate(
                            properties.get(
                                "LONGITUDE"
                            )
                        ),


                    "elevation":
                        properties.get(
                            "ELEVATION"
                        ),


                    "climate_identifier":
                        properties.get(
                            "CLIMATE_IDENTIFIER"
                        ),


                    "first_year":
                        self.get_year(
                            properties.get(
                                "FIRST_DATE"
                            )
                        ),


                    "last_year":
                        self.get_year(
                            properties.get(
                                "LAST_DATE"
                            )
                        ),
                }
            )


            count += 1


        return {
            "stations_imported": count
        }
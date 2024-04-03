"""
Description: Weather Data Table
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Description: Weather Data Table
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 04/03/24
Credit:
Updates:
"""
from datetime import datetime

class ProdUtil():
    """
    Summary:
    - A Production version Utility static class
    """

    @staticmethod
    def system_log(exception: Exception, data_entre=None) -> None:
        """
        Summary:
        - Opens and writes error logs to a file
        when issues arise from web-scrapping

        Args:
        - Exception object from the event
        - A data object of the corrupted data.

        Return:
        - None
        """
        log_date = datetime.now().strftime('%Y-%m-%d')
        
        with open(f'web_scraping_{log_date}.txt', 'a+', encoding="utf-8") as file_stream_output:

            file_stream_output.write(f'\nError: {exception}\n')
            file_stream_output.write(f'Data Row Corruption:\n {data_entre}\n')

    @staticmethod
    def format_date(unformatted_date: str) -> str:
        """
        Summary:
        - Re-formates string date data

        Args:
        - An unformated date as a string

        Return:
        - A formated date
        """
        return datetime.strptime(unformatted_date, '%B %d, %Y').strftime('%Y-%m-%d')


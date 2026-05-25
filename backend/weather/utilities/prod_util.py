"""
Description: Weather Data Table
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Updates:
"""

from datetime import datetime

import traceback

import logging

import os


class ProdUtil():
    """
    Summary:
    - A Production Utility static class
    """

    # =====================================
    # CONFIGURE LOGGER ONCE
    # =====================================

    log_date = datetime.now().strftime(
        '%Y-%m-%d'
    )

    log_name_path = (
        f'web_scraping_{log_date}.log'
    )

    logging.basicConfig(

        filename=log_name_path,

        level=logging.DEBUG,

        format=(
            '%(asctime)s - '
            '%(name)s - '
            '%(levelname)s - '
            '%(funcName)s - '
            '%(message)s'
        )

    )

    logger = logging.getLogger(__name__)

    @staticmethod
    def system_log(
            exception: Exception,
            data_entre=None) -> None:
        """
        Summary:
        - Opens and writes error logs
        to a file when issues arise.

        Args:
        - Exception object from the event
        - A data object of the corrupted data.

        Return:
        - None
        """

        try:

            # =====================================
            # GET TRACEBACK INFORMATION
            # =====================================

            trace_body = traceback.extract_tb(
                exception.__traceback__
            )

            method_name = 'Unknown'

            if trace_body:

                _, _, method_name, _ = (
                    trace_body[-1]
                )

            # =====================================
            # LOG ERROR
            # =====================================

            ProdUtil.logger.error(

                '\nError: %s\n'
                'Function Name: %s\n'
                'Data Corruption:\n%s\n\n',

                exception,

                method_name,

                data_entre

            )

            # =====================================
            # PRINT TO CONSOLE
            # =====================================

            print(
                f"\nERROR: {exception}\n"
            )

        except Exception as log_error:

            print(
                f"\nLOGGER FAILURE: "
                f"{log_error}\n"
            )

    @staticmethod
    def format_date(
            unformatted_date: str) -> str:
        """
        Summary:
        - Re-formats string date data

        Args:
        - An unformatted date as a string

        Return:
        - A formatted date
        """

        return datetime.strptime(

            unformatted_date,
            '%B %d, %Y'

        ).strftime('%Y-%m-%d')
"""
Description: Weather Plot Operations
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
"""

import calendar

import matplotlib.pyplot as plt

from backend.utilities.prod_util import ProdUtil


class PlotOperations:
    """
    Summary:
    - Handles weather plotting operations.

    Features:
    - Monthly temperature box plots
    - Daily temperature line plots
    """

    def __init__(
            self,
            weather_data):

        self.weather_data = weather_data

    def create_boxplot(self):
        """
        Summary:
        - Generates a box plot for
          average monthly temperatures.
        """

        try:

            monthly_means = [
                [] for _ in range(12)
            ]

            # =====================================
            # GROUP TEMPERATURES BY MONTH
            # =====================================

            for weather_record in self.weather_data:

                month = (
                    weather_record.sample_date.month
                )

                avg_temp = (
                    weather_record.avg_temp
                )

                if avg_temp is not None:

                    monthly_means[
                        month - 1
                    ].append(avg_temp)

            # =====================================
            # CREATE BOXPLOT
            # =====================================

            plt.figure()

            plt.boxplot(
                monthly_means
            )

            years = [

                weather_record.sample_date.year

                for weather_record
                in self.weather_data

            ]

            plt.title(

                f"Monthly Temperature "
                f"Distribution "
                f"({min(years)} - {max(years)})"

            )

            plt.xlabel(
                "Month"
            )

            plt.ylabel(
                "Average Temperature (°C)"
            )

            plt.xticks(
                range(1, 13)
            )

            plt.grid(True)

            plt.show()

        except Exception as e:

            print(
                f"\nBOXPLOT ERROR: "
                f"{e}\n"
            )

            ProdUtil.system_log(
                e,
                e.args
            )

    def create_lineplot(
            self,
            month,
            year):
        """
        Summary:
        - Generates a line plot for
          daily temperatures within
          a selected month/year.

        Args:
        - month (int)
        - year (int)
        """

        try:

            monthly_weather_data = [

                weather_record

                for weather_record
                in self.weather_data

                if (

                    weather_record.sample_date.year
                    == year

                    and

                    weather_record.sample_date.month
                    == month

                )

            ]

            daily_temperatures = []

            num_days_in_month = (

                calendar.monthrange(
                    year,
                    month
                )[1]

            )

            for day in range(
                    1,
                    num_days_in_month + 1):

                day_data = [

                    weather_record

                    for weather_record
                    in monthly_weather_data

                    if (

                        weather_record.sample_date.day
                        == day

                    )

                ]

                if day_data:

                    mean_temp = (

                        sum(

                            record.avg_temp

                            for record in day_data

                            if record.avg_temp
                            is not None

                        )

                        / len(day_data)

                    )

                    daily_temperatures.append(
                        mean_temp
                    )

                else:

                    daily_temperatures.append(
                        None
                    )

            # =====================================
            # CREATE LINE PLOT
            # =====================================

            plt.figure()

            plt.plot(

                range(
                    1,
                    num_days_in_month + 1
                ),

                daily_temperatures,

                marker="o"

            )

            plt.title(

                f"Daily Temperatures - "
                f"{calendar.month_name[month]} "
                f"{year}"

            )

            plt.xlabel(
                "Day"
            )

            plt.ylabel(
                "Average Temperature (°C)"
            )

            plt.xticks(

                range(
                    1,
                    num_days_in_month + 1
                )

            )

            plt.grid(True)

            plt.show()

        except Exception as e:

            print(
                f"\nLINEPLOT ERROR: "
                f"{e}\n"
            )

            ProdUtil.system_log(
                e,
                e.args
            )
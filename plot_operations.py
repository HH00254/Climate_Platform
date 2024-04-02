"""
Description: Weather Processing App Group 9
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/20/24
Credit:
Updates:f
"""

import matplotlib.pyplot as plt

class PlotOperations:

    def __init__(self, weather_data):
        self.weather_data = weather_data

def create_boxplot(self, year_range):
    mean_temps = []

    plt.boxplot(mean_temps)
    plt.title('Mean Temperatures Boxplot')
    plt.xlabel('Years')
    plt.ylabel('Mean Temperature (°C)')
    plt.show()

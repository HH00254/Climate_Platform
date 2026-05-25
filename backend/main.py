from services.weather_controller import WeatherProcessor

if __name__ == "__main__":

    wp = WeatherProcessor(
        "weather_data.sqlite"
    )

    wp.start()
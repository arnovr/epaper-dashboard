import requests

from slides.slide_runner import SlideRunner
from slides.weather.weather_drawing import WeatherDrawing

class Weather(SlideRunner):
    def __init__(self, api_key):
        self.api_key = api_key

    def name(self):
        return "Weather"

    def run(self):
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=Vleuten&units=metric&appid=" + self.api_key
        );

        if response.status_code != 200:
            raise RuntimeError("API Gave incorrect response: " + str(response.status_code))

        json = response.json()
        return WeatherDrawing({
            "description": json['weather'][0]['main'],
            "icon": json['weather'][0]['icon'],
            "temperature": json["main"]["temp"],
            "temperature_feels_like": json["main"]["feels_like"],
        }); 
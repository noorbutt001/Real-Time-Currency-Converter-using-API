import requests

from config.settings import *
from utils.cache import weather_cache


class WeatherService:

    def __init__(self):

        self.session = requests.Session()

    def get_weather(self, city):

        city = city.strip().title()

        if city in weather_cache:
            return weather_cache[city]

        try:

            response = self.session.get(
                BASE_URL,
                params={
                    "q": city,
                    "appid": API_KEY,
                    "units": "metric"
                },
                timeout=5
            )

            if response.status_code == 404:
                return {"error": "City not found"}

            if response.status_code == 401:
                return {"error": "Invalid API key"}

            response.raise_for_status()

            data = response.json()

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }

            weather_cache[city] = weather

            return weather

        except requests.Timeout:
            return {"error": "Timeout"}

        except requests.ConnectionError:
            return {"error": "No Internet"}
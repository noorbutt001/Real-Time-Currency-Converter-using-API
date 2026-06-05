from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DATABASE_URL = "sqlite:///database/weather.db"

CACHE_TIME = 300
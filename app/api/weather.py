import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str):
    if not API_KEY:
        return {"error": "Weather API key is not configured."}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        return {"error": "Could not fetch weather data. Check the city name."}

    return response.json()
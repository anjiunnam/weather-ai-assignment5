import requests

API_KEY = "92df9d98c562e42a8c093196c643dee5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        return {"error": "Could not fetch weather data. Check the city name."}

    return response.json()
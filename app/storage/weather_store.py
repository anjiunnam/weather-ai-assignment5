import json
import os

STORE_PATH = "data/latest_weather.json"


def save_latest(weather_data: dict):
    os.makedirs("data", exist_ok=True)
    with open(STORE_PATH, "w", encoding="utf-8") as f:
        json.dump(weather_data, f, indent=2)


def get_latest():
    if not os.path.exists(STORE_PATH):
        return None

    with open(STORE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
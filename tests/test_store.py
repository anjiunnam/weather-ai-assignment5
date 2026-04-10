import os
from app.storage.weather_store import save_latest, get_latest, STORE_PATH


def test_save_and_get_latest():
    sample = {
        "city": "Oshawa",
        "temperature": 18,
        "humidity": 70,
        "wind_speed": 4,
        "condition": "Clear",
        "description": "clear sky"
    }

    save_latest(sample)
    loaded = get_latest()

    assert loaded == sample


def test_get_latest_returns_none_when_file_missing():
    if os.path.exists(STORE_PATH):
        os.remove(STORE_PATH)

    result = get_latest()
    assert result is None
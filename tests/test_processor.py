from app.etl.processor import normalize_weather


def test_normalize_weather_success():
    raw_data = {
        "name": "Toronto",
        "main": {
            "temp": 22.5,
            "humidity": 60
        },
        "wind": {
            "speed": 5.2
        },
        "weather": [
            {
                "main": "Clouds",
                "description": "broken clouds"
            }
        ]
    }

    result = normalize_weather(raw_data)

    assert result["city"] == "Toronto"
    assert result["temperature"] == 22.5
    assert result["humidity"] == 60
    assert result["wind_speed"] == 5.2
    assert result["condition"] == "Clouds"
    assert result["description"] == "broken clouds"


def test_normalize_weather_invalid_input():
    raw_data = {"error": "Could not fetch weather data"}
    result = normalize_weather(raw_data)
    assert result is None
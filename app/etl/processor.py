def normalize_weather(raw_data: dict):
    if not raw_data or "error" in raw_data:
        return None

    try:
        return {
            "city": raw_data["name"],
            "temperature": raw_data["main"]["temp"],
            "humidity": raw_data["main"]["humidity"],
            "wind_speed": raw_data["wind"]["speed"],
            "condition": raw_data["weather"][0]["main"],
            "description": raw_data["weather"][0]["description"]
        }
    except (KeyError, IndexError, TypeError):
        return None
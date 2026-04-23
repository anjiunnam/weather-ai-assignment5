from app.reasoning.rules import detect_risks


def generate_summary(weather_data: dict):
    return (
        f"The weather in {weather_data['city']} is {weather_data['description']} "
        f"with a temperature of {weather_data['temperature']}°C."
    )


def generate_recommendation(weather_data: dict):
    condition = weather_data["condition"].lower()
    temp = weather_data["temperature"]
    wind_speed = weather_data["wind_speed"]

    if condition in ["rain", "thunderstorm", "snow", "drizzle"]:
        return "Carry an umbrella or protective clothing and be careful on wet or slippery roads."

    if temp >= 35:
        return "Avoid outdoor activity in peak afternoon hours and drink plenty of water."

    if temp <= 5:
        return "Wear layered warm clothing before going outside."

    if wind_speed >= 12:
        return "Be cautious in open outdoor areas because of strong wind."

    return "Weather looks comfortable for normal outdoor activities."

def generate_result(weather_data: dict):
    return {
        "summary": generate_summary(weather_data),
        "recommendation": generate_recommendation(weather_data),
        "risks": detect_risks(weather_data)
    }
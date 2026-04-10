from app.reasoning.rules import detect_risks


def generate_summary(weather_data: dict):
    return (
        f"The weather in {weather_data['city']} is {weather_data['description']} "
        f"with a temperature of {weather_data['temperature']}°C."
    )


def generate_recommendation(weather_data: dict):
    condition = weather_data["condition"].lower()
    temp = weather_data["temperature"]

    if condition in ["rain", "thunderstorm", "snow", "drizzle"]:
        return "It is better to stay indoors or carry proper protection outside."

    if temp > 30:
        return "Stay hydrated and avoid too much time outdoors in peak heat."

    if temp < 5:
        return "Wear warm clothing before going outside."

    return "Weather looks comfortable for normal outdoor activities."


def generate_result(weather_data: dict):
    return {
        "summary": generate_summary(weather_data),
        "recommendation": generate_recommendation(weather_data),
        "risks": detect_risks(weather_data)
    }
def detect_risks(weather_data: dict):
    risks = []

    if weather_data["temperature"] >= 35:
        risks.append("High heat risk")

    if weather_data["wind_speed"] >= 12:
        risks.append("Strong wind risk")

    if weather_data["condition"].lower() in ["rain", "thunderstorm", "snow", "drizzle"]:
        risks.append("Unsafe weather condition")

    if not risks:
        risks.append("No major risk detected")

    return risks
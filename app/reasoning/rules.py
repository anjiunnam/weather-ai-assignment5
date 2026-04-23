def detect_risks(weather_data: dict):
    risks = []

    temperature = weather_data["temperature"]
    wind_speed = weather_data["wind_speed"]
    condition = weather_data["condition"].lower()

    if temperature >= 35:
        risks.append("High heat risk: avoid outdoor activity in peak afternoon hours.")

    if temperature <= 5:
        risks.append("Cold weather risk: wear warm layers before going outside.")

    if wind_speed >= 12:
        risks.append("Strong wind risk: be careful when biking or walking in open areas.")

    if condition in ["rain", "thunderstorm", "snow", "drizzle"]:
        risks.append("Unsafe weather condition: carry protection and avoid slippery areas.")

    if not risks:
        risks.append("No major weather risk detected.")

    return risks
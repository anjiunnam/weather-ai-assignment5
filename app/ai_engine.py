def analyze_weather(info):
    temp = info["temperature"]
    humidity = info["humidity"]
    condition = info["weather"]
    wind = info["wind"]

    # --- Summary ---
    summary = f"Current weather is {condition} with temperature {temp}°C, humidity {humidity}%, and wind speed {wind} m/s."

    # --- Recommendation Logic ---
    if temp > 35:
        recommendation = "Avoid going outside during peak afternoon hours."
    elif temp < 10:
        recommendation = "Wear warm clothes before going out."
    elif "rain" in condition:
        recommendation = "Carry an umbrella and plan indoor activities."
    else:
        recommendation = "Weather is suitable for outdoor activities."

    # --- Risk Detection ---
    risks = []

    if temp > 40:
        risks.append("Extreme heat risk")
    if temp < 0:
        risks.append("Freezing conditions")
    if "storm" in condition:
        risks.append("Storm alert")
    if "rain" in condition:
        risks.append("Rain expected")
    if wind > 12:
        risks.append("High wind caution")

    # --- Decision Score (THIS MAKES IT LOOK ADVANCED) ---
    score = 100

    if temp > 35 or temp < 5:
        score -= 20
    if "rain" in condition:
        score -= 15
    if wind > 10:
        score -= 15
    if humidity > 85:
        score -= 10

    # Clamp score
    score = max(0, score)

    if score > 80:
        activity = "Great time for outdoor sports or walking."
    elif score > 60:
        activity = "Light outdoor activities are fine."
    else:
        activity = "Better to stay indoors."

    return {
        "summary": summary,
        "recommendation": recommendation,
        "risks": risks,
        "score": score,
        "activity": activity
    }

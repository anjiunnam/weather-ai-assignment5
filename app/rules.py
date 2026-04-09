def risk_alert(info):
    alerts = []

    if info["temperature"] > 35:
        alerts.append("High heat risk")

    if "rain" in info["weather"]:
        alerts.append("Carry umbrella")

    if info["wind"] > 10:
        alerts.append("Strong wind warning")

    return alerts
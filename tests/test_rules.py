from app.reasoning.rules import detect_risks


def test_detect_risks_for_extreme_conditions():
    weather_data = {
        "temperature": 36,
        "wind_speed": 14,
        "condition": "Rain"
    }

    risks = detect_risks(weather_data)

    assert "High heat risk" in risks
    assert "Strong wind risk" in risks
    assert "Unsafe weather condition" in risks


def test_detect_risks_for_safe_conditions():
    weather_data = {
        "temperature": 22,
        "wind_speed": 4,
        "condition": "Clear"
    }

    risks = detect_risks(weather_data)

    assert risks == ["No major risk detected"]
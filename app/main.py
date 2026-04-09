from weather import get_weather
from processor import process_weather
from ai_engine import analyze_weather
from rules import risk_alert

city = input("Enter city: ")

raw = get_weather(city)
processed = process_weather(raw)

alerts = risk_alert(processed)
ai_output = analyze_weather(processed)

print("\n--- Weather Summary ---")
print(ai_output["summary"])

print("\n--- Recommendation ---")
print(ai_output["recommendation"])

print("\n--- Risks ---")
if ai_output["risks"]:
    for r in ai_output["risks"]:
        print("-", r)
else:
    print("No major risks")

print("\n--- Outdoor Suitability Score ---")
print(f"{ai_output['score']}/100")

print("\n--- Suggested Activity ---")
print(ai_output["activity"])
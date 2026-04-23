# Improvement Notes

## Weakness Found
The original version gave very basic recommendation and risk output.
It also used a generic invalid-city error message.

## Evidence
During evaluation, the system worked end to end, but some outputs were too generic to be very useful.

## Improvement Made
I improved:
- recommendation wording for hot, cold, rainy, and windy conditions
- invalid city error handling with a clearer user-facing message

## What Improved
The system now gives more helpful and more specific guidance.
The failure case experience is also clearer for users.

## What Still Remains Weak
The app still does not support forecasting, retrieval, or advanced context-aware reasoning.
It is still a focused proof of concept.
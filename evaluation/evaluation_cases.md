# Evaluation Cases

## Representative Cases

### Case 1 - Toronto
Expected:
- Valid weather result
- Reasonable summary
- Recommendation matches condition
- No crash

### Case 2 - Vancouver
Expected:
- Rain-related summary or risk if applicable
- Recommendation reflects wet weather

### Case 3 - Dubai
Expected:
- Heat-related recommendation if temperature is high
- Risk alert if extreme heat threshold is crossed

### Case 4 - Winnipeg
Expected:
- Cold-weather recommendation if temperature is low
- No crash

### Case 5 - Miami
Expected:
- Humid or storm-related recommendation if conditions justify it
- No crash

## Failure Cases

### Failure Case 1 - Invalid city
Input: abcxyztest
Expected:
- Safe error message
- No crash

### Failure Case 2 - Missing or failed API response
Expected:
- Safe error handling
- No crash
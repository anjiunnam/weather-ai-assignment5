# Final System Results

## Output Quality Metric
Metric used: simple rubric scoring
- Correct
- Partially Correct
- Incorrect

## End-to-End Success Metric
Metric used:
- Success = user enters city and app returns usable result without crashing
- Failure = crash, broken flow, or unusable result

## Upstream Component Metric
Component evaluated: ETL normalization
Metric used:
- Correct field extraction
- Missing-field safety
- Clean normalized structure

## Case Results

| Case | Output Quality | End-to-End Success | ETL Quality | Notes |
|------|----------------|-------------------|------------|------|
| Toronto | Correct | Success | Correct | Summary and recommendation matched output |
| Vancouver | Correct/Partially Correct | Success | Correct | Rain handling checked |
| Dubai | Correct/Partially Correct | Success | Correct | Heat recommendation checked |
| Winnipeg | Correct/Partially Correct | Success | Correct | Cold recommendation checked |
| Miami | Correct/Partially Correct | Success | Correct | Humidity/storm behavior checked |
| Invalid city | Correct | Success | Correct | Error handled safely |
| API failure case | Correct | Success/Documented | Correct | Explained as handled failure path |




## Upstream Component Evaluation: ETL Normalization

The upstream component I evaluated was the normalization step.

Reason:
The app depends on converting raw API JSON into a clean internal schema before reasoning happens.

What I checked:
- city extracted correctly
- temperature extracted correctly
- humidity extracted correctly
- wind speed extracted correctly
- condition and description extracted correctly
- invalid or missing fields handled safely

Result:
The ETL layer worked correctly for representative valid cases and safely returned failure behavior for bad inputs.
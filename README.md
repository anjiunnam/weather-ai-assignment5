1. Problem
        Raw weather data is hard to interpret

2. Solution
        AI-based decision system

3. Architecture
        Input → API → AI → Output

4. Features
        AI summary
        Recommendations
        Risk alerts
5. How to Run
        python main.py



## Architecture Category

This system is best classified as tool-first.

The app depends on deterministic external API calls to get live weather data, then applies rule-based reasoning to generate summary, recommendation, and risk alerts.

I did not choose retrieval-first because the system does not search stored documents or chunks.
I did not choose prompt-first because the app does not mainly rely on long-context prompting.


## Supported Tasks

- Get current weather for a city
- Show weather summary
- Show recommendation based on conditions
- Show risk alerts for unsafe weather

## Out of Scope

- Long-term forecasting
- Historical weather analytics
- Maps and geolocation
- User accounts
- Production-grade storage
- Retrieval over documents



## Assignment 6 Architecture Justification
## Pipeline and Data Flow
## Evaluation Summary
## Baseline Comparison
## Evidence-Based Improvement


User enters city -> backend fetches raw weather data -> ETL normalizes response -> reasoning layer generates summary, recommendation, and risks -> UI displays result


## Capability Not Implemented

One important capability I did not implement is retrieval-first RAG.

RAG would help only if the system needed to answer questions from stored documents, historical files, or multiple data sources.
For this app, live API calls and deterministic reasoning were simpler and more appropriate.

RAG would add retrieval logic, storage overhead, and more debugging complexity.
I would consider adding it only if the app later needed historical weather comparison or document-based advisory features.
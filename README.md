# Portfolio Decision Engine

**Status: Planning / Early Design**

A personal decision-support system for equity investing (not a stock price predictor).

The goal is to help answer practical questions such as:
- How concentrated is my portfolio?
- What material SEC filings or events just occurred for my holdings?
- How would simple market shocks affect individual positions and overall risk?
- Should I Buy / Hold / Trim / Watch?

### Planned Core Features
- Portfolio concentration and risk analysis
- SEC filing ingestion and relevance filtering
- Simple scenario / shock simulation
- Clear recommendation layer with supporting evidence
- Decision logging so I can measure whether the tool actually helps

### Planned Tech Stack
- **Python**
- **FastAPI**
- **Strawberry GraphQL**
- **SQLite**
- **Redis** (caching + rate limiting)
- **yfinance** + **Pandas**

### Current Status
This repository is in the planning and architecture phase.  
Implementation has not started yet. The focus right now is defining the data model, decision logic, and API shape before writing production code.

### Roadmap (High Level)
1. Holdings + price data layer
2. Concentration & basic risk metrics
3. SEC filing ingestion
4. Scenario engine
5. Recommendation + evidence output
6. GraphQL API + Redis caching
7. Simple web / CLI interface

---

This is a personal project intended for real use with my own portfolio.

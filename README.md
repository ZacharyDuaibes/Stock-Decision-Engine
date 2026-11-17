# Portfolio Decision Engine

**Status: Early implementation**

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
First working piece: load holdings from CSV, rank by weight, and simulate price shocks (`portfolio.py`).

### Usage

Holdings CSV needs `symbol` and `market_value` columns. Sample file: `examples/sample_holdings.csv`.

Rank holdings by weight:

```bash
python3 portfolio.py examples/sample_holdings.csv
```

Simulate price shocks:

```bash
python3 portfolio.py examples/sample_holdings.csv --shock AAA -20 --shock BBB -10
```

Example output:

```
Portfolio impact: -13.0%
Symbol        Before     After   Impact (pp)
AAA            50.0%     46.0%         -10.0
BBB            30.0%     31.0%          -3.0
CCC            20.0%     23.0%          +0.0
```

`--shock` can be repeated. Percents are relative price changes (e.g. `-20` means −20%). Impact (pp) is each position’s contribution to the portfolio move in percentage points; After is the reweighted share of the portfolio after the shock.

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

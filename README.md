# Portfolio Decision Engine

A personal decision-support tool for equity investing.

This is **not** a stock price predictor.  
It is a system that helps answer practical questions:

- Should I buy more, hold, trim, or watch?
- How concentrated is my portfolio across tickers, sectors, and themes?
- What material events (filings, news) just occurred for my holdings?
- What happens to my positions under simple scenario shocks?

The goal is better decisions under incomplete information, not forecasting returns.

### Core ideas
- Start from *my* actual holdings and the questions I actually ask
- Surface concentration, co-movement, and second-order exposures
- Ingest recent SEC filings and major events
- Produce a clear recommendation layer with supporting evidence
- Log every suggestion vs. what I actually did so I can measure whether the tool helps

### Status
Early stage. Building the MVP focused on reliable data + usable decision output before adding more sophisticated models.
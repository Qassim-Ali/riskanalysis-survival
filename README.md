# Survival-Based Stock Risk Analysis

A beginner project exploring how survival analysis .How a technique more commonly seen in actuarial science  can be applied to financial risk modelling.

## thesis

In actuarial science, survival models measure how long something "survives" before a bad event occurs. I got curious about whether the same framework could be applied to stocks. How often does a stock experience a significant drop, and what does that tell us about its risk profile?

## What it does

- Pulls real historical stock data using Yahoo Finance
- Defines a "stress event" as any day the stock drops more than 2%
- Builds a survival curve showing how the probability of avoiding a stress event decays over time
- Outputs a plain-english risk summary

## Results (Micron, MU — 2024 to 2026)

- Stress event rate: 23.39% of all trading days
- Expected days between stress events: 4.3 days
- Expected stress events in a typical trading year: ~58
- Average daily survival rate: 76.61%

Micron is a highly volatile stock — a stress event roughly once a week makes it a useful and interesting subject for a risk model.

## What I learned

The survival curve is the same shape you'd see in life insurance modelling or clinical trials — it starts at 1.0 and decays as events accumulate. Applying it to finance felt like a natural crossover between the two fields.

## Libraries used
- `yfinance` — real historical stock data
- `numpy` — numerical calculations
- `pandas` — data manipulation
- `matplotlib` — visualization

## Notes
This is my second coding project. I'm exploring the overlap between actuarial science and quantitative finance.

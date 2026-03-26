import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# download stock data
stock = yf.download("MU", start="2024-01-01", end="2026-03-05")

# calculate daily returns
returns = stock["Close"].pct_change().dropna()

print(f"Downloaded {len(returns)} days of data")
print(f"First few returns:")
print(returns.head())

# define a "stress event" — a day where the stock drops more than 2%
threshold = -0.02

# mark each day as a failure (1) or survival (0)
events = (returns.values.flatten() < threshold).astype(int)

# calculate the survival function — probability of surviving each day
total_days = len(events)
failures = events.cumsum()
survival = 1 - (failures / total_days)

print(f"Total stress events (drops > 2%): {events.sum()}")
print(f"Stress event rate: {events.mean():.2%} of all trading days")

# plot the survival curve
plt.figure(figsize=(12, 6))
plt.plot(survival, color="blue", linewidth=2)

# add a line showing the overall stress rate
plt.axhline(y=1 - events.mean(), color="red", linestyle="--", linewidth=1.5, label=f"Average survival rate: {1 - events.mean():.2%}")

plt.title("Survival Analysis — Micron (MU) Stress Event Risk")
plt.xlabel("Trading Days")
plt.ylabel("Probability of No Stress Event")
plt.legend()
plt.tight_layout()
plt.show()

# print a risk summary
print(f"Probability of surviving any given day without a stress event: {1 - events.mean():.2%}")
print(f"Expected days between stress events: {1 / events.mean():.1f} days")
print(f"In a typical trading year (252 days), expect ~{int(events.mean() * 252)} stress events")
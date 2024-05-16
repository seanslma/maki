# Datetime
https://medium.com/data-science-at-microsoft/introduction-to-feature-engineering-for-time-series-forecasting-620aa55fcab0

- month/day/hour
- weekday/weekend/holiday
- lag (shift): use previous data 
- windows (rolling average): mean for the last day/week etc.
- expanding

## datetime feature
Usually the `day of year`, `day of week` and `hour` will cover all the season patterns. 
Each will encoded into the `sine` and `cosine` features.

## sin/cos hour 
```py
df['h_sin'] = np.sin(np.pi * df['hour'] / 12.)
df['h_cos'] = np.cos(np.pi * df['hour'] / 12.)
```

## mean/median/min/max/std/skew/kurt/range

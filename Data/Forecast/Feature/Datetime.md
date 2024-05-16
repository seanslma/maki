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

## sin/cos features
```py
# hour
df['h_sin'] = np.sin(df['hour'] / 12 * np.pi)
df['h_cos'] = np.cos(df['hour'] / 12 * np.pi)
# month
df['m_sin'] = np.sin(df['month'] / 6 * np.pi)
df['m_cos'] = np.cos(df['month'] / 6 * np.pi)
# day of year
df['y_sin'] = np.sin(df['day_of_year'] / 183 * np.pi)
df['y_cos'] = np.cos(df['day_of_year'] / 183 * np.pi)
```

## mean/median/min/max/std/skew/kurt/range

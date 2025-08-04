# Datetime
- https://medium.com/data-science-at-microsoft/introduction-to-feature-engineering-for-time-series-forecasting-620aa55fcab0
- https://medium.com/@karanbhutani477/feature-engineering-for-time-series-data-a-deep-yet-intuitive-guide-b544aeb26ec2

features:
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
# sin(2 * pi * x / max(x))
# cos(2 * pi * x / max(x))

# hour
df['h_sin'] = np.sin(np.pi * df['hour'] / 12)
df['h_cos'] = np.cos(np.pi * df['hour'] / 12)
# month
df['m_sin'] = np.sin(np.pi * df['month'] / 6)
df['m_cos'] = np.cos(np.pi * df['month'] / 6)
# day of year
df['y_sin'] = np.sin(np.pi * df['day_of_year'] / 183)
df['y_cos'] = np.cos(np.pi * df['day_of_year'] / 183)
```

## radial basis function
sin/cos vs radial basis function (rbf):
https://developer.nvidia.com/blog/three-approaches-to-encoding-time-information-as-features-for-ml-models/

diff:
- sin/cos: cyclical or periodic data, such as time series data
- rbf: non-linear relationships and capturing complex patterns in data, such as images
- rbf can introduce more complexity to the model, which may lead to overfitting if not carefully tuned
- rbf can be computationally more expensive than sine/cosine features, especially for large datasets
  
## lag and lag diff/auto correlation
lag features:
https://www.kaggle.com/code/ryanholbrook/time-series-as-features
```py
df['x_lag1'] = df.groupby(['id'])['x'].shift(1)
df['x_lag1_diff'] = df['x'] - df['x'].groupby(['id']).shift(1)
df['x_lag1_autocorr'] = df['x'].corrwith(df['x'].shift(1))
```

## percentage diff
```py
df['pct_diff_x_y'] = (df['x'] - df['y']) / df['y'] * 100
```

## diff first/median
```py
df['x_diff_first'] = df['x'] - df['x'].groupby(['id']).transform('first') #median
```

## imbalance
```py
df['imb_x_y'] = (df['x'] - df['y']).divide(df['x'] + df['y'], fill_value=np.nan)
```

## rolling
mean/var/std/min/max/med/skew/kurt/cumsum/range
```py
df['x_mean'] = df.groupby(['id'])['x'].agg('mean') # std etc
df['x_cumsum'] = df.groupby(['id'])['x'].cumsum()
df['x_range'] = df.groupby(['id'])['x'].max(axis=1) - df.groupby(['id'])['x'].min(axis=1)
```

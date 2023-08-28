# Outlier

check outlier by hisgram and scatter plot.

https://www.analyticsvidhya.com/blog/2021/05/feature-engineering-how-to-detect-and-remove-outliers-with-python-code/

https://stats.stackexchange.com/questions/69874/how-to-correct-outliers-once-detected-for-time-series-data-forecasting

## remove outliers by stastical method
- Q1: first quartile, median of first part
- Q3: third quartile, median of second part

Minor outlier
- Lower bound: Q1 - (1.5 * (Q3-Q1))
- Upper bound: Q3 + (1.5 * (Q3-Q1))

Major outlier
- Lower bound: Q1 - (3 * (Q3-Q1))
- Upper bound: Q3 + (3 * (Q3-Q1))

Python code to remove major outlier
```py
p25 = d1['val'].quantile(0.25) #percentile25
p75 = d1['val'].quantile(0.75) #percentile75
lower_limit = p25 - 3 * (p75 - p25)
upper_limit = p75 + 3 * (p75 - p25)
df = d1.copy()
df['val'] = np.where(df['val'] < lower_limit, np.nan, df['val'])
df['val'] = np.where(df['val'] > upper_limit, np.nan, df['val'])
```

## reduce effects of outliers by using a weighting mechanism
Weights of observations are adjusted so as to append less weight to extreme values.
- Huber regression
- Bisquare regression
```py
huber_regressor = sklearn.linear_model.HuberRegressor(
    epsilon=1.35, max_iter=100, alpha=0.0001, warm_start=False, fit_intercept=True, tol=1e-05
)
```

## time series shocks
Use Kalman Filter to adjust for time series shocks.

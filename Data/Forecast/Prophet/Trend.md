# Trend
There are three built-in trend functions 
- piecewise linear
- piecewise logistic growth, and
- flat

## force trend growth rate to be flat
```py
m = Prophet(growth='flat')
```

## Saturating Forecast using `logistic growth` trend model
https://facebook.github.io/prophet/docs/saturating_forecasts.html#forecasting-growth

By default, Prophet uses a linear model for its forecast.
Prophet allows you to make forecasts using a `logistic growth` trend model:
- `cap` and `floor` columns can be used to bound the trend.
- `cap` or `floor` must be specified for every row in the dataframe, and that it does not have to be constant.

example
```py
# fit model
df['cap'] = 8.5
m = Prophet(growth='logistic')
m.fit(df)

# predict
future = m.make_future_dataframe(periods=1826)
future['cap'] = 8.5
forecast = m.predict(future)
fig = m.plot(forecast)
```

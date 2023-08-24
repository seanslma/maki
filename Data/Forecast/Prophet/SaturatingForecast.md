# Saturating Forecast

https://facebook.github.io/prophet/docs/saturating_forecasts.html#forecasting-growth

- Use the `cap` and `floor` columns to bound the trend.
- `cap`/`floor` must be specified for every row in the dataframe, and that it does not have to be constant.

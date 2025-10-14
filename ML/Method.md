# Method

https://www.reddit.com/r/MachineLearning/comments/ob2rll/d_how_often_is_lightgbm_used_for_forecasting_in/

## statistics
- Prophet and ARIMA-type models are great for forecasting trends with steady growth and stable seasonality
- but struggle with time-series that have complex dependencies on exogenous variables (e.g. ‘shocks’ relating to weather)

## ensemble
Use an ensemble of 
- Prophet to capture the underlying seasonality, and
- XGBoost to capture the weather/seasonality shock impact

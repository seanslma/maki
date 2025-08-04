# Time Series

## methods
https://news.ycombinator.com/item?id=37877443
- On extremely high dimensional data: `MLP` that just uses lagged values as features
- On mid-dimensional data: `LightGBM/Xgboost` is by far the best and generally performs at or better than any deep learning model
- On low-dimensional data: `(V)ARIMA/ETS/Factor` models are still king

## model history
https://medium.com/@ycwong.joe/a-brief-history-of-time-series-models-38455c2cd78d

## summary
https://chartexpo.com/blog/time-series-forecasting

## How to feed forecast into next step's input feature
https://www.kaggle.com/code/ryanholbrook/forecasting-with-machine-learning
- multioutput model
- each model for one step
- one model, update feature based on prevous forecast
- each model for one step, update feature based on prevous forecast

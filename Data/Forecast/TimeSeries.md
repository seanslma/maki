# Time Series

## methods
https://news.ycombinator.com/item?id=37877443
- On extremely high dimensional data: `MLP` that just uses lagged values as features
- On mid-dimensional data: `LightGBM/Xgboost` is by far the best and generally performs at or better than any deep learning model
- On low-dimensional data: `(V)ARIMA/ETS/Factor` models are still king

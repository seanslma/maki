# Memory

## XGBoost reduce memory
https://xgboosting.com/xgboost-use-less-memory/
- set `tree_method = 'hist'`
- reduce `max_bin`. default = 256
- reduce `max_depth`. default = 6
- increase `min_child_weight`. default = 1
- `colsample_bytree`, `colsample_bylevel`, and `colsample_bynode`. default = 1

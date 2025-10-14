# feature importance
The methods, like PFI or SHAP importance, are not designed for feature selection. They are for feature importance - explain features

Purpose of feature selection:
- Improve predictive performance
- Speed up model training and prediction
- Reduce feature space for comprehensibility
- Cost reduction

## feature importance example
```py
import xgboost as xgb
import lightgbm as lgb

# XGBoost feature importance
import xgboost as xgb
# model = model = xgb.XGBClassifier(
#     objective='binary:logistic',  # Default for binary classification
#     eval_metric='logloss',        # Metric for evaluation
# )
model = xgb.XGBRegressor(
    objective='reg:squarederror',  # Default for regression, minimizes squared error
    eval_metric='rmse',            # Metric for evaluation
)
model.fit(X, y)
importance = model.feature_importances_
print(importance)

# LightGBM feature importance
train_data = lgb.Dataset(data=X.to_arrow(), label=y.to_arrow())
# for small number of features, reduce `num_leaves` to avoid warnings
# for small number of data points, reduce `min_data_in_leave` to avoid warnings
# warnings #1: [Warning] No further splits with positive gain, best gain: -inf
# warnings #2: There are no meaningful features which satisfy the provided configuration.
# Decreasing Dataset parameters min_data_in_bin or min_data_in_leaf and re-constructing Dataset might resolve this warning.
params = {'objective': 'regression', 'metric': 'rmse', 'num_leaves': 2, 'min_data_in_leaf': 2}
model = lgb.train(params, train_data, num_boost_round=100)
importances = model.feature_importance(importance_type='gain')
print(importance)

# Catboost feature importance, lgb: 35x faster, xgb: 15x faster
# model = ctb.CatBoostClassifier(verbose=0)
model = ctb.CatBoostRegressor(verbose=0)
model.fit(X.to_pandas(), y.to_pandas())
importance = model.get_feature_importance()
print(importance)
```

## shap feature explainer
```py
import shap
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import (
    plot_acf,
    plot_pacf,
)

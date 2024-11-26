# LightGBM

## LightGBM vs XGBoost
- LightGBM generally faster than XGBoost, especially for large datasets, does not support arrow
- XGBoost might have slightly lower memory requirements compared to LightGBM

## parameters
https://lightgbm.readthedocs.io/en/latest/Parameters.html

The hyperparameters that have the greatest effect on optimizing the LightGBM evaluation metrics are [ref](https://docs.aws.amazon.com/sagemaker/latest/dg/lightgbm-tuning.html): 
- `num_iterations`: [50, 1000]. How many trees will be built
- `learning_rate`: [0.001, 0.01]. default=0.1.
- `num_leaves`: [10, 100], (1, 131072], default=31. Maximum number of leaves in one tree
- `feature_fraction`: [0.1, 1], default=1. randomly select a subset of features on each iteration (tree)
- `bagging_fraction`: [0.1, 1]. alias: `subsample`. randomly select part of data without resampling
- `bagging_freq`: [0, 10]. frequency for bagging
- `max_depth`: [15, 100]. Maximum depth of the tree
- `min_data_in_leaf`: [10, 200], default=20. Minimal number of data in one leaf

## example
https://github.com/microsoft/LightGBM/issues/2930

## feature selection
https://www.kaggle.com/code/pnprabakaran/feature-selection-before-hand-lightgbm

## LightGBM example
`lgb.train` is the core training API for lightgbm.
```py
params = {
    'verbose': -1, 
    'objective': 'regression_l1', 
    'seed': 13,
    'device': 'gpu',       
    'n_jobs': -1,          
    'learning_rate': 0.02,
    'num_leaves': 96,     
    'feature_fraction': 0.6,
    'feature_fraction_bynode': 0.9,     
    'bagging_fraction': 0.8, 
    'bagging_freq': 5,     
    'min_child_samples': 1500,
}

num_boost_round = 1200 # number of iterations
# train model
train_set = lgb.Dataset(df[xcols], df['target'])
model = lgb.train(
    params, 
    train_set,
    num_boost_round,
    init_model=None, 
    valid_sets=[train_set, test_set], 
    callbacks=[lgb.log_evaluation(50), lgb.early_stopping(stopping_rounds=250)],
)
model.save_model('lgb_model.txt')
# forecast
preds = m.predict(df[xcols])

# feature importance
ax = lgb.plot_importance(model, max_num_features=40, figsize=(15,15))
plt.show()

# feature importance to csv
df_importance = pd.DataFrame({
    'feature': model.feature_name(),
    'importance': model.feature_importance(),
})
df_importance.to_csv('feature_importance.csv')
```

## LGBMRegressor
`LGBMRegressor` is the sklearn interface, a wrapper for LightGBM. 
The `fit(X, y)` call is standard sklearn syntax for model training.
```py
params = {
    'verbose': -1,
    'objective': 'mae',
    'random_state': seed,    
    'device': 'gpu',
    'n_jobs': 4,     
    'n_estimators': 1200,
    'learning_rate': 0.03,
    'max_depth': 10,   
    'num_leaves': 256,  
    'subsample': 0.6,
    'colsample_bynode': 0.6,
    'colsample_bytree': 0.9,        
    'importance_type': 'gain',
}
model = lgb.LGBMRegressor(**params)

model.fit(
    df_train.drop(columns=['target']), 
    df_train['target'] - df_train['target_lag_7d'].fillna(0),
    eval_set=[(
        df_valid.drop(columns=['target']), 
        df_valid['target'] - df_valid['target_lag_7d'].fillna(0),
    )],
    categorical_feature=cat_features,
    callbacks=[
        lgb.callback.early_stopping(stopping_rounds=100),
        lgb.callback.log_evaluation(period=100)
    ],
)
model.booster_.save_model(model_filename)

# feature importance
lgb.booster_.feature_importance()
fea_imp_ = pd.DataFrame({'cols': train.columns, 'fea_imp': lgb.feature_importances_})
fea_imp_.loc[fea_imp_.fea_imp > 0].sort_values(by=['fea_imp'], ascending=False)

# plot feature importance
plt.barh(X_train.columns, xgb.feature_importances_)
plt.show()
```

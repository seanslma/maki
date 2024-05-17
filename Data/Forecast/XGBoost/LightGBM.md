# LightGBM

LightGBM vs XGBoost
- LightGBM generally faster than XGBoost, especially for large datasets
- XGBoost might have slightly lower memory requirements compared to LightGBM

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
    'n_jobs': -1, 
    'device': 'gpu',            
    'learning_rate': 0.02, 
    'feature_fraction_bynode': 0.9,     
    'feature_fraction': 0.6, 
    'bagging_fraction': 0.8, 
    'bagging_freq': 5, 
    'num_leaves': 96, 
    'min_child_samples': 1500,
}

ni = 1200
lgb_train = lgb.Dataset(df[xcols], df['target'])
model = lgb.train(params, lgb_train, ni, verbose_eval=False)
preds = m.predict(df[xcols])
```

## LGBMRegressor
`LGBMRegressor` is the sklearn interface, a wrapper for LightGBM. 
The `fit(X, y)` call is standard sklearn syntax for model training.
```py
params = {
    'verbose': -1,
    'objective': 'mae',
    'random_state': seed,
    'n_jobs': 4,
    'device': 'gpu',       
    'n_estimators': 1200,
    'learning_rate': 0.03,    
    'subsample': 0.6,
    'colsample_bynode': 0.6,
    'colsample_bytree': 0.9,
    'num_leaves': 256,
    'max_depth': 10,           
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
```

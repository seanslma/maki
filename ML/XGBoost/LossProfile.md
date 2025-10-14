# xgboost loss profiles (Train & Valid)

## Use XGBoost's Python API (`xgboost.train`)
```py
import xgboost as xgb
import matplotlib.pyplot as plt

# DMatrix datasets
dtrain = xgb.DMatrix(X_train, label=y_train)
dvalid = xgb.DMatrix(X_valid, label=y_valid)

params = {
    'objective': 'multi:softprob',
    'eval_metric': 'mlogloss',
    'num_class': num_classes,
    'tree_method': 'hist',
    # Add other params...
}

evals_result = {}
model = xgb.train(
    params,
    dtrain,
    num_boost_round=1000,
    evals=[(dtrain, 'train'), (dvalid, 'valid')],
    early_stopping_rounds=10,
    evals_result=evals_result,
    verbose_eval=10
)

train_loss = evals_result['train']['mlogloss']
valid_loss = evals_result['valid']['mlogloss']

# Plot Loss Curves
plt.figure(figsize=(10, 6))
plt.plot(train_loss, label='Train Loss')
plt.plot(valid_loss, label='Valid Loss')
plt.xlabel('Boosting Round')
plt.ylabel('Log Loss')
plt.title('XGBoost: Training vs Validation Loss')
plt.legend()
plt.grid(True)
plt.show()
```

## Use `xgb.cv`
```py
cv_results = xgb.cv(
    params,
    dtrain,
    num_boost_round=1000,
    nfold=5,
    metrics='mlogloss',
    early_stopping_rounds=10,
    verbose_eval=10
)

# Plot mean validation loss
plt.plot(cv_results['test-mlogloss-mean'], label='CV Valid Loss')
plt.plot(cv_results['train-mlogloss-mean'], label='CV Train Loss')
plt.xlabel('Boosting Round')
plt.ylabel('Log Loss')
plt.title('XGBoost CV Loss')
plt.legend()
plt.grid(True)
plt.show()
```

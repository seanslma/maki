# lightgbm loss profiles (Train & Valid)
Plotting the **training and validation loss (or other metrics)** over boosting rounds is useful to understand:
- When overfitting starts
- Whether early stopping kicked in at the right point
- Whether training should have run longer

## Use `evals_result` in `lgb.train()`

The `evals_result` parameter lets you collect the training history.

```py
import lightgbm as lgb
import matplotlib.pyplot as plt

evals_result = {}
model = lgb.train(
    params,
    train_set,
    num_boost_round=1000,
    valid_sets=[train_set, valid_set],
    valid_names=['train', 'valid'],
    evals_result=evals_result,
    early_stopping_rounds=10,
    verbose_eval=10
)

train_loss = evals_result['train']['multi_logloss']
valid_loss = evals_result['valid']['multi_logloss']

# Plot the Loss Profiles
plt.figure(figsize=(10, 6))
plt.plot(train_loss, label='Train Loss')
plt.plot(valid_loss, label='Valid Loss')
plt.xlabel('Boosting Round')
plt.ylabel('Log Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.grid(True)
plt.show()
```

## Use `lgb.cv()`
LightGBM's `cv()` function also returns loss per iteration:

```py
cv_results = lgb.cv(
    params,
    train_set,
    num_boost_round=1000,
    nfold=5,
    metrics='multi_logloss',
    early_stopping_rounds=10
)

# plot the validation loss
plt.plot(cv_results['multi_logloss-mean'])
plt.title('CV Validation Loss')
plt.xlabel('Boosting Round')
plt.ylabel('Log Loss')
plt.grid(True)
plt.show()
```

# LightGBM

## lgb python docs
https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.cv.html#lightgbm.cv

## lgb best practices
https://www.linkedin.com/advice/0/what-best-practices-using-lightgbm-gradient-boosting-g0lye

## lgb dataset
when we call `dataset`, it will:
- bundle sparse features
- bin continuous features into histograms, prevent creation of histogram bins that are too small (`min_data_in_bin`)
- dropping features which are guaranteed to be uninformative (for example, features which are constant)

### missing values
- LightGBM offers in-built options for handling missing values
- set the parameter accordingly `use_missing=True`

### categorical features
- LightGBM offers in-built options for encoding categorical features
- specify which features are categorical by using the `categorical_feature` parameter in `dataset`
- convert categorical columns to a categorical data type in pandas before splitting data into training and test sets
- take advantage of LightGBM's internal optimizations for categorical features rather than manually encoding these features

### early_stopping_round
Use early stopping to prevent overfitting

https://github.com/microsoft/LightGBM/issues/5196
- option 1: set `early_stopping_round` in `params` argument
- option 2: passing `early_stopping()` callback via `callbacks` argument
```py
model = lgb.train(
    params={**params, 'early_stopping_round': 3},
    train_set=train_set,
    num_boost_round=10,
    valid_sets=[valid_set],
    ...
)

bst_1 = lgb.train(
    params=params,
    train_set=train_set,
    num_boost_round=10,
    valid_sets=[valid_set],
    callbacks=[
        lgb.early_stopping(stopping_rounds=3),
        lgb.log_evaluation(1)
    ]
)
```

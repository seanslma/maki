# Imbalanced

## imbalanced data - should i use `smote`
- https://mindfulmodeler.substack.com/p/dont-fix-your-imbalanced-data
- https://mindfulmodeler.substack.com/p/imbalanced-data-do-nothing-should

Problem:
- oversampling, will break calibration
- undersampling, will lost some information

Solutions:
- weight data points: give underrepresented data points a higher and overrepresented a lower weight
  - lgb: `sample_weight` and `class_weight = balanced` in classification
- use cost-sensitive machine learning to train models
- do threshold tuning on validation data
- smote works for a weak classifier
- undersampling for extremely large data and assigned larger weights to the sampled examples

## lightgbm imbalanced data
```py
model = lgb.train(
    params={'class_weight': 'balanced'},
    train_set=train_data,
    valid_sets=valid_sets,
    num_boost_round=num_boost_round,
)
```

## xgboost imbalanced data
https://xgboosting.com/xgboost-imbalanced-multi-class-classification-set-sample_weight-using-compute_sample_weight/
```py
from sklearn.utils import compute_sample_weight
sample_weight = compute_sample_weight('balanced', y_train)
train_data = xgb.DMatrix(
    data=X_train,
    label=y_train,
    weight=sample_weight,
)

# sklearn
model = XGBClassifier(random_state=42)
model.fit(X_train, y_train, sample_weight=sample_weight)
```

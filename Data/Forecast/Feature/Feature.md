# Feature

## time series features
- `observed features` can only be lagged to the latest available date - so in forecast we have and can use these features
- `forecast features` can be included directly or lagged, as long as they are available at time of forecasting

## Feature importance assessment
Feature’s relative importance can be assessed through two approaches:
- Maybe first use `featurewiz-polars`
- Shapley (python package `shap`) decompositions
- Marginal performance loss through feature removal

## feature selection
Best approach: use `featurewiz` to reduce feature size and then use `shap` to explain feature importance.

Featurewiz: Recursive XGBoost Feature Selection
- Automated feature selection
- Extensive feature engineering
```py
import featurewiz as fw
wiz = fw.FeatureWiz(verbose=1)
X_train, y_train = wiz.fit_transform(train[preds], train[target])
X_test = wiz.transform(test[preds])
```
Featurewiz-Polars: https://github.com/AutoViML/featurewiz_polars/tree/main
```py
from featurewiz_polars import FeatureWiz

# Initialize FeatureWiz for classification
wiz = FeatureWiz(
    model_type="Classification",
    estimator=None,
    corr_limit=0.7,
    category_encoders='onehot',
    classic=True,
    verbose=0,
)

# Fit and transform the training data
X_transformed, y_transformed = wiz.fit_transform(X_train, y_train)

# Transform the test data
X_test_transformed = wiz.transform(X_test)

# Transform the test target variable
y_test_transformed = wiz.y_encoder.transform(y_test)

# View results
print("Selected Features:")
print(wiz.selected_features)
# Example Output: ['col1', 'col2', 'category_A', 'category_B']

print("\nTransformed DataFrame head:")
print(X_transformed.head())
# Example Output: Polars DataFrame with only the selected features
```


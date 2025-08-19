# feature selection
pros and cons of different methods:
- https://www.paypalobjects.com/ecm_assets/Feature%20Selection%20WP-PP-v1.pdf
- voting: time consuming
- union: leading to to many features with many methods
- union of xgb, lgb and ctb: best result with low compution time

links:
- https://neptune.ai/blog/feature-selection-methods
- https://www.kaggle.com/code/prashant111/comprehensive-guide-on-feature-selection/notebook
- https://www.kaggle.com/code/kanncaa1/feature-selection-and-data-visualization
- methods: https://journalofbigdata.springeropen.com/articles/10.1186/s40537-024-00905-w

good disscusion:
- https://www.reddit.com/r/datascience/comments/1gsa6aj/lightgbm_feature_selection_methods_that_operate
- suggest `Permutation Importance`
- others: NFE and then RFE
- Correlation-based feature selection with Mutual Information is a good starting point, LightGBM can handle it efficiently

three widely used feature selection methods:
- ANOVA
- Mutual Information
- Recursive Feature Elimination

use model build-in importance feature:
- xgboost
- lightgbm
- random forrest

## Simple methods
### Variance Threshold
Remove constant/near-constant features:
```py
from sklearn.feature_selection import VarianceThreshold
X_reduced = VarianceThreshold(threshold=0.01).fit_transform(X)
```

### Correlation Filter
Remove features with low target correlation:
- only apply to linear relationship
- simple but less effective compared to univariate selection
- reducing features helps explainability. But dropping them via correlations will just lead to loss of potentially useful features
```py
# Calculate correlations
corr = df.corr()['target'].sort_values(ascending=False)
print(corr)
```

Remove highly correlated features (>0.95):
```py
import pandas as pd
corr_matrix = X.corr().abs()
upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
)
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
X_filtered = X.drop(to_drop, axis=1)
```

### vif for numeric features
  - Measure multicollinearity: how much a feature is linearly correlated with other features
  - Useful for linear models (e.g., linear regression), where multicollinearity can harm interpretability or inflate variance
  - For tree-based models (like LightGBM, XGBoost), multicollinearity is not usually a problem, since trees can handle correlated features
  - In real world, the very best variable could be extremely highly correlated with all the other variables -- you might drop it based on vif scores

### pearson corr vs vif
- corr().abs(), using pearson correlation, is faster and simpler, great for quick pairwise filtering
- vif is more robust for detecting multicollinearity, especially in linear models.
- both are not good for tree based models like xgboost


## Filter methods
- `f_classif` for numerical features and a categorical target
- `chi-squared` for categorical features and a categorical target

### Univariate Selection
- for regression problems: `f_regression`
- for classification problems: `f_classif`
- for catagrical features: ``
- doesn't consider feature interactions

select the best features:
```py
from sklearn.feature_selection import SelectKBest, f_classif
# select top 500 features for classification using ANOVA F-value between each feature and target
selector = SelectKBest(score_func=f_classif, k=500)
selected = selector.fit_transform(X_train, y_train)
```

calculate scores for all features:
```py
selector = SelectKBest(score_func=chi2, k=10)
fit = selector.fit(X, y)
f_scores = pd.DataFrame({'feature': X.columns, 'score': fit.scores_})
print(f_scores.nlargest(10, 'score'))
```

### Nonlinear Univariate
- It's slow: https://github.com/scikit-learn/scikit-learn/issues/6904
- It has an inherent n.log(n) cost per feature as long as it's using exact nearest neighbors.
```py
from sklearn.feature_selection import mutual_info_regression, mutual_info_classif
mi_scores = mutual_info_regression(X, y, njob=-1, discrete_features=False, random_state=42)
mi_scores = mutual_info_classif(X, y, njob=-1, discrete_features=False, random_state=42)
```

## Wrapper methods
- use a machine learning model to evaluate the performance of different subsets of features

### Permutation Importance
Measures drop in model performance when each feature is shuffled
- can be slow
```py
# Permutation Importance example
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

# Train a model, Random Forest is a great choice as it's a powerful tree-based model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X.to_pandas(), y.to_pandas())

# Calculate Permutation Importance on the test set to get a more reliable estimate
perm = permutation_importance(model, X.to_pandas(), y.to_pandas(), n_repeats=10, random_state=13)

# Get and sort the `perm.importances_mean` attribute that gives the average importance score
df = pl.DataFrame({
    'feature': X.columns,
    'perm_score': perm.importances_mean,
    'perm_score_std': perm.importances_std,
}).sort('perm_score', descending=True)
print(df)
```

### Recursive Feature Elimination (RFE)
https://machinelearningmastery.com/rfe-feature-selection-in-python/

RFE works by searching for a subset of features by starting with all features in the training dataset and successfully removing features until the desired number of features reached.
- Too slow for a huge amount of features

```py
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
# Create a sample dataset
X, y = make_classification(
  n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=42
)
# Initialize the model and RFE selector
model = LogisticRegression()
rfe_selector = RFE(estimator=model, n_features_to_select=5, step=1)
# Fit RFE
rfe_selector = rfe_selector.fit(X, y)
# Get the selected features
selected_features = rfe_selector.support_
print(f'Selected features: {selected_features}')
```

## Embedded methods
- force the coefficients of less important features to become exactly zero
- larger `alpha` leads to heavier penalty. 0-no regularization, 0.01-light, 1-strong, 100-very strong

Lasso (L1) regularization:
- A linear model with linear relationships between features and target.
- Shrinks some coefficients to zero, performing explicit feature selection based on linear correlations.
- Sensitive to multicollinearity — often picks one feature among correlated groups.

```py
from sklearn.linear_model import Lasso
from sklearn.datasets import make_regression
# Create a sample dataset with some irrelevant features
X, y = make_regression(n_samples=100, n_features=20, n_informative=5, random_state=42)
# Initialize and train the Lasso model
lasso = Lasso(alpha=0.01)
lasso.fit(X, y)
# Features with a coefficient of 0 are not important
print(lasso.coef_)
```

Auto feature selection:
`BorutaPy`: A Robust Feature Selection Algorithm
- can be computationally expensive

Time series feature generation:
- `TSFresh` can automatically extract and filter useful time series features based on statistical tests
- `Featuretools` can help with automated feature generation + selection (more for relational data, but flexible)

## feature importance
Effect of Correlated Features:
- Lasso tends to pick one feature out of a correlated group and zero out the rest.
- Boosted trees often split on multiple correlated features, sharing importance among them.

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

# create SHAP explainer (for tree base models)
explainer = shap.TreeExplainer(model.regressor)

# sample 50% of the data to speed up the calculation
rng = np.random.default_rng(seed=785412)
sample = rng.choice(X_train.index, size=int(len(X_train)*0.5), replace=False)
X_train_sample = X_train.loc[sample, :]
shap_values = explainer.shap_values(X_train_sample)

# shap summary report (top 10 features only)
shap.initjs()
shap.summary_plot(shap_values, X_train_sample, max_display=10, show=False)
fig, ax = plt.gcf(), plt.gca()
ax.set_title('SHAP Summary plot')
ax.tick_params(labelsize=8)
fig.set_size(10, 4.5)
```







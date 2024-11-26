# Parameters

## subsample
- `subsample`: the fraction of the training samples (randomly selected rows) that will be used to train each tree

## colsample_by*
https://medium.com/analytics-vidhya/xgboost-colsample-by-hyperparameters-explained-6c0bac1bdc1
- `colsample_bytree`: the fraction of features (randomly selected columns) when new tree is created
- `colsample_bylevel`: random subsample of columns when every new level is reached
- `colsample_bynode`: random subsample of columns based on every split (left or right swerve)

## grid search
```py
from xgboost import XGBRegressor
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV

model = XGBRegressor()
parameters = {
    'max_depth': [3, 4, 6, 8, 10],
    'learning_rate': [0.01, 0.05, 0.1, 0.2, 0.3],
    'n_estimators': [100, 300, 500, 700, 900, 1000],
    'colsample_bytree': [0.3, 0.5, 0.7]
}
cv_split = TimeSeriesSplit(n_splits=4, test_size=100) # Coefficient of Variation

grid_search = GridSearchCV(estimator=model, cv=cv_split, param_grid=parameters)
grid_search.fit(X_train, y_train)
```

Note that:
- GridSearchCV: Iterates over all combinations of hyperparameters in the grid. Can be computationally expensive, especially for large parameter grids and complex models.   
- RandomizedSearchCV: For a more efficient approach, consider using RandomizedSearchCV, which samples a fixed number of hyperparameter combinations randomly.   
- Bayesian Optimization: More advanced techniques like Bayesian optimization can further optimize the search process by intelligently selecting the next hyperparameter combination to evaluate.

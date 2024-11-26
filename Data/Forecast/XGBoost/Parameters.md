# Parameters

## subsample
- `subsample`: the fraction of the training samples (randomly selected rows) that will be used to train each tree

## colsample_by*
https://medium.com/analytics-vidhya/xgboost-colsample-by-hyperparameters-explained-6c0bac1bdc1
- `colsample_bytree`: the fraction of features (randomly selected columns) when new tree is created
- `colsample_bylevel`: random subsample of columns when every new level is reached
- `colsample_bynode`: random subsample of columns based on every split (left or right swerve)

## grid search

GridSearchCV:
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

RandomizedSearchCV:
```py
import numpy as np
import pandas as pd
from scipy.stats import randint
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = RandomForestClassifier(random_state=42)

# Define the hyperparameter search space
param_dist = {
    'n_estimators': randint(10, 200),
    'max_depth': randint(1, 20),
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 10),
    'bootstrap': [True, False]
}

# Create the RandomizedSearchCV instance
random_search = RandomizedSearchCV(
    estimator=model, 
    param_distributions=param_dist, 
    n_iter=100,    # number of samples
    cv=3,          # cross-validation folds
    verbose=2, 
    random_state=42, 
    n_jobs=-1,
)

# Fit the model
random_search.fit(X_train, y_train)

# Get the best hyperparameters
print(f"Best hyperparameters: {random_search.best_params_}")

# Get the best model and evaluate it on the test set
best_model = random_search.best_estimator_
test_score = best_model.score(X_test, y_test)
print(f"Test score: {test_score}")
```

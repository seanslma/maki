# Parameters

## subsample
- `subsample`: the fraction of the training samples (randomly selected rows) that will be used to train each tree

## colsample_by*
https://medium.com/analytics-vidhya/xgboost-colsample-by-hyperparameters-explained-6c0bac1bdc1
- `colsample_bytree`: the fraction of features (randomly selected columns) when new tree is created
- `colsample_bylevel`: random subsample of columns when every new level is reached
- `colsample_bynode`: random subsample of columns based on every split (left or right swerve)

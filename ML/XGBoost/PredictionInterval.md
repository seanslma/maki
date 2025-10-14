# Prediction Interval
https://cienciadedatos.net/documentos/py42-forecasting-prediction-intervals-machine-learning.html

## Bootstrapping
Prediction intervals are estimated based on bootstrapped residuals.
```py
from skforecast.model_selection import backtesting_forecaster
metric, predictions = backtesting_forecaster(
    forecaster = forecaster,
    y                  = data['Demand'],
    initial_train_size = len(data_train) + len(data_val),
    fixed_train_size   = False,
    steps              = 7,
    refit              = False,
    interval           = [10, 90],
    n_boot             = 1000,
    metric             = 'mean_squared_error',
    verbose            = False,
    show_progress      = True,
)
```

## Quantile regresion models

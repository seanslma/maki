# Uncertainty (Prediction) Interval 
Not Confident Interval: https://stats.stackexchange.com/questions/619860/are-prophets-uncertainty-intervals-confidence-intervals-or-prediction-interva

The default `uncertainty interval` is 80%.

https://www.mikulskibartosz.name/understanding-uncertainty-intervals-generated-by-prophet/
```py
m = Prophet(uncertainty_samples=1000, interval_width=0.95)
```

By default, Interval_width parameter is related to uncertainty in `trend` and `observation noise` only.
The uncertainty interval of the calculated seasonality is not taken into account.
But Prophet calculates it when we set the `mcmc_samples` parameter. 
```py
m = Prophet(uncertainty_samples=1000, mcmc_samples=1000, interval_width=0.95)
```

To see the uncertainty in seasonality we must do `full Bayesian sampling` by settting the `mcmc.samples`. 
The default value of 0 for `mcmc.samples` mans that it uses `maximum of posterior estimation`.

# Uncertainty (Prediction) Interval 
Not Confident Interval: https://stats.stackexchange.com/questions/619860/are-prophets-uncertainty-intervals-confidence-intervals-or-prediction-interva

https://www.mikulskibartosz.name/understanding-uncertainty-intervals-generated-by-prophet/
```py
m = Prophet(uncertainty_samples=1000, interval_width=0.95)
```

By default, the uncertainty interval of the calculated seasonality is not taken into account, 
but Prophet calculates it when we set the `mcmc_samples` parameter. 
```py
m = Prophet(uncertainty_samples=1000, mcmc_samples=1000, interval_width=0.95)
```

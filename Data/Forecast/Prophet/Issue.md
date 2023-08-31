# Issue

## Program stalls
https://github.com/facebook/prophet/issues/842

Too few data points lead to numeric singularity??? then use newton not L-BFGS. Other reasons???

## Trend issue
The trend can be completely wrong for long term forecast:
https://towardsdatascience.com/fixing-prophets-forecasting-issue-b473afe2cc70

## Optimization terminated abnormally. Falling back to Newton.
https://github.com/facebook/prophet/issues/1678

by disabling the Newton fallback, will will see all the errors from stanpy
```py
m = Prophet()
m.stan_backend.set_options(newton_fallback=False)
m.fit(df)
```
then catch the error:
```py
except RuntimeError as e: 
```

## Line search failed to achieve a sufficient decrease, no more progress can be made
https://discourse.mc-stan.org/t/line-search-failed-error/10163
```
Very small alpha (related to step size in line search) supports the assumption that the search direction is not pointing downhill.
You can also test running with smaller ODE solver tolerances.
```

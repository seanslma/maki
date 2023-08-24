# Prophet

Prophet will internally scale `y` before fitting the model so `y` does not need to be normalized.

For data without any seasonality or holiday effects, Prophet is just a piecewise linear regression, so it's not appropriate for these time series.

quick start:\
https://facebook.github.io/prophet/docs/quick_start.html#python-api

guide:\
https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-prophet-in-python-3

Implementing Facebook Prophet efficiently:\
https://towardsdatascience.com/implementing-facebook-prophet-efficiently-c241305405a3

"Prophet uses a decomposable time series model (Harvey & Peters 1990) with three main model components: trend, seasonality, and holidays.  They are combined in the following equation:

`y(t) = g(t) + s(t) + h(t) + e(t)`

Here g(t) is the trend function which models non-periodic changes in the value of the time series, s(t) represents periodic changes (e.g., weekly and yearly seasonality), and h(t) represents the effects of holidays which occur on potentially irregular schedules over one or more days. The error term e(t) represents any idiosyncratic changes which are not accommodated by the model; later we will make the parametric assumption that e(t) is normally distributed."

"For model fitting we use Stan’s L-BFGS to find a maximum a posteriori estimate."

## seasonality
```
m = Prophet(yearly_seasonality=False, weekly_seasonality=False, daily_seasonality=False)
m.add_seasonality(name='yearly', period=365.25, fourier_order=10)
m.add_seasonality(name='quarterly', period=365.25/4, fourier_order=10)
m.add_seasonality(name='monthly', period=30.5, fourier_order=10)
m.add_seasonality(name='weekly', period=7, fourier_order=10)
m.add_seasonality(name='daily', period=1, fourier_order=10)
```

## parameters
```
yearly_seasonality='auto',
weekly_seasonality='auto',
daily_seasonality='auto',
holidays=None,
seasonality_mode='additive',
seasonality_prior_scale=10.0,
holidays_prior_scale=10.0,
changepoint_prior_scale=0.05,
mcmc_samples=0,
interval_width=0.80,
stan_backend=None
```

### can be tuned
  - **changepoint_prior_scale**: [0.001, **0.05**, 0.5]
    * Parameter modulating the flexibility of the automatic changepoint selection.
    * Large values will allow many changepoints, possibly overfit, will produce wide uncertainty intervals
    * Small values will allow few changepoints, possibly underfit
  - **seasonality_prior_scale**: [0.01, **10**, 10]
    * Parameter modulating the strength of the seasonality model.
    * Larger values allow the model to fit larger seasonal fluctuations
    * Smaller values dampen the seasonality
    * Can be specified for individual seasonalities using add_seasonality.
  - **holidays_prior_scale**: [0.01, **10**, 10]
    * Parameter modulating the strength of the holiday
        components model, unless overridden in the holidays input.
  - **seasonality_mode**: 'additive' (default) or 'multiplicative'.

### may be tuned
  - **changepoint_range**: 0.8
    * Proportion of history in which trend changepoints will be estimated.
    * Defaults to 0.8 for the first 80%.
    * Not used if`changepoints` is specified.

### not be tuned
  - growth: linear
    * String 'linear', 'logistic' or 'flat'
    * to specify a linear, logistic or flat trend.
  - changepoints: None
    * List of dates at which to include potential changepoints.
    * If not specified, potential changepoints are selected automatically.
  - n_changepoints: 25
    * Number of potential changepoints to include.
    * Not used if input `changepoints` is supplied.
    * If `changepoints` is not supplied, then n_changepoints potential changepoints
        are selected uniformly from the first `changepoint_range` proportion of the history.
  - yearly_seasonality: auto
    * Fit yearly seasonality.
    * Can be 'auto', True, False, or a number of Fourier terms to generate.
  - weekly_seasonality: auto
    * Fit weekly seasonality.
    * Can be 'auto', True, False, or a number of Fourier terms to generate.
  - daily_seasonality: auto
    * Fit daily seasonality.
    * Can be 'auto', True, False, or a number of Fourier terms to generate.
  - holidays: None
    * pd.DataFrame with columns holiday (string) and ds (date type)
        and optionally columns lower_window and upper_window which specify a
        range of days around the date to be included as holidays.
        lower_window=-2 will include 2 days prior to the date as holidays. Also
        optionally can have a column prior_scale specifying the prior scale for
        that holiday.
  - mcmc_samples: Integer, if greater than 0, will do full Bayesian inference
        with the specified number of MCMC samples. If 0, will do MAP
        estimation.
  - interval_width: Float, width of the uncertainty intervals provided
        for the forecast. If mcmc_samples=0, this will be only the uncertainty
        in the trend using the MAP estimate of the extrapolated generative
        model. If mcmc.samples>0, this will be integrated over all model
        parameters, which will include uncertainty in seasonality.
  - uncertainty_samples: 1000
    * Number of simulated draws used to estimate uncertainty intervals.
    * Settings this value to 0 or False will disable uncertainty estimation and speed up the calculation.
  - stan_backend: str as defined in StanBackendEnum default: None - will try to
        iterate over all available backends and find the working one

## Neural Prophet
https://arxiv.org/pdf/2111.15397

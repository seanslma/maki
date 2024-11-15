# Forecast
- static / dynamic forecasting
- short term: 2-week lookahead
- long term

## data
Data aspects:
- missing data,
- trend,
- seasonality,
- volatility,
- drift and
- rare events.

https://neptune.ai/blog/arima-vs-prophet-vs-lstm

## methods
why does forecast combination work?
- https://scholar.cu.edu.eg/?q=amiratiya/files/m4-ijf.pdf
- average of diverse or comparable forecasts has a shorter distance to the true values compared to each of the forecast
- exclude forecasts that are considerably worse than the best ones in the pool, unless they are very diverse from the rest

## retrospect
- check accuracy each week
- target: minimize cost or forecast error?

## underfit and overfit
https://curiousily.com/posts/hackers-guide-to-fixing-underfitting-and-overfitting-models/

- underfit: high bias
- overfit: high variance
- mse (mean squared error) = variance + bias^2

## prediction intervals
https://otexts.com/fpp2/prediction-intervals.html

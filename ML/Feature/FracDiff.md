# Fractionally Differentiated Features

Fractionally Differentiated Features are a technique used to transform time series data in a way that
- reduces short-term noise and
- preserves long-term trends (memory)

Example, fractional differencing $y_t - \gamma y_{t-1}$ where $\gamma$ is a fractional value like 0.5.

Why use fractional differencing?
- Preserve Long-Term Trends: Fractional differencing allows you to remove short-term noise while maintaining the long-range dependencies that are crucial for accurate forecasts, especially in financial, economic, or stock market data.
- Stationarity Without Over-Differencing: It can help make the series stationary without over-differencing, which can lead to loss of information. For example, first differencing (subtracting one previous observation) may eliminate too much of the useful data, but fractional differencing avoids this problem.
- Better Model Performance: For certain time series models, like machine learning models (LightGBM, XGBoost), maintaining long-term dependencies can be crucial for predictive accuracy. Fractional differencing can improve model performance by preserving these important correlations.

Note that integer differencing will:
- make the data stationary,
- it also often results in over-differencing (no memory), which can remove valuable information and hurt model performance

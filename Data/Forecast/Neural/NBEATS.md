# NBEATS

NBEATS (Neural Basis Expansion Analysis for Time Series) is a neural network-based model specifically designed for time series forecasting.
- Focuses on: Capturing non-linear relationships and complex patterns in time series data.
- Architecture: It typically consists of a stack of fully connected layers and/or convolutional layers, allowing it to capture complex patterns in time series data.
- Training: NBEATS is trained using gradient descent-based optimization methods, where the model parameters are updated iteratively to minimize a predefined loss function.
- Interpretability: While neural networks can be challenging to interpret due to their complex architecture, techniques like attention mechanisms in NBEATS can help understand which parts of the input sequence are important for the predictions.

## Strengths
- Can handle complex seasonality and trends.
- Offers good accuracy for short-term forecasting.
- Can incorporate past covariates (additional data points that might influence the forecast).
- Can be extended to handle multivariate forecasting (multiple time series at once).

## Weaknesses
- Requires more data for training compared to XGBoost.
- Can be computationally expensive to train, especially for large datasets.
- Interpretability of the model can be challenging.

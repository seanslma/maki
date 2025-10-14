# TCN

TCN (Temporal Convolutional Network) is a convolutional neural network (CNN) architecture used for time series forecasting.

## Strengths
- Focuses on long-range dependencies: TCNs excel at capturing these dependencies in time series data due to their convolutional layers, making them well-suited for tasks where long-term patterns are important (e.g., stock price trends).
- Potentially faster training: TCNs might be computationally less expensive to train than LSTMs for some datasets, especially for very long sequences.

## Weaknesses
- May struggle with complex seasonality: While TCNs can handle some seasonality, they might not be as adept at capturing intricate seasonal patterns compared to LSTMs.
- Hyperparameter tuning: TCNs can still require careful hyperparameter tuning to achieve optimal performance.
- Less established: Compared to LSTMs, TCNs are a relatively newer architecture, potentially leading to fewer resources and established practices.

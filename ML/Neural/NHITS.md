# NHITS

NHITS (Neural Hierarchical Interpolation for Time Series) Forecasting. 

N-HITS is particularly suitable for `hierarchical time series` forecasting tasks, 
- where the data can be naturally decomposed into multiple levels of aggregation
- such as sales data at different geographical levels or product hierarchies

## how it works
- It utilizes a special technique called hierarchical interpolation to efficiently forecast future values. This technique breaks down the forecasting process into smaller components focusing on different frequencies within the data.
- Additionally, NHITS employs multi-rate input processing, meaning it can analyze data at various granularities to capture both short-term and long-term patterns.

## Strengths
- **Accuracy:** NHITS boasts high accuracy, especially for short-term forecasting, often outperforming established models like LSTMs.
- **Complex seasonality:**  It excels at capturing intricate seasonal patterns and trends in time series data.
- **Efficiency:** Compared to other high-accuracy models, NHITS can be computationally efficient, requiring less training time in some cases. 
- **Flexibility:** It can handle multivariate forecasting (multiple time series at once) and incorporate past covariates (additional data points that might influence the forecast).

## Weaknesses
- **Data requirements:** While generally efficient, NHITS might still require more data for training compared to simpler models.  
- **Interpretability:** Similar to other neural networks, understanding how NHITS arrives at predictions can be challenging.

## help
- A research paper on NHITS: [https://arxiv.org/abs/2201.12886](https://arxiv.org/abs/2201.12886)
- Documentation on NHITS implementation: [https://www.nixtla.io/](https://www.nixtla.io/)

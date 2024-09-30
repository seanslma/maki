# Arima

## SARIMAX example 
https://github.com/SamWachira/Electricity-Demand-Forecasting/blob/main/Time_Series_Electricity.ipynb

## ARIMAX (autoregressive integrated moving average with exogenous variables) 
- The ARIMAX model is an extension of the standard ARIMA model, and 
- it allows for the inclusion of one or more exogenous variables in the model equation. 
- The ARIMAX model can be estimated using maximum likelihood estimation, and 
- the parameters of the model can be estimated using numerical optimization techniques.

## components
- Auto-Regressive (AR):
  - determine the present value based on historical values
  - only for data with stationary trend
- Moving Average (MA):
  - smoothen variations to reveal the underlying trend
  - only for data with stationary trend
- Integrated (I):
  - integrate the AR and MA elements by computing differences between current and past values
  - transform the dataset into a stationary trend
 
## parameters
- p: the number of past values considered for the AR component
- q: the number of moving averages applied
- d: the number of past values subject to differentiation

## limit
lacking adaptability

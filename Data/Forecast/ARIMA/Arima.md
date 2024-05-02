# Arima

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

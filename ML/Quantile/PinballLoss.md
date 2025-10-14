# Pinball loss

## pinball loss in Quantile Regression
- https://mindfulmodeler.substack.com/p/how-i-made-peace-with-quantile-regression
```py
diff = y_true - y_pred
pinball_loss = np.maximum(quantile * diff, (quantile - 1) * diff).mean()
```
- assume `quantile = 0.1` and `y_true = 100`
- if `y_pred = 97` (y_pred < y_true, `underpredict`): loss = 0.1 * (100 - 97) = 3 * 0.1
- if `y_pred = 103` (y_pred > y_true, `overpredict`): loss = (1 - 0.1) * (103 - 100) = 3 * 0.9
- loss is asymmetric, more penalty for overpredict
- expect the model to underpredict 90% of the time and overpredict 10% of the time
- the predict mean is below the true - equivalent to the 10% quantile

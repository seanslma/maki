# example

https://medium.com/mlearning-ai/forecast-with-xgboost-model-in-python-87d4b6cada98
```py
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

#create example data
X, y = make_classification(
    n_samples=100,
    n_informative=5,
    n_classes=2,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#training
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.01,
    subsample=0.75,
    colsample_bytree=1,
    max_depth=3,
    gamma=0,
)
model.fit(
    X_train, y_train,
    eval_set=[(X_train, y_train), (X_test, y_test)],
    early_stopping_rounds=20,
)

pred = model.predict(X_test)

#display forecast
plt.figure(figsize=(10, 5), dpi=80)
x_ax = range(len(y_test))
plt.plot(x_ax, y_test, label="test")
plt.plot(x_ax, pred, label="predicted")
plt.title('XGB prediction')
plt.legend()
plt.show()

#save model
model.save_model('model_sklearn.json')

#load model
model2 = xgb.XGBRegressor()
model2.load_model('model_sklearn.json')
```

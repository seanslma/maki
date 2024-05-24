# StandardScalar

## `fit_transform` issue
will convert `Float32` to `float64`
```py
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# will convert to float64
train_eng[numerical_features] = scaler.fit_transform(train_eng[numerical_features])
```

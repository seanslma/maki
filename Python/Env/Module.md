# Module

## tools
  - Redis: Redis' access libraries
  - ElasticSearch: data search engine

## win32com
install pywin32 for win32com:
  python -m pip install pywin32

## Plotly and Cufflinks
cufflinks is the link between plotly and pandas.
```py
import pandas as pd
import cufflinks as cf
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
```

## Geographical Plotting
```py
import plotly.plotly as py
import plotly.grath_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

layout = dict(geo={'scope':'usa'})
choromap = go.Figure(data=[data], layout=layout)
iplot(choromap)
```
## patsy
Patsy is a Python library for describing statistical models (especially linear models) with a small string-based "formula syntax".

```py
import patsy
y, X = patsy.dmatrices('y ~ x0 + x1', df)
coef, resid, _, _ = np.linalg.lstsq(X, y)
coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)

#transferm
y, X = patsy.dmatrices('v2 ~ C(key2)', df) #categorical data
y, X = patsy.dmatrices('y ~ I(x0 + x1)', df)
y, X = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', df)
y, X = patsy.dmatrices('y ~ standardize(x0) + center(x1)', df)
new_X = patsy.build_design_matrices([X.design_info], new_df)
```

## statsmodels
Some kinds of models found in statsmodels include:
  * Linear models, generalized linear models, and robust linear models
  * Linear mixed effects models
  * Analysis of variance (ANOVA) methods
  * Time series processes and state space models
  * Generalized method of moments
```py
import statsmodels.api as sm
import statsmodels.formula.api as smf

#ordinary least squares linear regression
model = sm.OLS(y, X)
results = model.fit() #results.params,results.summary()

results = smf.ols('y ~ col0 + col1 + col2', data=data).fit()

#AR: time series analysis
model = sm.tsa.AR(values)
results = model.fit(MAXLAGS)
```

## scikit-learn
```py
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
```

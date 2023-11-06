# sample

## down sample
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
```py
dfsum = df.resample('A-JUN', label='left').sum()  #annual sum
dfsum = df.resample('A-JUN', label='left').mean() #annual average
```

## up sample
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.interpolate.html
```py
dfupsmp = df.resample('D').interpolate(method='linear')
dfupsmp = df.resample('D').interpolate(method='spline', order=2)
```

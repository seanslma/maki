# DateTime

## combine `date`  and `time` into one col
```py
df = df.assign(ts=lambda x: pd.to_datetime(x['date'].astype(str) + ' ' + x['time'].astype(str)))
```

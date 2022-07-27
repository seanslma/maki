# Conversion

## pd.Timestamp to Quarter datetime (str)
```
s.dt.to_period('Q').dt.to_timestamp()
s.dt.to_period('Q').dt.strftime('%Y-%m-%d')
```


## Quarter-Year to pd.Timestamp
```
qs = df['Quarter'].str.replace(r'(Q\d) (\d+)', r'\2-\1')
ymd_quarter = pd.PeriodIndex(qs, freq='Q').to_timestamp()
ymd_quarter = pd.to_datetime(qs, errors='coerce')
```

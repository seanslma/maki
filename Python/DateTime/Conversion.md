# Conversion

## pd.Timestamp to Quarter datetime (str)
```
s.dt.to_period('Q').dt.to_timestamp()
s.dt.to_period('Q').dt.strftime('%Y-%m-%d')
```

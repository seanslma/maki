# Conversion

## Valid `freq` values
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

## pd.Timestamp to Quarter datetime (str)
```
s.dt.to_period('Q').dt.to_timestamp()
s.dt.to_period('Q').dt.strftime('%Y-%m-%d')

per = pd.Timestamp('2023-07-01').to_period('Q-DEC') #cal year quarter
per = pd.Timestamp('2023-07-01').to_period('Q-JUN') #fin year quarter
```

## Quarter-Year to pd.Timestamp
```
qs = df['Quarter'].str.replace(r'(Q\d) (\d+)', r'\2-\1')
ymd_quarter = pd.PeriodIndex(qs, freq='Q').to_timestamp()
ymd_quarter = pd.to_datetime(qs, errors='coerce')
```

## pd.Timestamp to cal/fin year
```
per = pd.Timestamp('2023-07-01').to_period('A-DEC') #cal year
per = pd.Timestamp('2023-07-01').to_period('A-JUN') #fin year
```

## DateOffset
```
pd.DateOffset(months=12) #within the same day
>>> pd.Timestamp("2021-08-25") - pd.DateOffset(months=1)
Timestamp('2021-07-25 00:00:00')

pd.tseries.frequencies.to_offset('A-JUN') #offset to the period start/end
>>> pd.Timestamp("2021-08-25") - pd.tseries.frequencies.to_offset('1M')
Timestamp('2021-07-31 00:00:00')
```

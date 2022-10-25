# Conversion

## Valid `freq` values
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

## pd.Timestamp to month datetime
```
s.dt.to_period('M').dt.to_timestamp()

df['mth'] = df['dt'].astype('datetime64[M]')
```

## pd.Timestamp to Quarter datetime (str)
```
s.dt.to_period('Q').dt.to_timestamp()
s.dt.to_period('Q').dt.strftime('%Y-%m-%d')

per = pd.Timestamp('2023-07-01').to_period('Q-DEC') #cal year quarter
per = pd.Timestamp('2023-07-01').to_period('Q-JUN') #fin year quarter
```

## pd.Timestamp to cal/fin year
```
per = pd.Timestamp('2023-07-01').to_period('A-DEC') #cal year
per = pd.Timestamp('2023-07-01').to_period('A-JUN') #fin year
```

## Quarter-Year to pd.Timestamp
```
qs = df['Quarter'].str.replace(r'(Q\d) (\d+)', r'\2-\1')
ymd_quarter = pd.PeriodIndex(qs, freq='Q').to_timestamp()
ymd_quarter = pd.to_datetime(qs, errors='coerce')
```

## DateOffset
```
#within the same day
>>> pd.Timestamp("2021-08-25") - pd.DateOffset(months=1)
Timestamp('2021-07-25 00:00:00')

#offset to the period end
>>> pd.Timestamp("2021-07-01") - pd.tseries.frequencies.to_offset('A-JUN')
Timestamp('2022-06-30 00:00:00')

#offset to the period start
>>> pd.Timestamp("2021-07-01") + pd.tseries.frequencies.to_offset('AS-JUL')
Timestamp('2022-07-01 00:00:00')

#offset to the period start: Cal Year
>>> pd.Timestamp("2021-01-01") + pd.tseries.frequencies.to_offset('AS-JAN')
Timestamp('2022-01-01 00:00:00')
```

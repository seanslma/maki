# DateOffset

## normalize
```
>>> pd.date_range('2022-08-01 23:59:59', '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'))
DatetimeIndex(['2022-08-01 23:59:59'], dtype='datetime64[ns]', freq='MS')

>>> pd.date_range('2022-08-01 23:59:59', '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'), normalize=True)
DatetimeIndex(['2022-08-01', '2022-09-01'], dtype='datetime64[ns]', freq='MS')

>>> pd.date_range(pd.Timestamp('2022-08-01 23:59:59') + pd.DateOffset(days=0, normalize=True), '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'))
DatetimeIndex(['2022-08-01', '2022-09-01'], dtype='datetime64[ns]', freq='MS')
```

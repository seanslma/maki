# tseries

## offset
```python
from pandas.tseries.offsets import Day, MonthEnd
offset = MonthEnd()
ts.groupby(offset.rollforward).mean()
ts.resample('M').mean()#faster
```

## period
```python
prd = pd.Period(2007, freq='A-DEC')
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
prd.asfreq('M', how='start') #convert to another period
```

## resample
```python
ts.resample('M').mean()
ts.resample('M', kind='period').mean()

#up-sampling
df.resample('D').asfreq()
df.resample('D').ffill(limit=2)

#down-sampling (aggregate)
ts.resample('5min', closed='right').sum()
ts.resample('5min', closed='right', label='right', loffset='-1s').sum()

#Open-High-Low-Close (OHLC) resampling
ts.resample('5min').ohlc()

#multiple key
df2 = pd.DataFrame({'time': times.repeat(3),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N * 3.)})
time_key = pd.TimeGrouper('5min')
df2 = df.set_index('time').groupby(['key', time_key]).sum()
df2 = df2.reset_index()
```

## moving window
```python
df['val'].rolling(250).mean()
df['val'].rolling(250, min_periods=10).std()
df['val'].expanding().mean()

#exponentially weighted moving average
df['val'].ewm(span=30).mean()
 
#binary moving window
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()
corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
corr = returns.rolling(125, min_periods=100).corr(spx_rets) #for all cols

#user-defined moving window
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
```

## timezone
```python
import pytz
pytz.common_timezones[-5:]
tz = pytz.timezone('America/New_York')

#from naive to localized
ts_utc = ts.tz_localize('UTC')
#converted to another time zone
ts_utc.tz_convert('America/New_York')

#localize timestamp
stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc = stamp.tz_localize('utc')
stamp_utc.tz_convert('America/New_York')
```

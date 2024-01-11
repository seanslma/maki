# perf (I)

- https://scipy.github.io/old-wiki/pages/PerformanceTips
- https://llllllllll.github.io/principles-of-performance/index.html
- https://speakerdeck.com/pycon2018/jake-vanderplas-performance-python-seven-strategies-for-optimizing-your-numerical-code
- https://speakerdeck.com/nnja/nina-zakharenko-the-basics-of-memory-management-in-python-north-bay-python-2018
- https://software.intel.com/en-us/articles/large-matrix-operations-with-scipy-and-numpy-tips-and-best-practices
- http://conference.scipy.org/proceedings/scipy2018/pdfs/anton_malakhov.pdf
- http://conference.scipy.org/proceedings/scipy2017/pdfs/oleksandr_pavlyk.pdf

## example
Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects

https://realpython.com/fast-flexible-pandas

```
Tariff Type   Cents per kWh   Time Range
Peak          28              17:00 to 24:00
Shoulder      20              07:00 to 17:00
Off-Peak      12              00:00 to 07:00
```

```
method        time
.itertuples() 713 ms
.apply()      272 ms
.isin()        10 ms
pd.cut()        3 ms
np.digitize()   2 ms
```

### DateTime
```py
# change String Datetime to Timestamp
df['date_time'] = pd.to_datetime(df['date_time'])
# 50x faster when explicitly using format
df['date_time'] = pd.to_datetime(df['date_time'], format='%d/%m/%Y %H:%M:%S')
```

### .isin()
```py
# define hour range Boolean arrays
peak_hours = df.index.hour.isin(range(17, 24))
# apply tariffs to hour ranges
df.loc[peak_hours, 'cost_cents'] = df.loc[peak_hours, 'energy_kwh'] * 28
```

### pd.cut()
```py
cents_per_kwh = pd.cut(
    x=df.index.hour,
    bins=[0, 7, 17, 24],
    include_lowest=True,
    labels=[12, 20, 28]
).astype(int)
df['cost_cents'] = cents_per_kwh * df['energy_kwh']
```

### np.digitize()
```py
prices = np.array([12, 20, 28])
bins = np.digitize(df.index.hour.values, bins=[7, 17, 24])
df['cost_cents'] = prices[bins] * df['energy_kwh'].values
```

### HDFStore
```py
# save to datastore
ds = pd.HDFStore('C:/ds1.h5')
ds['df1'] = df
ds.close()
# get from datadtore
ds = pd.HDFStore('C:/ds1.h5','r')
df = ds['df1']
ds.close()
```

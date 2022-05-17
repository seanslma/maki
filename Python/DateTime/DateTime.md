# DateTime

[Dealing with datetimes like a pro in Pandas](https://medium.com/jbennetcodes/dealing-with-datetimes-like-a-pro-in-pandas-b80d3d808a7f)

## pywintypes.datetime
```python
import pywintypes
from datetime import datetime

#check if dt is pywintypes.datetime
isinstance(dt, pywintypes.TimeType)

#change pywintypes.datetim to datetime
dt2 = datetime.fromtimestamp(timestamp=dt.timestamp(), tz=dt.tzinfo)
```

## datetime
```python
import datetime
de = datetime.date(year=2017, month=10, day=24)
tm = datetime.time(hour=4, minute=3, second=10, microsecond=7199)
dt = datetime.datetime(year=2017, month=10, day=24, \
        hour=4, minute=3, second=10, microsecond=7199)
td = datetime.timedelta(days=3, minutes = 55)
dt2 = dt + td

#string to datetime
dt = datetime.strptime('2020-01-01 13:00:10', '%Y-%m-%d %H:%M:%S')
```

## datetime64
```python
dt64 = np.datetime64(5, 'ns') 
dt64 = np.datetime64(1508887504, 's')
dt64 = np.datetime64('2017-10-24')
dt64 = np.datetime64('2017-10-22T12:35:40.123')

td64 = np.timedelta64(2, 'h')
td64 = np.timedelta64(5, 'D')
td64 = dt64_1 - dt64_2
```

## timedelta
```python
np.timedelta64(300000000000, 'ns')==timedelta(seconds=300)
#return false

np.timedelta64(300000000000, 'ns')==pd.Timedelta(hours=1/12)
#return true
```

## Timestamp
```python
ts = pd.Timestamp(1239.1238934) #defautls to nanoseconds
ts = pd.Timestamp(1239.1238934, unit='D')
ts = pd.Timestamp('2017-10-24 05')
ts = pd.Timestamp('today')
ts = pd.Timestamp.now()

ts = pd.Timestamp(2017, 1, 1, 12)
ts = pd.Timestamp(year=2017, month=1, day=1, hour=12)

ts = pd.to_datetime('2017-10-24 05')
ts = pd.to_datetime('today')
dt64_idx = pd.to_datetime(['2017-1-1', '2017-1-2'])

# dt to dt64 and ts
dt64 = np.datetime64(dt)
ts = pd.Timestamp(dt) # or pd.to_datetime(dt)

#dt64 to dt and ts
unix_epoch = np.datetime64(0, 's')
one_second = np.timedelta64(1, 's')
seconds_since_epoch = (dt64 - unix_epoch) / one_second
dt = datetime.utcfromtimestamp(seconds_since_epoch)

ts = pd.Timestamp(dt64)

#ts to dt and dt64
dt = ts.to_pydatetime()
dt64 = ts.to_datetime64()
```

## timestamp to date
```python
#timestamp series to datetime.date
ts.apply(lambda x: x.date())

ts.dt.to_pydatetime()

#timestampIndex to datetime.date
tsIndex.date

dt64 = np.datetime64('2012-05-01T01:00:00.000000')

#dt64 to ts
ts = pd.Timestamp(dt64)

#dt64 to dt
seconds = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
dt = datetime.utcfromtimestamp(seconds)

#dt to dt64
dt64 = np.datetime64(dt)
```

## dt, dt64, ts to string
```python
#dt to str
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
datetime.now().strftime('%#d/%m/%Y %H:%M:%S') #without zero-padded day in windows
datetime.now().strftime('%-d/%m/%Y %H:%M:%S') #without zero-padded day in linux
 
dt = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S') #str to datetime

#ts to str
ts.strftime('%Y-%m-%d')
df.timestamp.dt.strftime('%Y-%m-%d')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S.%f', utc=False) #str to ts
df['date'] = pd.to_datetime(df['date'], unit='s') #unix time to dt64
```

## fg
```python
#add days
dt = datetime.now()
dt2 = dt + timedelta(days=1)

#convert datetime to string
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#without zero-padded day in windows
datetime.now().strftime('%#d/%m/%Y %H:%M:%S')
#without zero-padded day in linux
datetime.now().strftime('%-d/%m/%Y %H:%M:%S')

#convert string to datetime
date = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S.%f', utc=False)

#create a date list
pd.date_range(fr, to, freq='D', closed='left')

#set index
df.set_index('date', inplace=True)

#convert datetimes to the user’s timezone
df.index = df.index.tz_convert('America/Los_Angeles')

#rounding (truncating) datetimes
df.index = df.index.floor('1H') #ceiling

#count things in this dataframe
df.groupby(['date', 'request']).count()

#calculate the start of a week
df['week_start'] = df.index.to_period('W').start_time

#start of next week
df['next_week_start'] = df['week_start'] + pd.DateOffset(weeks=1)

#create range
pd.date_range(start_date, periods=10, freq='D')
pd.date_range(start_date, end_date, freq='30min')

```

## get year, month from date col
```python
#combine group by resulted time series multi-level index in to one col
df_date = pd.DataFrame(dict(A=1), ts.index)
df['date'] = df_date.index.map('{0[0]}-{0[1]:02}-01'.format).values
```

## combine year, month, day cols to date col
```python
#if we do not use values the index will be kept
dts = pd.to_datetime(df[['Year', 'Month', 'Day']]).values
```


## change days to dt
```python
#old
def days2dt(days_since_epoch):
    epoch = dt.datetime(1980, 1, 6)
    return [epoch + dt.timedelta(days=x) for x in days_since_epoch]
    
#new 30x faster
def days2dt(days_since_epoch):
    microseconds = np.around(np.asarray(days_since_epoch) * (24*60*60*10**6))
    return np.datetime64('1980-01-06') + microseconds.astype('timedelta64[us]')
```

## change dt to timedelta [seconds] and back
```python
dts_str = ['2019-07-01 12:00:00','2020-07-01 12:00:00']
datetimes = pd.to_datetime(dts_str, format='%Y-%m-%d %H:%M:%S', utc=False).values
seconds = pd.to_timedelta(datetimes).total_seconds()
dts_back = pd.to_datetime(seconds)
```

## change ctime to datetime
```python
last_modified = os.path.getctime(file) #float 1382189138.4196026
datetime.fromtimestamp(last_modified)
```

## save df to csv with fixed dt format
```python
df.to_csv(file, index=False, date_format='%#d/%m/%Y %H:%M:%S')
```

## round dt to nearest time
```python
df['dt'] = df['dt'].dt.ceil('30min')
```

## numpy.datetime to datetime
```python
def npdt_to_dt(dt):
    #converts a numpy datetime64 object to a python datetime object 
    timestamp = (dt - np.datetime64('1970-01-01T00:00:00')) / np.timedelta64(1, 's')
    return datetime.utcfromtimestamp(timestamp)
```

## days in month
```python
dts = pd.date_range('2020-01-01', periods=10, freq='m')
dts.to_period().days_in_month
```

## offset months
```python
from pandas.tseries.offsets import MonthBegin, MonthEnd
dt= pd.to_datetime(['2002-07-02','2002-10-03'])
dt + MonthBegin(-1) #move backward till get the first month begin
#['2002-07-01', '2002-10-01']
dt + MonthEnd(1) #move forward till get the first month end
#['2002-07-31', '2002-10-31']

#get the first day of each date, MonthBegin does not work
df['first_day_in_month'] = df['date'].to_numpy().astype('datetime64[M]')
```

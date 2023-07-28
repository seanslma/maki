# DateOffset

## period
Only honor the integer periods
```py
t = pd.Timestamp('2022-08-01 12:25:56')
p = t.to_period('30T')
print(f'from {p.start_time} to {p.end_time}')
from 2022-08-01 12:25:00 to 2022-08-01 12:54:59.999999999
```

## normalize
```py
>>> pd.date_range('2022-08-01 23:59:59', '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'))
DatetimeIndex(['2022-08-01 23:59:59'], dtype='datetime64[ns]', freq='MS')

>>> pd.date_range('2022-08-01 23:59:59', '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'), normalize=True)
DatetimeIndex(['2022-08-01', '2022-09-01'], dtype='datetime64[ns]', freq='MS')

>>> pd.date_range(pd.Timestamp('2022-08-01 23:59:59') + pd.DateOffset(days=0, normalize=True), '2022-09-16', freq=pd.tseries.frequencies.to_offset('MS'))
DatetimeIndex(['2022-08-01', '2022-09-01'], dtype='datetime64[ns]', freq='MS')
```

## normalize vs floor('D')
Really???
- `pd.Timestamp.normalize()` sets the time component to midnight (00:00:00) in the `local time zone`, but does not change the time zone itself.
- `pd.Timestamp.floor('D')` sets the time component to midnight (00:00:00) in the `UTC time zone`, and then converts the timestamp to the local time zone if necessary.

## pd.DateOffset vs pd.Timedleta vs pd.tseries.offsets.Day
- `DateOffset` respect calendar arithmetic while `Timedelta` respects absolute time arithmetic, might be different for datetime with timezone info
- pd.DateOffset(days=1) increments a date by 1 calendar day (23, 24, or 25 hours depending on day light savings time)
- pd.Timedelta(days=1) increments a date by 24 hours.

```py
import pandas as pd
date = pd.Timestamp('2016-10-30 00:00:00+0300', tz='Europe/Helsinki')
date_plus_dateoffset = date + pd.DateOffset(days=1)
date_plus_timedelta = date + pd.Timedelta(days=1)
date_plus_offsetsday = date + pd.tseries.offsets.Day()

print(date_plus_dateoffset) #2016-10-31 00:00:00+02:00
print(date_plus_timedelta)  #2016-10-30 23:00:00+02:00
print(date_plus_offsetsday) #2016-10-30 23:00:00+02:00
```

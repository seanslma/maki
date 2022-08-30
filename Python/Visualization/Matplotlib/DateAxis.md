# Date axis

```
import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

n = 25
numpy.random.seed(n)
   
ds = pandas.date_range('2020-01-01', periods=n, freq='m')
df = pandas.DataFrame({    
    't': ds,
    'v': numpy.random.randn(n), 
})
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(ax=ax, x='t', y=['v'])
```

## rotate
```
plt.setp(axes.get_xticklabels(), rotation = 15)
```

## turn on grid
```
ax.xaxis.grid(True, which="minor") #minor
ax.xaxis.grid(which='both', linestyle='dotted') #both
```

## b\nY
```
#ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
```

## time\ndate
```
ax.plot(df.t, df.v)
dy_fmt=mdates.DateFormatter('%H:%M\n%Y-%m-%d')
hr_fmt=mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(dy_fmt)
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_minor_formatter(hr_fmt)
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(2,24,2)))
```

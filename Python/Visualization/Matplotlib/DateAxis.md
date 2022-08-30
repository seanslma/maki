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

## b\nY
```
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
```

## 

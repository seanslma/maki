# Date axis

## example
```py
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
```py
plt.setp(axes.get_xticklabels(), rotation = 15)
```

## turn on grid
```py
ax.xaxis.grid(True, which="minor") #minor
ax.xaxis.grid(which='both', linestyle='dotted') #both
```

## b\nY
```py
#ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
```

## time\ndate
```py
ax.plot(df.t, df.v)
dy_fmt=mdates.DateFormatter('%H:%M\n%Y-%m-%d')
hr_fmt=mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(dy_fmt)
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_minor_formatter(hr_fmt)
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(2,24,2)))
```

## date minor tick labels too crowded
When using auto date locator, sometimes the minor tick labels are too crowded. In this case we need to check the number of visible non-empty minor tick labels and replace with custom locator.

We also adjust the major tick label heights as sometimes it's not aligned with the minor tick labels.

There are some custom postprocessing of the major tick labels as well to remove first empty line.

```py
colours = [my_colours[col] for col in df.columns]
kwargs.setdefault('color', colours)
kwargs.setdefault('alpha', 0.6)
kwargs['stacked'] = False
kwargs['subplots'] = True
kwargs['sharey'] = True
kwargs['legend'] = False

# df index is datetime
axes = df.fillna(0).plot.area(
    figsize=figsize,
    layout=layout,
    **kwargs
)

ymin, ymax = plt.ylim()
use_custom_locator = None
minor_locator = mdates.DayLocator(bymonthday=range(1, 32, 2))
for col, ax in zip(df.columns, axes.ravel()):
    ax.set_title(col)
    ax.set_ylim(ymin*1.1, ymax*1.1)

    # switch to custom locator based on number of visible labels
    if use_custom_locator is None:
        n_ticks = sum(
            1 for lbl in ax.get_xminorticklabels()
            if lbl.get_visible() and lbl.get_text().strip()
        )
        use_custom_locator = n_ticks > 9
    if use_custom_locator:
        ax.xaxis.set_minor_locator(minor_locator)

    # adjust height of major tick labels
    for label in ax.get_xticklabels(which='major'):
        label.set_y(0.005)

    # remove first empty line in major tick labels
    labels = [
        lbl.get_text().replace('\n\n', '\n')
        for lbl in ax.get_xticklabels(which='major')
    ]
    ax.set_xticks(
        ticks=ax.get_xticks(minor=False),
        labels=labels,
        minor=False,
    )

axes[0, 0].set_ylabel('Shared Y Axis')

fig = axes[0, 0].figure
fig.suptitle('My Custom Chart', fontsize=14)

fig.show()
plt.close(fig) # close the figure to free memory
```

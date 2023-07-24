# Pandas

## df.plot
```py
ax = df.plot(
  x='date',
  y=['forecast_revenue','actual_revenue'],
  title=f'Cal Year: 2022',
  figsize=(12,5),
)
_ = ax.set_ylabel("Revenued ($)")
```

## rotate axis labels
```py
import matplotlib.pyplot as plt
#set font and plot size to be larger
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})
df['rating'].plot(kind='hist', title='Rating')
df.plot(kind='scatter', x='speed', y='distance', title='my plot')
```

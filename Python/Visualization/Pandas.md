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
## hour x-axis with 24 hours
```py
tod = df.groupby('time')[['min', 'max']].mean().reset_index()
# # cannot restrict the min/max
# ax = tod.plot(x='time', y=['min', 'max'], figsize=(12, 6), grid=True)
# xticks = pd.date_range('2023-01-01', freq='2H', periods=12)
# ax.set_xticks(xticks.time)
# ax.xaxis.set_major_formatter(plt.FixedFormatter(xticks.strftime('%H:%M')))

tod['hour'] = tod['time'].apply(lambda x: x.hour + x.minute / 60)
ax = tod.plot(x='hour', y=['min', 'max'], figsize=(12, 6), grid=True)
xticks = list(range(0, 25, 2))
xtick_labels = [f'{h:2}:00' for h in xticks]
ax.set_xticks(xticks)
ax.set_xlim(xticks[0], xticks[-1])
ax.xaxis.set_major_formatter(plt.FixedFormatter(xtick_labels))
```

## day of week profile
```py
dow = df.assign(dow=lambda x: x['ts'].dt.dayofweek).groupby('dow')[['min', 'max']].mean().reset_index()
ax = dow.plot(x='dow', y=['min', 'max'], figsize=(12, 6), grid=True)
ax.set_xticks(range(0,7))
_ = ax.set_xticklabels(['Mon', 'Tue','Wed', 'Thur', 'Fri', 'Sat', 'Sun'])
```

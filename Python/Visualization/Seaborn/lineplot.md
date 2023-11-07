# lineplot

## line styles
```py
line_styles = ['-', '--', '..', '-.', '-..-', '--...', '-    ', '--   ', '--..', 'o-', 's-', '^-', '>--', '<--', '*-', 'h-', '+-', '-', '-', None]
```

## line plot with figure size
will automatically plot x, y, z based on index ts.
```py
df = pd.DataFrame({'ts':ts, 'x': x, 'y': y, 'z': z}).set_index(ts)
plt.figure(figsize=(18,7))
sns.lineplot(data=df)
plt.show()
```

## lineplot with hue and style
ToD profile
```py
tod = df.groupby(['quarter', 'time'])[['QLD', 'NSW']].mean().reset_index()
tod['hour'] = tod['time'].apply(lambda x: x.hour + x.minute / 60)
tod = tod.set_index(['quarter', 'time', 'hour']).stack().rename_axis(index={None: 'model'}).rename('val').reset_index()

sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
g = sns.lineplot(data=tod, x='hour', y='val', hue='quarter', style='model', legend='brief')

# Set xticks
xticks = list(range(0, 25, 2))
xtick_labels = [f'{h:02}:00' for h in xticks]
plt.xticks(xticks, xtick_labels)
_ = plt.xlim(xticks[0], xticks[-1])

# Set the legend position to the right-top outside corner
_ = g.legend(loc='upper left', bbox_to_anchor=(1.05, 1.1))
```

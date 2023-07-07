# Example

## matplotlib
```py
plt.plot(x, y, 'ko', label="Original Data")
plt.plot(x_fit, y_fit, 'r-', label="Fitted Curve")
plt.legend()
```

## df secondary y
```py
ax = df.plot(x='dt',y=['y_left'],figsize=(14,6))
df.plot(x='dt',y=['y_right'], ax=ax, secondary_y=True)
_ = ax.set(xlabel='')
```

## plot.ly
```py
df.iplot()
```

## sns realplot/lmplot
```py
g = sns.FacetGrid(df, row='scenario', col='month', hue='region', height=1.5, aspect=3, sharex=False)
g.map(sns.lineplot, 'year', 'val')

sns.relplot(kind='line', data=df, x='year', y='daily', hue='month', col='type', height=6, aspect=1.5)
g= sns.relplot(kind='line', data=df, x='year', y='daily', hue='month', style='type', height=6, aspect=1.5)
g._legend.set_bbox_to_anchor([0.36,0.72])

sns.lmplot(data=df, x='val_1', y='val_2', row='year', col='month', hue='type')
```

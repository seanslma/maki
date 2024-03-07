# Aggregation

## groupby
5x faster
```py
l = dl.group_by(['region', 'country', 'city']).agg(pl.col('value').sum())
f = df.groupby(['region', 'country', 'city'])[['value']].sum())
```

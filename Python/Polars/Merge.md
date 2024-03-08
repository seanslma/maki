# Merge

## join
lazy join with streaming is 2x faster
```py
df.lazy().join(dl.lazy(), on=['id', 'id2'], how='left').filter(
    (pl.col('day') < pl.col('day_right')) & (pl.col('day_right') - pl.col('day') <= 30)
).collect()

df.lazy().join(dl.lazy(), on=['id', 'id2'], how='left').filter(
    (pl.col('day') < pl.col('day_right')) & (pl.col('day_right') - pl.col('day') <= 30)
).collect(streaming=True)
```

join is 2x faster than pandas
```py
d1.merge(d2, left_index=True, right_index=True) #index: id, date
l1.join(l2, on=['id', 'date'], how='inner')
```

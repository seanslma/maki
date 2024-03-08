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

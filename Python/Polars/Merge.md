# Merge

## vertical concat
- all dfs must have the same cols and same order
```py
import polars as pl
d1 = pl.DataFrame({
    'x': [1, 2, 3],
    'y': [4, 5, 6]
})
d2 = pl.DataFrame({
    'y': [7, 8, 9],
    'x': [10, 11, 12]
})
try:
    df = pl.concat([d1, d2], how='vertical')
    print(df)
except Exception as e:
    print(f'Error: {e}')
# output
# Error: unable to vstack, column names don't match: "x" and "y"
```

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

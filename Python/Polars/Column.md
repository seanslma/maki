# Column

## rename
```py
df = pl.DataFrame({
    'foo': [1, 2, 3],
    'bar': [6, 7, 8],
    'ham': ['a', 'b', 'c'],
})
df.rename({'foo': 'apple'})
df.rename(lambda col: 'c' + col[1:])
```

## reorder columns
https://stackoverflow.com/questions/71353113/polars-how-to-reorder-columns-in-a-specific-order

Do not use Square bracket indexing:
- cannot be parallelized
- cannot be optimized
```py
df = pl.DataFrame({
    'z': [1, 2],
    'x': ['a', 'b'],
    'y': [True, False],
})

df.select(['x', 'y', 'z'])
```

## create new column conditional on other columns
```py
df.with_columns(
    pl.when(pl.col('x') > 0.5).then(0).otherwise(1).alias('y')
)
```

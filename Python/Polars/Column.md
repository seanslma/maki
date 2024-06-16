# Column

## reorder columns
https://stackoverflow.com/questions/71353113/polars-how-to-reorder-columns-in-a-specific-order

Do not use Square bracket indexing:
- cannot be parallelized
- cannot be optimized
```py
df = pl.DataFrame({
    'z': [1, 2],
    'x': ['a', 'b'],
    'y': [True, False]
})

df.select(['x', 'y', 'z'])
```

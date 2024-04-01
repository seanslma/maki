# Data type

## cast
https://stackoverflow.com/questions/71790235/switching-between-dtypes-within-a-dataframe

## string to int/float
```py
df = pl.DataFrame({'val_str': ['1.5', '2.2', '12', '']})
df.with_columns(
    pl.col('val_str').cast(pl.Float64, strict=False).alias('val')
)
```

## int/float to string
```py
df = pl.DataFrame({'val': [1.5, 2.2, 12, None]})
df.with_columns(
    pl.col('val').cast(pl.Utf8, strict=False).alias('val_str')
)
```

## string to datetime
```py
df.with_columns(
    pl.col('date').str.strptime(pl.Datetime, fmt='%Y-%m-%d').cast(pl.Datetime)
)
```

## new col
```py
df = pl.DataFrame({'val': ['10', '20', '']})
df.with_columns([
    pl.format('Value is {}', pl.col('val'))
])
```

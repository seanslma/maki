# Group

## select and where
```
d = (
    df
    .select('name', 'price')
    .where((df['id']==1) | (df['id']==3))
)
display(d)
```

## groupby
```
d = (
    df
    .select('id', 'name')
    .groupBy('name')
    .count()
)
display(d)
```

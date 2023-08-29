# ColType

## convert col to float
```py
df['val'] = pd.to_numeric(df['val'], errors='coerce')
df['val'] = df.astype({'val':'float'})
```

## convert col to string
using `map` to apply the function
```py
df[col] = df[col].map('{:.4f}'.format, na_action='ignore')
```

## empty df with dtypes
```py
df = pd.DataFrame({
    'id': pd.Series(dtype='int'),
    'name': pd.Series(dtype='str'),
    'value': pd.Series(dtype='float'),
    'datetime': pd.Series(dtype='datetime64[ns]'),
 })

df = pd.DataFrame({
    c: pd.Series(dtype=t) for c, t in {
        'a': 'int',
        'b': 'str',
        'c': 'float',
    }.items()
})

# slower
col_types = {
    'id': 'int',
    'name': 'str',
    'value': 'float',
    'datetime': 'datetime64[ns]',    
}
df = pd.DataFrame(columns=col_types.keys()).astype(col_types)
```

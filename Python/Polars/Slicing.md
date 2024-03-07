# Slicing

## category and date
```py
dl.filter(pl.col('code') == '4311251697')   #10.3ms
df[df['code'].values == '4311251697']       #12.2ms

dl.filter(pl.col('ts') >= datetime(2022,8,1)).filter(pl.col('ts') < datetime(2022,9,1))      #314ms
df[(df['ts'].values >= pd.Timestamp(2022,8,1)) & (df['ts'].values < pd.Timestamp(2022,9,1))] #236ms
```

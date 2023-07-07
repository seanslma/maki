# Fill Na

## fillna for selected columns within groups
```py
df['col'] = df.groupby('grp')['col'].ffill()
```

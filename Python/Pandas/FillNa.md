# Fill Na

## fillna for selected columns within groups
```
df['col'] = df.groupby('grp')['col'].ffill()
```

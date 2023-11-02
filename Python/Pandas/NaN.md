# NaN

## fillna for selected columns within groups
```py
df['col'] = df.groupby('grp')['col'].ffill()
```

# df.groupby
`df.groupby` mean does not support "skipna=False"

## drop nan from array
```py
arr[~pd.isnull(arr)]
```

## check df nan values
```py
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
```

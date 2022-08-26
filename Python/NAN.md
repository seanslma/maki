# NaN

df groupby mean does not support "skipna=False"

## drop nan from array
```python
arr[~pd.isnull(arr)]
```

## check df nan values
```python
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
```

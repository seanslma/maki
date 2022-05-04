# index

The .loc/[] operations can perform enlargement when setting a non-existent key for that axis.

## cols to multiindex
```python
mi = df.columns.str.split('_', expand=True)
```

## get level values
```python
df.index.get_level_values(0)
df.index.get_level_values('level_2')
```

get one value
```python
df.index.values[1][0] #fastest
df.index[1][0]  #fast
df.index.get_level_values(0)[1] #slow
```

## rename levels
```python
df = df.rename_axis(index={None:df.index.name})
df = df.rename_axis(columns={None:df.index.name})
```

## reorder levels
```python
#custom reorder MultiIndex
mi = pd.MultiIndex.from_product([['Value'],regions,scens], names=[None,'Region','Scenario'])
df = df.reorder_levels([None,'Region','Scenario'], axis=0).reindex(mi) #index (default)
df = df.reorder_levels([None,'Region','Scenario'], axis=1).reindex(mi) #columns
```

## add a new index
```python
df = pd.concat([df], keys=['New_Idx'], names=['idx0'])
```

## drop rows with duplicate index
```python
df.pipe(lambda x: x[~x.index.duplicated(keep='first')])
```

## get last day of each month in index
```python
df.loc[df.groupby(df.index.to_period('M')).apply(lambda x: x.index.max())]
```

# index

The .loc/[] operations can perform enlargement when setting a non-existent key for that axis.

## get level values
```python
df.index.get_level_values(0)
df.index.get_level_values('level_2')
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

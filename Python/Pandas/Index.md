# index

The `.loc/[]` operations can perform enlargement when setting a non-existent key for that axis.

## `df.drop` vs `df.droplevel`
- `df.drop`: Removes rows or columns based on labels or indices.
- `df.droplevel`: Drops levels from a multi-level index, simplifying it to a single-level index DataFrame.

## get values vs slice rows
```
id  name
1   a       2.0
2   a       4.0
Name: val, dtype: float64
```
Singe value in index returns results excluding the index:
```
>>> s[1]
name
a    2.0
Name: val, dtype: float64
```
Multiple values in index returns results including the index:
```
>>> s[[1]]
id  name
1   a       2.0
Name: val, dtype: float64
```

## cols to multiindex
```py
mi = df.columns.str.split('_', expand=True)
```

## get level values
```py
df.index.get_level_values(0)
df.index.get_level_values('level_2')
```

## get levle unique values
_**caveat**_:  `index.levels` does not return updated contents if any rows or columns have been deleted.
The MultiIndex keeps all the defined levels of an index, **even if they are not actually used**, to avoid a recomputation of the levels in order to make slicing highly performant.
```py
df.index.levels[0]                               #fastest but should avoid to use, bad
df.index.levels[df.index.names.index('level_1')] #do not use it
df.index.get_level_values('Level_1').unique()    #slow
df.index.unique(level='level_1')                 #suggested
```

## get one value
```py
df.index.values[1][0] #fastest
df.index.values[1][df.index.names.index('id')] #by level name
df.index[1][0]  #fast
df.index.get_level_values(0)[1] #slow
```

## rename levels
```py
df = df.rename_axis(index={None:df.index.name})
df = df.rename_axis(columns={None:df.index.name})
```

## reorder levels
```py
#custom reorder MultiIndex
mi = pd.MultiIndex.from_product([['Value'],regions,scens], names=[None,'Region','Scenario'])
df = df.reorder_levels([None,'Region','Scenario'], axis=0).reindex(mi) #index (default)
df = df.reorder_levels([None,'Region','Scenario'], axis=1).reindex(mi) #columns
```

## modify one level
```py
df.set_index(df.index.set_levels(df.index.get_level_values('a').dt.date, level='a'))
```

## add a new index
```py
df = pd.concat([df], keys=['New_Idx'], names=['idx0'])
```

## drop rows with duplicate index
```py
df.pipe(lambda x: x[~x.index.duplicated(keep='first')])
```

## get last day of each month in index
```py
df.loc[df.groupby(df.index.to_period('M')).apply(lambda x: x.index.max())]
```

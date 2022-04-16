# reshape

## melt
unpivot a table col by col. The selected id cols will be repeated and the selected value cols will be stacked col by col.

```python
df = pd.DataFrame({'A':['a','b','c'], 'B':[1,3,5], 'C':[2,4,6]})             
pd.melt(df, id_vars=['A'], value_vars=['B','C'], var_name='var', value_name='val')                   
```

## pivot
return reshaped DataFrame organized by given index / column values.

```Python
df = pd.DataFrame({'idx': ['a', 'a', 'b', 'b', 'c', 'c'],
                   'col': ['B', 'C', 'B', 'C', 'B', 'C'],
                   'va1': [1, 2, 3, 4, 5, 6],
                   'va2': ['x', 'y', 'z', 'q', 'w', 't']})            
df.pivot(index='idx', columns='col', values='va1')
df.pivot(index='idx', columns='col', values=['va1', 'va2'])    

#back to melt status
df_pivot = df_pivot.reset_index()
df_pivot.columns.name = None              
```

## stack
stack row by row to a series, with original index and col names being merged to new index.

```python
df = pd.DataFrame({'A':['a','b','c'], 'B':[1,3,5], 'C':[2,4,6]})             
df.stack()

#add names for new index and col
df.stack().rename_axis(index={None: 'new_idx'}).rename('new_val').reset_index()

#multiIndex columns
df.stack(list(range(df.columns.nlevels)))
```

## unstack
for df, stack col by col to a series, with col names and original index being merged to new index.

```Python
df = pd.DataFrame({'A':['a','b','c'], 'B':[1,3,5], 'C':[2,4,6]})             
df.unstack()
```
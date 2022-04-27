# group

## avoid using `df.index.levels[]`
# Merge

## join vs merge
`merge` joins columns of left to columns of right, but `join`(... on=[...]) joins columns of left to **index keys** of right.

## group by month, quarter, year
Test code:
```python
def test(df):
    print(f'df.index.levels[0]: {df.index.levels[0]}')
    print(f'df.index.get_level_values(0): {df.index.get_level_values(0)}')
    return df
dx = (
    pd.DataFrame(
        data={'id':[1,2],'name':['a', 'b'],'value':[5,6]}
    )
    .set_index(['id', 'name'])
    .groupby('id')
    .apply(test)
)
```
Results:
```
df.index.levels[0]: Int64Index([1, 2], dtype='int64', name='id')
df.index.get_level_values(0): Int64Index([1], dtype='int64', name='id')
df.index.levels[0]: Int64Index([1, 2], dtype='int64', name='id')
df.index.get_level_values(0): Int64Index([2], dtype='int64', name='id')
```

## reshape to serials and group
```python
#df.columns = ['idx1','idx2','idx3','prd1','prd2','prd3']
#set index
df = df.set_index(['idx2','idx2','idx3'])
#stack val cols
df = df.stack().rename_axis(index={None:'prd'}).rename('val')
#average values based on idx3
dm = df.groupby(['idx1', 'idx2']).mean()
#add back idx3
dm = pd.concat([dm], keys=['avg'], names=['idx3'])
#correct index order
dm = dm.reorder_levels(['idx1','idx2','idx3'])
#combine with original df
dc = pd.concat([dm,df],axis=0,ignore_index=False)
#expand prd back to cols
d2 = dc.unstack('prd').reset_index()
#d2.columns = ['idx1','idx2','idx3','prd1','prd2','prd3']
```

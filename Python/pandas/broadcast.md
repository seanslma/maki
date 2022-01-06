# broadcast

## Expand df date ranges to individual rows
```
df = (
    df
    .assign(DATE=lambda x: [pd.date_range(row.STARTDATE, row.ENDDATE, freq='d') for _,row in x.iterrows()])
    .explode('DATE')
    .drop(['STARTDATE', 'ENDDATE'], axis=1)
)
```

## multiindex

reindex with level can broadcast the level. also df.div can broadcast only one level.

not good, will repeat all combinations:
```python
va = np.array([[1991,1992],[6,7],[8,9],[1,2],[3,4]]).T
df = pd.DataFrame(va,columns=['a','b','c','x','y']).set_index(['a','b','c'])

d2 = df.groupby(['a','c']).mean()/2
d3 = d2.reindex(df.unstack('b').columns, axis=1, level=0)
d3 = d3.stack(level=1).reorder_levels(['a','b','c'])
```

## broadcast with reindex
```python
va = np.array([[1991,1991,1992],[6,7,7],[8,8,10],[1,2,3],[3,4,5]]).T
df = pd.DataFrame(va,columns=['a','b','c','x','y']).set_index(['a','b','c'])

ia = df.index.get_level_values('a')
ic = df.index.get_level_values('c')
mi = pd.MultiIndex.from_arrays([ia,ic],names=['a','c'])
d2 = df.groupby(['a','c']).mean()/2
d2.reindex(mi)
d2.reindex(df.index.droplevel('b')) #better?
d2.loc[df.index.droplevel('b'),:] #best?
```


  

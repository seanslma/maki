## adv

### interpolation
```py
df = df.set_index(dts)
df = df.set_index('fld')
df = df.reindex(dts, fill_value=0)
df = df.reindex(dts, method=method)
```

### first val >= v
```py
i0 = np.searchsorted(dts, dt0, side='left') #a[i-1] < v <= a[i]
i1 = np.searchsorted(dts, dt1, side='right') - 1 #a[i-1] <= v < a[i]
```

### num of nan in a col
```py
df.isna().sum()
df['fd'].isna().sum()
```
### bin label
```py
#label data according to provided bins
lbls_new = pd.cut(x=col_dat, bins=bins, include_lowest=True, right=False, labels=lbls).astype(int)

#digitize: assign the index according to provided bins
bin_ind = np.digitize(val, bins=[10, 20, 40, 50], right=True)
```

### filter col
```py
df2 = df[df['tech'].str.contains('|'.join(techs))]
```

### combine rows/cols
```py
#same cols append rows
df = pd.concat([df1,df2],axis=0,ignore_index=True) #don't use append, too slow
#same number of rows append cols
df = pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True)],axis=1)

#NOTE: concat drops the name of the merge axis when not aligned
```

### merge

if the col is obj type, the merge does not work!!!\\
https://www.datasciencebytes.com/bytes/2014/11/27/when-joins-go-wrong-check-data-types/

merge has similar functionality as the the sql join (inner, left, right, and outer).

https://stackoverflow.com/questions/53645882/pandas-merging-101
```py
#left join
df = df_left.merge(df_right, how='left', on='user_id')

#left join if null
df = df_left.merge(df_right, how='outer', on=['id'], indicator='i')
df = df.query('i == "left_only"').drop('i', 1)

#inner join
df = pd.merge(left, right, how="left", on=["key1", "key2"])
```

### pivot
```py
df['dt'] = pd.to_datetime(df['settlementdate'], format='%Y-%m-%d %H:%M', utc=False)

df1 = pd.DataFrame()
df1['date'] = df['dt'].dt.date
df1['hour'] = df['dt'].dt.hour
df1['value'] = np.ones(df1.shape[0])

df.pivot_table(columns='id',values='val',aggfunc='mean')

df2 = pd.pivot_table(df1, index=['date'],
  columns=['hour'], values=['value'], aggfunc=np.sum, fill_value=0)
```

### aggregation
```py
#group
df.groupby('day')['total_bill'].mean()
df.groupby('day')['total_bill'].aggregate('mean')
dg = df.groupby(['store'], as_index=False).agg({'col1':'mean', 'col2':'sum', 'col3':'sum'})

df = df_tips.groupby(by='sex').agg({'total_bill': ['count', 'mean', 'sum']})
df.rename(columns={'count': 'count_meals', 'mean': 'average_bill', 'sum': 'total_bills'})

#filter
df.groupby('day').filter(lambda x : x['total_bill'].mean() > 20)
df.groupby('day').filter(lambda x : x['total_bill'].mean() > 20)['size'].mean()

#get row with max value in col in each group
ind = df.groupby(['a','b'])['version'].transform(max) == df['version']
df_new = df[ind]

df_grouped = df.groupby(['a', 'b'], as_index=False).agg({'version':'max'})
df_grouped = df_grouped.rename(columns={'version':'version_max'})
df = pd.merge(df, df_grouped, how='left', on=['a', 'b'])
df = df[df['version'] == df['version_max']]

df.groupby('kind').agg({'col1': {'foo': sum()}, 'col2': {'mean': np.mean, 'std': np.std}})
df.groupby('kind').agg(min_height=('height', 'min'), max_weight=('weight', 'max'))
```

### transform
transform will created a new col with the same indices [populate the grouped value to all elements in each group]

```py
#get row with max value in col in each group
ind = df.groupby(['a','b'])['version'].transform(max) == df['version']
df_new = df[ind]
```


### add a new level to df column
```py
df.columns = pd.MultiIndex.from_product([['x'], df.columns])

#from tuples
tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]
pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))

#from arrays
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
```
### Sum columns by level in MultiIndex df
  df.groupby(level=0, axis=1).sum()
  df.sum(level=0, axis=1)

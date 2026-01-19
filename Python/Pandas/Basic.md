## Basic
```py
df.info()
df.describe()
```

### indexing
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

avoid what is called chained indexing (not just for performance):
```py
dfmi['one']['second'] #bad
dfmi.loc[:, ('one', 'second')] #good
```

### change column names
```py
df.columns = df.columns.str.lower()

#common rows
df_index = np.intersect1d(df_percentage.index, df_repeated_EV_num.index)
df_index = df_percentage.index.intersection(df_repeated_EV_num.index)
df1 = df2.loc[df_index,:] * df3.loc[df_index,df2.columns]
```

### get one val by row index and col label
```py
df.at[df.index[0], 'A']
df.loc[df.index[0], 'A']
df.get_value(df.index[0], 'A')

df.iat[0, df.columns.get_loc('A')]
df.iloc[0, df.columns.get_loc('A')]
df.get_value(0, df.columns.get_loc('A'), takable=True)
```

### replace col vals by dic
```py
#slower
df.replace({'col1': dic})
df['col1'].replace(dic, inplace=True)

#faster
df['col1'].map(dic) #not matched will be changed to NaN
df['col1'].map(di).fillna(df['col1']) #keep unmatched values
```

### drop duplicate rows
```py
df = pd.DataFrame({
    'col1':['A','B','A','B','C'],
    'col2':[3,4,3,5,6],
    'col3':[0,0.1,0.2,0.3,0.4],
})

df.drop_duplicates(['col1','col2'])[['col1','col2']] #drop col3
```

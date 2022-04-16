## other

https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/

### pd version
  #pandas version
  pd.__version__
  #versions of Python and dependent packages and OS type
  pd.show_versions() 
  
### change display width
  from IPython.core.display import display, HTML
  display(HTML("<style>.container {width:90% !important;}</style>"))  
  pd.set_option('display.max_columns', 10)
### add/delete col/s
```python
#add a new col to the end
df['A'] = [1,2,3]
#insert a col to a specific position
df.insert(loc=0, column='A', value=[1,2,3])

#add columns
df = pd.concat([df1, df2], axis=1, ignore_index=True)

#delete col 'area'
df = df.drop('area', axis=1)
#using columns parameter
df = df.drop(columns='area')
#keep df using inplace=True
df.drop("area", axis=1, inplace=True)
#delete multiple cols
df = df.drop(['A', 'B', 'C'], axis=1)

#keep only a few cols
df1 = df[['A','B']]
```

### add/delete row/s
```python
#add row
df.append(df2, ignore_index=True)
df = pd.concat([df1,df2],ignore_index=True)

def df_insert_row(r, df):
    d1 = pd.DataFrame(np.random.randn(1, df.shape[1]), columns=df.columns)
    d2 = pd.concat([df.iloc[:r], d1, df.iloc[r:]], axis=0, ignore_index=True)

#delete rows using iloc
df = df.iloc[5:,]

#delete rows with labels 0,1,5
df = df.drop([0,1,5], axis=0)

#delete the rows with label '2018Q1', index should be set
df = df.drop('2018Q1', axis=0)

#drop rows with any NaN values
df.dropna() 

#drop only if ALL columns are NaN
df.dropna(how='all')

#drop rows without at least two **not** NaN values
df.dropna(thresh=2)

#drop rows only if NaN in specific columns   
df.dropna(subset=[1,3,5])  
df.dropna(subset=['a','d','g'])  

```

### rename cols
```python
#rename multiple cols with dict
df.rename(columns={ 'area': 'place_name', 'Y2001': 'year_2001' }, inplace=True)
#rename all cols using a function, to lower case
df.rename(columns=str.lower)
#using lambda
df.rename(columns=lambda x: x.lower().replace(' ', '_')
```

### change cols type
```python
#change all cols
df.astype('int32').dtypes
#change a few cols
df.astype({'col1': 'int32'}).dtypes
```


### replace/drop NaN
```python
#replace NaN
df = df.fillna(0)

df.fillna({'a':0, 'b':0}, inplace=True)

df[['a', 'b']] = df[['a','b']].fillna(value=0)

#drop NaN
df = df.dropna(subset=['id'])
#drop rows where all fields are missing
df.dropna(how='all')
```

### get duplicate
```python
df_duplicate = df[df.duplicated(['a'], keep=False)]
```

### drop duplicate
```python
df = df.drop_duplicates(['first_name','last_name'], keep='first')
```
### conditional select rows
```python
df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]

#get row indexes
df.index[df['v'].isin([1,5,6])].tolist()
df.index[df['v'].isin(['a','b','c'])].tolist()
```

### np.Array to dateframe
```python
ar = np.zeros((2, 3),dtype=float)
df = pd.DataFrame(ar, columns=['A','B','C'])
```




### reshape
```python
#melt:join all cols
df = pd.DataFrame({'id': ['d1', 'd2', 'd3'],'p1': [3, 2, 1], 'p2': [7, 5, 3]})
df2 = pd.melt(df, id_vars=['id'], var_name='p', value_name='val')

#stack: join all rows
df3 = df.stack()

#unstack: create cols based on index
index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),('two', 'a'), ('two', 'b')])
s = pd.Series(np.arange(1.0, 5.0), index=index)
df1 = s.unstack(level=-1)
df0 = s.unstack(level=0)
df0.unstack()
```


### concat
```python
#append rows
df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
#append cols
df = pd.concat([df1,df2,df3],axis=1)
#add index with name
df = pd.concat([d1,d2], keys=['City','Street'], names=['idx1','idx2'])
```

### count positive in each row
```python
np.sum(np.where(df[cols] > 0, 1, 0), axis=1)
```

### repeat
```python
df=pd.DataFrame(columns=['a','b'],data=[[1,2],[3,4]])
#repeat each column 2x
df[np.repeat(df.columns.values,2)]
```

### split
```python
chunks = np.split(df, df.shape[0] / 10**6)
```

### idx to col
```python
df = df.reset_index(level=0)
```

### fill gaps
```python
df.reindex(dt_all, method='ffill')
```

### lists to df
```python
df = pd.DataFrame({'a':l1,'b':l2,'c':l3})
df = pd.DataFrame(columns=['a','b','c'],data=np.column_stack([l1,l2,l3]))
```


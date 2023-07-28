# Dictionary

## merge dicts
```py
dic1 = {'a':1, 'b':2}
dic2 = {'e':5, 'f':6}
dic3 = {**dic1, **dic2}
```

## df to dic
```py
#each col to a key
df = pd.DataFrame({'a': [1,2],'b': ['x', 'y'], 'c': ['u', 'v']})
dic = df.to_dict('list')

#each row to a key
df = pd.DataFrame({'id': ['p', 'q', 'r'],'a': ['red', 'yellow', 'blue'], 'b': [0.5, 0.25, 0.125]})
dic = df.set_index('id').T.to_dict('list')

#not work
dic = {k: list(g) for k, g in df.groupby('id')['a','b']}

#series: id is key, a and b are in 2d array
xx = df.groupby('id').apply(lambda x:x[['a','b']].values)

#series: similar to previous, values col has a name
yy = df.groupby('id')['a','b'].apply(lambda x: x.values.tolist()).to_frame('val').reset_index()
```

# Performance

## get is faster
```python
import timeit

a1 = df.get('name').unique() #fastest
a2 = df.name.unique()        #ok
a3 = df['name'].unique()     #slow

t1 = timeit.Timer(lambda: df.get('name').unique())
print(t1.timit(10)
```

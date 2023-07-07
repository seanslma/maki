# Performance

## get is faster
```py
import timeit

a1 = df.get('name').unique() #fastest
a2 = df.name.unique()        #ok
a3 = df['name'].unique()     #slow

t1 = timeit.Timer(lambda: df.get('name').unique())
print(t1.timit(10)
```

## named agg is slow
https://stackoverflow.com/questions/69799691/named-aggregations-with-pandas-group-by-agg-are-super-slow-why

Once you pass in `lambda`, the operation is **no longer vectorized** across the groups even though it can be vectorized within each group.

bad:
```py
df.groupby('A').agg(**{
  'newname' : ('B', lambda x: x.sum(min_count=1))
})
```

good
```py
df.groupby('A').sum(min_count=1)

d = df.groupby('A')
pd.DataFrame({
    'name-b1': d['B'].sum(min_count=1),
    'name-b2': d['B'].size(),
})
```

https://llllllllll.github.io/principles-of-performance/index.html

https://speakerdeck.com/pycon2018/jake-vanderplas-performance-python-seven-strategies-for-optimizing-your-numerical-code

https://speakerdeck.com/nnja/nina-zakharenko-the-basics-of-memory-management-in-python-north-bay-python-2018

https://software.intel.com/en-us/articles/large-matrix-operations-with-scipy-and-numpy-tips-and-best-practices

http://conference.scipy.org/proceedings/scipy2018/pdfs/anton_malakhov.pdf

http://conference.scipy.org/proceedings/scipy2017/pdfs/oleksandr_pavlyk.pdf

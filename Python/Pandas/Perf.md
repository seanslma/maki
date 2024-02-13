# Performance

## unique values
https://stackoverflow.com/questions/13688784/python-speedup-np-unique

The `numpy.unique()` is based on sorting (quicksort), and the `pandas.unique()` is based on hash table.
- np.unique: sorted slower
- pd.unique: not sorted faster

General rules:
- list of integers/strings: `list(set())`
- pd.Series with integers: `pd.unique()`
- pd.Series with strings: `pd.unique()` or `list(set(s.values))` [1.5x faster]

```py
%timeit df.get('name').unique() 
1.64 ms ± 25 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%timeit df.name.unique()    
1.66 ms ± 80.3 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%timeit df['name'].unique()  
1.84 ms ± 108 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%timeit list(set(df['name']))
3.23 ms ± 368 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit list(set(df['name'].values))
579 µs ± 39.3 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%timeit np.unique(df['name'].values)
12.7 ms ± 644 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

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


## df.where vs np.where
No big differences: np.where will convert `datetime64[ns]` to object - use df.where if possible
```py
# 0.6 ms for 48*365*1 rows
# 60 ms for 48*365*100 rows
d1 = d.assign(
    f0=np.where(d['f0'] < 0.1, 0, d['f0'])
)
# 1.0 ms for 48*365*1 rows
# 66 ms for 48*365*100 rows
d2 = d.assign(
    f0=lambda x: x['f0'].where(x['f0'] >= 0.1, 0)
)
```

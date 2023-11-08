# Pandas

## iter rows, using `zip` with values is 400x faster than `df.iterrows()`.
assume df has columns `name`, `date`, and `value`.
```py
%timeit for row in df.iterrows(): pass
1.67 s ± 70.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit for row in df.to_records(index=False): pass
69.2 ms ± 2.89 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit for n, d, v in zip(df['name'], df['date'], df['value']): pass
10.9 ms ± 751 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit for n, d, v in zip(df['name'].values, df['date'].values, df['value'].values): pass
4.12 ms ± 302 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

## slow multiindex methods
Get the mask of the index in both mi1 and mi2 - can be 2x faster.
```py
#slow
iboth = mi1.intersection(mi2)
mask1 = mi1.isin(iboth)
mask2 = mi2.isin(iboth)

#fast (joining the index of both dfs will be 8x faster than joining normal cols)
d1 = pd.DataFrame(index=mi1, data=np.arange(len(mi1)), columns=['id1'])
d2 = pd.DataFrame(index=mi2, data=np.arange(len(mi2)), columns=['id2'])
df = d1.merge(d2, how='inner', left_index=True, right_index=True)
mask1 = np.full(len(mi1), False, dtype=bool)
mask1[df.id1] = True
mask2 = np.full(len(mi2), False, dtype=bool)
mask2[df.id2] = True
```

## pd.eval
```py
np.random.seed(0)
df = pd.DataFrame(np.random.rand(100000,2), columns=['x','y'])

import numba as nb
@nb.njit
def nb_and(x, y):
    n = len(x)
    val = np.empty(n, dtype=np.bool_)
    for i in range(n):
        val[i] = (x[i] < 0.9) & (y[i] < 0.9)
    return val

np.allclose(nb_and(df.x.values, df.y.values), (df.x < 0.9) & (df.y < 0.9))

%timeit -r 10 -n 100 nb_and(df.x.values, df.y.values)
154 µs ± 2.57 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

%timeit -r 10 -n 100 (df.x < 0.9) & (df.y < 0.9)
483 µs ± 2.44 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

%timeit -r 5 -n 100 df.eval('(x < 0.9) & (y < 0.9)')
1.58 ms ± 28.4 µs per loop (mean ± std. dev. of 5 runs, 100 loops each)
```

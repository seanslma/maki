# Pandas

## ravel() vs flatten()
np.ravel() will avoid copy if possible and thus faster than flatten() 

## broadcasting rules
when broadcasting is possible, we do not need to use np.tile()

## slow multiindex methods
Get the mask of the index in both mi1 and mi2 - can be 50x slower.
```
#slow
iboth = mi1.intersection(mi2)
mask1 = mi1.isin(iboth)
mask2 = mi2.isin(iboth)

#fast
d1 = pd.DataFrame(index=mi1, data=np.arange(len(mi1)), columns=['id1'])
d2 = pd.DataFrame(index=mi2, data=np.arange(len(mi2)), columns=['id2'])
df = d1.merge(d2, how='inner', left_index=True, right_index=True)
mask1 = np.full((len(mi1),), False, dtype=bool)
mask1[df.id1] = True
mask2 = np.full((len(mi2),), False, dtype=bool)
mask2[dy.id2] = True
```

## pd.eval
```
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
# 154 µs ± 2.57 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

%timeit -r 10 -n 100 (df.x < 0.9) & (df.y < 0.9)
483 µs ± 2.44 µs per loop (mean ± std. dev. of 10 runs, 100 loops each)

%timeit -r 5 -n 100 df.eval('(x < 0.9) & (y < 0.9)')
1.58 ms ± 28.4 µs per loop (mean ± std. dev. of 5 runs, 100 loops each)
```

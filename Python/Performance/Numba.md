# Numba

## nb vs np.where
```
np.random.seed(0)
df = pd.DataFrame(np.random.rand(100000,2), columns=['x','y'])

import numba as nb
@nb.njit
def nb_where(x, y):
    n = len(x)
    val = np.empty(n, dtype=np.float64)
    for i in range(n):
        if x[i] < 0.9 and y[i] < 0.9:
            val[i] = x[i]
        else:
            val[i] = x[i] + y[i]
    return val
    
assert(np.where((df.x < 0.9) & (df.y < 0.9), df.x, df.x + df.y)==nb_where(df.x.values, df.y.values)).all()

%%timeit -r 7 -n 1000 
mask = (df.x >= 0.9) | (df.y >= 0.9)
df.x[mask] += df.y[mask]
# 6.16 ms ± 14.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit -r 7 -n 1000 np.where((df.x < 0.9) & (df.y < 0.9), df.x, df.x+df.y)
# 1.04 ms ± 1.52 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit -r 7 -n 1000 nb_where(df.x.values, df.y.values)
286 µs ± 2.32 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

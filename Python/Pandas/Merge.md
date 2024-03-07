# Merge

## out merge
```py
d1.merge(d2, how='outer', on=['i', 'j'], suffixes=('_x', '_y'), indicator=True)`
```

## join vs merge
- `join`(... on=[...]) joins **index/columns** of left to **index keys** of right
- `merge` joins **index/columns** of left to **index/columns** of right - less restricted

## avoid `join` with duplicate index
`join` with duplicate index will lead to `m x n` records.
```py
d1 = pd.DataFrame({'v1': [1,5,6]}, index=[1,3,3])
d2 = pd.DataFrame({'v2': [4,6]}, index=[3,3])
d1.join(d2, how='left')
```

## merge on index is 2-3x faster than on column
```py
import time
import numpy as np
import pandas as pd

np.random.seed(11)
n = 1000000

a1 = np.arange(n)
np.random.shuffle(a1)
d1 = (
    pd.DataFrame({'x': a1, 'y': 2*a1})
    # .astype({'x': 'category'})
)

a2 = a1.copy()
np.random.shuffle(a2)
d2 = (
    pd.DataFrame({'x': a2, 'y': 2*a2})
    # .astype({'x': 'category'})
)

# merge on column
t0 = time.time()
d1.merge(d2, how='left', left_on='x', right_on='x')
print(f'Merging on column time: {time.time()-t0:.3f}')

# merge on index
t0 = time.time()
d1.set_index('x').merge(d2.set_index('x'), how='left', left_index=True, right_index=True)
print(f'Merging on index  time: {time.time()-t0:.3f}')
```

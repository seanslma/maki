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

# Merge

## join vs merge
`merge` joins columns of left to columns of right, but `join`(... on=[...]) joins columns of left to **index keys** of right.

## avoid `join` with duplicate index
`join` with duplicate index will lead to m x n records.
```
d1 = pd.DataFrame({'v1': [1,5,6]}, index=[1,3,3])
d2 = pd.DataFrame({'v2': [4,6]}, index=[3,3])
d1.join(d2, how='left')
```

# Issue

## merge drops not used index levels
***caveat***: A `left merge` will drop the index levels not used

## ffill becomes bfill
https://stackoverflow.com/questions/63079668/pandas-how-to-explain-not-sorted-index-reindex-with-fill-values-ffill-behaviour
```py
df = pd.DataFrame(
    np.linspace(1,9,9).reshape(3,3),
    columns=list('abc'),
    index=[3,2,1],
)

df.reindex([0,1,2,3,4], method='ffill')
     a    b    c
0  7.0  8.0  9.0
1  7.0  8.0  9.0
2  4.0  5.0  6.0
3  1.0  2.0  3.0
4  NaN  NaN  NaN

# this works
df.reindex([0, 1, 2, 3, 4]).fillna(method='ffill')
```

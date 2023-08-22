# broadcast

## multiindex
reindex with level can broadcast the level. also df.div can broadcast only one level.

not good, will repeat all combinations:
```py
va = np.array([[1991,1992],[6,7],[8,9],[1,2],[3,4]]).T
df = pd.DataFrame(va,columns=['a','b','c','x','y']).set_index(['a','b','c'])

d2 = df.groupby(['a','c']).mean()
d3 = d2.reindex(df.unstack('b').columns, axis=1, level=0)
d3 = d3.stack(level=1).reorder_levels(['a','b','c'])
```

## broadcast with reindex
get grouped mean and then broadcast back to the original df rows.
```py
va = np.array([[1991,1991,1992],[6,7,7],[8,8,10],[1,2,3],[3,4,5]]).T
df = pd.DataFrame(va,columns=['a','b','c','x','y']).set_index(['a','b','c'])

ia = df.index.get_level_values('a')
ic = df.index.get_level_values('c')
mi = pd.MultiIndex.from_arrays([ia,ic],names=['a','c'])
d2 = df.groupby(['a','c']).mean()
d2.reindex(mi)
d2.reindex(df.index.droplevel('b')) #better? it seems reindex is faster than loc for single index
d2.loc[df.index.droplevel('b'),:] #best?
```

## Expand df date ranges to individual rows
```py
df = (
    df
    .assign(
        DATE=lambda x:
            [
                pd.date_range(row.STARTDATE, row.ENDDATE, freq='d')
                for _,row in x.iterrows()
            ]
    )
    .explode('DATE')
    .drop(['STARTDATE', 'ENDDATE'], axis=1)
)
```

At least 10x faster:
```py
def explode_date_range(
    df: pd.DataFrame,
    start_date_col: str,
    end_date_col: str,
    new_date_col: str = 'ts',
    freq: str = '30T',
    end_date_offset: pd.DateOffset = None,
) -> pd.DataFrame:
    df = df.reset_index(drop=True)
    if end_date_offset is not None:
        df[end_date_col] += end_date_offset
    # Get exploded timestamp column
    dt = (
        pd.concat([
            pd.DataFrame({
                'i': i,
                'ts': pd.date_range(start=s, end=e, freq=freq)
            })
            for i, (s, e) in enumerate(zip(df[start_date_col], df[end_date_col]))
        ])
        .set_index('i')
        .rename_axis(None, axis=0)
    )
    # Re-sample df based on new timestamp column
    df = (
        df
        .drop(columns=[start_date_col, end_date_col])
        .reindex(dt.index)
        .assign(ds=dt.ts)
        .rename(columns={'ds': new_date_col})
    )
    return df
```

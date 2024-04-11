# pandas performance: explode date range in df col

- ai solution
- df.explode solution
- recommended solution

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

## old 
```py
df = (
    df.assign(
        ds=lambda x: [
            pd.date_range(
                start=row[start_date_col],
                end=row[end_date_col],
                freq=freq,
            ) for (_, row) in x.iterrows()
        ],
    )
    .explode('ts')
    .rename(columns={'ts': new_date_col})
    .drop(columns=[start_date_col, end_date_col])
)
```

## new
```py
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

# Re-sampling df based on new timestamp column
df = (
    df
    .drop(columns=[start_date_col, end_date_col])
    .reindex(dt.index)
    .assign(ds=dt.ts)
    .rename(columns={'ds': new_date_col})
)
```

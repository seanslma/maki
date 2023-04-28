# Datetime

## to_datetime
From pandas 2.0, cannot use `datfirst` separatedly. 
```py
# dayfirst applies to all formats (previouslt not yyyy-mm-dd)
to_datetime('2023-02-01', dayfirst=True)
>>> 2023-01-02
# dayfirst does not apply to yyyy-mm-dd format
to_datetime('2023-02-01', dayfirst=True, format='mixed')
>>> 2023-02-01
```

## read_csv
int column will be persed as int64, use `dtype` to set the type to int32.
```py
pd.read_csv(fp,
    index_col=[
        'name',
        'year',
        'quarter',
        'date',
        'value',
    ],
    dtype={
        'year': 'int32',
        'quarter': 'int32',
    },
    parse_dates=['date'],
)
```

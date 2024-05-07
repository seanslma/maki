# Datetime
https://www.confessionsofadataguy.com/date-and-datetime-manipulation-in-polar/
```py
df = pl.DataFrame({'dt': ['2024-10-01', '2024-10-02']})
```

## string to date
```py
df.with_columns(
    dt = pl.col('dt').str.to_datetime().cast(pl.Date)
)
df.with_columns(
    dt = pl.col('dt').str.strptime(pl.Date)
)

ctx = pl.SQLContext(data=df)
ctx.execute('SELECT *, CAST(dt as DATE) as date FROM data', eager=True)
ctx.execute('SELECT *, DATE(dt) as dt FROM data', eager=True)
```

## string to datetime
```py
df.with_columns(
    dt = pl.col('dt').str.to_datetime().cast(pl.Datetime)
)
```

## date to string
```py
df.with_columns(
    dt = pl.col('dt').dt.strftime('%Y-%m-%d')
)
```

## date to yera/month/day
```py
df.with_columns([
    pl.col('dt').dt.year().alias('year'),
    pl.col('dt').dt.month().alias('month'),
    pl.col('dt').dt.day().alias('day'),
])
```

## add days to date column
```py
df.with_columns(
    dt = pl.col('dt') + pl.duration(days=1)
)
```

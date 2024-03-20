# How to create pandas test dataframe

## create string column

## create datetime column
Assume we will create a datetime range for one year with second resolution
```py
start_date = np.datetime64('2020-01-01 00:00:00') # must include the H:M:S
end_date = np.datetime64('2021-01-01 00:00:00')
```

We can create a datetime column using numpy
```py
%%timeit
low = start_date.astype(int)
high = end_date.astype(int)
t1 = np.arange(low, high, step=(high - low)//(366*24*3600)).astype('datetime64[s]')
d1 = pd.DataFrame({'ts': t1})
# 319 ms ± 12.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

We can also create it using pandas
```py
%%timeit
t2 = pd.date_range(start_date, end_date, periods=(366*24*3600)+1, inclusive='left', unit='s')
d2 = pd.DataFrame({'ts': t2})
# 930 ms ± 44.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

numpy version is much faster but less convinient.

We can also generate random date values between a range
```py
rng = np.random.default_rng(seed=11)
start_date = np.datetime64('2020-01-01') 
end_date = np.datetime64('2021-01-01')
low = start_date.astype(int)
high = end_date.astype(int)
ts = rng.integers(low, high, size=100).astype('datetime64[D]')
```

## create integer column

## create float column

## create dataframe

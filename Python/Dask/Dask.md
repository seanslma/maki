# Dask

https://gist.github.com/fionaRust/c7953629690a8be2e7477f266b113877

## dask tutorial
https://github.com/dask/dask-tutorial


## when to use
Dask provides convenience to parallelize code, better than multiprocessing and joblib.

Also compared to pandas, dask can filter parquet file row by row when reading. So if do not need all the data tis can be faster.

If load the total file all together, pandas is much faster.

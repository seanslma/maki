# DataFrame

## MultiIndex
cavaet: **NotImplementedError**: *Dask dataframe does not yet support multi-indexes*. At least not fully supported.

- If multiindex is not required, save the dataframe as a parquet file by resetting the index. 
- It's much faster to load a parquet file without multiindex, though the total time including recreating the index is a little longer.
- Aslo, we can read any level separately much faster - with multiindex, we need to read all the index levels together. 

## Partition

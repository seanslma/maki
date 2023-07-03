# DataFrame

## MultiIndex
cavaet: *NotImplementedError: Dask dataframe does not yet support multi-indexes*

If multiindex is not required, save the dataframe as a parquet file by resetiing the index. 
It's much faster to load a parquet file without multiindex, though the total time including recreating the index is a little longer.
Aslo, wecan read any level separately - with multiindex, we need to read all the index levels together. 

## Partition

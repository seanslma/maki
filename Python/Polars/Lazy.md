# Lazy

## Eager and Lazy APIs
https://benfeifke.com/posts/the-3-reasons-why-i-switched-from-pandas-to-polars-20230328/
```
                    Eager API        Lazy API
---------------------------------------------------
Dataframe Creation	DataFrame()      LazyFrame()
Input CSV           read_csv()       scan_csv()
Input Parquet       read_parquet()   scan_parquet()
Output Parquet      write_parquet()	 sink_parquet()
```

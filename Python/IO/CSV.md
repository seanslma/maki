# CSV

## csv reading perf
- https://datapythonista.me/blog/how-fast-can-we-process-a-csv-file
- https://github.com/datapythonista/bench_csv
```
pandas with C engine                    pandas_c                     1.501
pandas with PyArrow engine and PyArrow  dtypespandas_pyarrow_arrow   0.292
NumPy with loadtxt function             numpy_loadtxt                1.835
DuckDB 0.9.2 with SQL API               duckdb_sql                   0.817
DuckDB 0.10.0 with SQL API              duckdb_sql                   0.289
DataFusion with SQL API                 datafusion_sql               0.206
Polars in eager mode                    polars_eager                 0.114
Polars in lazy mode                     polars_lazy                  0.106
Polars in streaming mode                polars_streaming             0.115
Polars with SQL API                     polars_sql                   0.098
```

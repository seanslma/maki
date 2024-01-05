# DuckDB

## DuckDB vs Sqlite
DuckDB is optimized for queries that apply aggregate calculations across large numbers of rows, 
whereas SQLite is optimized for fast scanning and lookup for individual rows of data. 

If you need to perform analytical queries, go with DuckDB otherwise, use SQLite.

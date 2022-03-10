# DuckDB
DuckDB is an in-process SQL OLAP database management system

When to use DuckDB
- Processing and storing tabular datasets, e.g. from CSV or Parquet files
- Interactive data analysis, e.g. Joining & aggregate multiple large tables
- Concurrent large changes, to multiple large tables, e.g. appending rows, adding/removing/updating columns
- Large result set transfer to client

When to not use DuckDB
- Non-rectangular data sets, e.g. graphs
- High-volume transactional use cases (e.g. tracking orders in a webshop)
- Large client/server installations for centralized enterprise data warehousing
- Writing to a single database from multiple concurrent processes

## Example
### connection
```
import duckdb
con = duckdb.connect(database=':memory:') #in-memory database
con = duckdb.connect(database='my-db.duckdb', read_only=False) #database file (not shared between processes)
con = duckdb.connect(database='my-db.duckdb', read_only=True)  #database file (shared between processes)
```

### query
```
con.execute("CREATE TABLE items(item VARCHAR, value DECIMAL(10,2), count INTEGER)")
con.execute("INSERT INTO items VALUES ('jeans', 20.0, 1), ('hammer', 42.2, 2)")

con.execute("SELECT * FROM items")
print(con.fetchall())
# [('jeans', 20.0, 1), ('hammer', 42.2, 2)]

con.execute("INSERT INTO items VALUES (?, ?, ?)", ['laptop', 2000, 1])
con.executemany("INSERT INTO items VALUES (?, ?, ?)", [['chainsaw', 500, 10], ['iphone', 300, 2]] )
con.execute("SELECT item FROM items WHERE value > ?", [400])
```

### pandas
```
import pandas as pd
con.register('df_view', df)
con.execute('SELECT * FROM df_view')
con.fetchall()

# fetch as pandas data frame
df = con.execute("SELECT * FROM items").fetchdf()
# fetch as dictionary of numpy arrays
arr = con.execute("SELECT * FROM items").fetchnumpy()
```

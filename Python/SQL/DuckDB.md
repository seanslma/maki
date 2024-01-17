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

## install
```sh
mamba install python-duckdb -y
```

## Example
### connection
```py
import duckdb
con = duckdb.connect(database=':memory:') #in-memory database
con = duckdb.connect(database='my-db.duckdb', read_only=False) #database file (not shared between processes)
con = duckdb.connect(database='my-db.duckdb', read_only=True)  #database file (shared between processes)
```

### query
```py
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
```py
import pandas as pd
con.register('df_view', df)
con.execute('SELECT * FROM df_view')
con.fetchall()

# fetch as pandas data frame
df = con.execute("SELECT * FROM items").fetchdf()
# fetch as dictionary of numpy arrays
arr = con.execute("SELECT * FROM items").fetchnumpy()
```

## `register` vs `CREATE TABLE df AS SELECT * FROM df`
```py
con = duckdb.connect(':memory:')
con.register('df', df)
con.execute("CREATE TABLE my_table AS SELECT * FROM df")
```

**`duckdb.register('df', df)`:**
- **Registers a virtual table:** Makes a DataFrame accessible within DuckDB without physically copying data.
- **No persistence:** Virtual table disappears when DuckDB connection closes.
- **Query-only:** Changes to the virtual table don't affect the original DataFrame.
- **Ideal for:** Quick queries and exploration without data duplication.

**`conn.execute("CREATE TABLE df AS SELECT * FROM df")`:**
- **Creates a persistent table:** Stores data physically in DuckDB's database.
- **Data copied:** Data is copied from the DataFrame into DuckDB's storage.
- **Independent table:** Changes to the table within DuckDB don't affect the original DataFrame.
- **Ideal for:** Persisting data, complex queries, sharing data across sessions.

## performance
have some data (e.g., NEM demand data for different generators and days/intervals). Now there are some new data that can be either updated demand or demand in new days. We need update/insert the new data into the original data.

In this case, will it be faster by using duckdb to hold the original data then upsert the new data to duckdb, compared to directly using pandas? write the code to test it!

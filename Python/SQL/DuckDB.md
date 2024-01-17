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

For a parquet file about 10MB, the pandas code is 2-3x faster compared to duckdb.

**pandas outer merge**
```py
# %%timeit
# Merge DataFrames, prioritizing df2's values
df = pd.merge(d1, d3, how='outer', on=d1.index.names, suffixes=('', '_update'))

# Update sales_amount where values are present in df2
cols_update = []
for col in d1.columns:
    col_update = f'{col}_update'
    cols_update.append(col_update)
    df[col] = df[col_update].fillna(df[col])

# Drop unnecessary columns
df1 = df.drop(columns=cols_update)
```

**duckdb upsert**: cannot register d1 as a virtual table because it will be modified 
```py
# %%timeit
# Connect to a DuckDB database
conn = duckdb.connect()

# Load DataFrames into DuckDB
d1t = d1.reset_index()
conn.execute('CREATE TABLE d1 AS SELECT * FROM d1t')
conn.register('d2', d3.reset_index())

# Perform the upsert using SQL
id_cols = ', '.join(d1.index.names)
dat_cols = ', '.join(d1.columns)
upd_vals = ', '.join([f'{col} = EXCLUDED.{col}' for col in d1.columns])
conn.execute(f'CREATE UNIQUE INDEX i1 ON d1 ({id_cols})')

conn.execute(f'''
    INSERT INTO d1 ({id_cols}, {dat_cols})
    SELECT {id_cols}, {dat_cols}
    FROM d2
    ON CONFLICT ({id_cols}) DO UPDATE SET {upd_vals}
''')

# Retrieve the updated DataFrame
df2 = conn.execute('SELECT * FROM d1').fetchdf()

# Close the connection
conn.close()
```

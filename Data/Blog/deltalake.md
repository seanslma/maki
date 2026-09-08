# Use `delta_scan` instead of `to_pyarrow_dataset` for performace in reading delta lake data

When querying Delta Lake tables stored in Azure Data Lake Storage (ADLS) with DuckDB, I found two common approaches:

- Using `delta-rs` and `to_pyarrow_dataset()`
- Using DuckDB's native `azure` and `delta` extensions through `delta_scan()`

In my testing, the second approach was consistently 3 to 4 times faster.

Here I will show you both implementations and explain why `delta_scan()` can deliver significantly better performance when DuckDB is your query engine.

## Option 1: `delta-rs` and `to_pyarrow_dataset()`

With this approach, the query path looks like this:

```
ADLS
  ↓
delta-rs
  ↓
PyArrow Dataset
  ↓
DuckDB Arrow Scan
```

The Delta table is first loaded through `delta-rs`, converted into a PyArrow dataset, and then registered with DuckDB.

This introduces an additional Arrow abstraction layer between Delta Lake and DuckDB. 
In practice, this extra layer can add noticeable overhead, especially when working with larger datasets (for more details, see the references section).

Here is the implementation detail:

```py
def get_storage_bearer_token() -> str:
    credential = DefaultAzureCredential()
    return credential.get_token(
        'https://storage.azure.com/.default'
    ).token

def get_delta_table_path(
    storage_account: str,
    container_name: str,
    relative_path: str,
) -> str:
    return (
        f'abfss://{container_name}@'
        f'{storage_account}.dfs.core.windows.net/{relative_path}'
    )

def get_duckdb_conn_delta_table(
    delta_table_path: str,
    table_name: str = 'delta_table',
):
    conn = duckdb.connect()
    token = get_storage_bearer_token()
    dataset = DeltaTable(
        delta_table_path,
        storage_options={'bearer_token': token},
    ).to_pyarrow_dataset()
    conn.register(table_name, dataset)
    return conn
```

Note that the example above uses a pre-fetched bearer token for simplicity.

For production workloads, consider using a more persistent authentication mechanism so DuckDB can manage credential refresh automatically. 
Depending on your environment, options may include:

- `credential_chain`
- `service_principal`
- explicit secret configuration

This becomes especially important for long-running services where access tokens may expire during execution.

## Option 2: DuckDB `delta` extension and `delta_scan()`

With DuckDB's Delta extension, the execution path is:

```
ADLS
  ↓
DuckDB Delta Extension
  ↓
DuckDB Query Engine
```

Instead of going through `delta-rs` and PyArrow, DuckDB reads the Delta table directly. This allows the engine to handle internally:

- scan planning
- partition pruning
- file pruning
- metadata loading
- metadata caching

Because DuckDB has been heavily optimising its Delta extension, this direct integration is likely the main reason for the performance improvement I observed.

Before using `delta_scan()`, DuckDB needs a few extensions: `httpfs`, `delta` and `azure`. 
The `httpfs` extension is required to setup the secure HTTP connection for downloading `delta` and `azure`. 
However, if your environment blocks the HTTP connection, you need to manually download the `httpfs` extension and unzip it into the DuckDB extension folder. 
In that case, remove the `INSTALL httpfs;` statement and keep only the `LOAD httpfs;` command.

The following is the implementation detail for this approach:

```py
def get_duckdb_conn_delta_scan(
    delta_table_path: str,
    table_name: str = 'delta_table',
):
    conn = duckdb.connect()
    conn.execute("""
        INSTALL httpfs; LOAD httpfs;
        INSTALL delta; LOAD delta;
        INSTALL azure; LOAD azure;
    """)
    token = get_storage_bearer_token()
    conn.execute(f"""
        CREATE OR REPLACE SECRET azure_secret (
            TYPE azure,
            PROVIDER access_token,
            ACCESS_TOKEN '{token}',
            ACCOUNT_NAME '{storage_account}'
        );
    """)
    conn.execute(f"""
        CREATE OR REPLACE VIEW {table_name} AS
        SELECT * FROM delta_scan('{delta_table_path}');
    """)
    return conn
```

## How to run the test

For testing, I used a simple helper function that executes a query and returns either a Pandas or Polars DataFrame.

```py
def get_df_from_path(
    path: str,
    query: str,
    df_type: str = 'pandas',
) -> pd.DataFrame | pl.DataFrame:
    with get_duckdb_conn(path) as conn:
        if df_type == 'pandas':
            results = conn.execute(query).df()
        else:
            results = conn.execute(query).pl()
    return results
```

You can easily adapt this function to benchmark both approaches against your own Delta tables.

## References

- https://github.com/delta-io/delta-rs/issues/631
- https://github.com/delta-io/delta-rs/issues/1569
- https://github.com/delta-io/delta-rs/issues/4362
- https://github.com/duckdb/duckdb-delta/issues/35

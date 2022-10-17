# DeltaLake

Delta Lake is a storage layer that adds relational database semantics to Spark-based data lake processing.

## managed and external tables
Tables in a Spark catalog, including Delta Lake tables, can be managed or external.

managed
- managed table is defined without a specified location, and the data files are stored within the storage used by the metastore.
- Dropping the table not only removes its metadata from the catalog, but also deletes the folder in which its data files are stored.

external
- external table is defined for a custom file location, where the data for the table is stored.
- The metadata for the table is defined in the Spark catalog.
- Dropping the table deletes the metadata from the catalog, but doesn't affect the data files

## create tables from dataframe
```
df.write.format('delta').saveAsTable('managed_table')
df.write.format('delta').option('path', '/mydata').saveAsTable('external_table')
```

## create tables from sql
```
spark.sql("CREATE TABLE MyExternalTable USING DELTA LOCATION '/mydata'")

%sql
CREATE TABLE MyExternalTable
USING DELTA
LOCATION '/mydata'
```

## table schema
define the table schema by specifying the column `names`, `types`, and `nullability` as part of the CREATE TABLE statement.
```
%sql

CREATE TABLE ManagedSalesOrders
(
    Orderid INT NOT NULL,
    OrderDate TIMESTAMP NOT NULL,
    CustomerName STRING,
    SalesTotal FLOAT NOT NULL
)
USING DELTA
```

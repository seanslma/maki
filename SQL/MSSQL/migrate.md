# migrate

- download and install MySQL ODBC Connector
- download and install SQL Server Migration Assistant for MySQL platform

## from mysql
### Zero datetime
With data type datetime (Transact-SQL) you can store date values from 1753-01-01 onward, with datetime2 (Transact-SQL) from year 0001 on, but never from year 0000.

zero datetime ['0000-00-00 00:00:00'] will cause migration error in ssma: Column 'xx' does not allow DbNull value.

**solution**: change the value to 1900-01-01 00:00:00 in the mysql tables.

```sql
-- list table cols with default zero datetime
SELECT c.table_schema, c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE, c.IS_NULLABLE, c.COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS as c
inner join INFORMATION_SCHEMA.Tables as t
on t.table_schema = c.table_schema and t.table_name = c.table_name
WHERE t.Table_Type = 'BASE TABLE' and c.IS_NULLABLE = 'NO' and c.COLUMN_DEFAULT like '0000-00-00%';

-- change datatime to 1900-01-01 00:00:00
update 24c_lite.bids_forecast
set BIDOFFERDATE = '1900-01-01 00:00:00'
if BIDOFFERDATE = '0000-00-00 00:00:00';
```

### failed on large table about 5GB
I had the same error in SSMA while migrating a table from Oracle to SQL Server. The table had 1000 million records and the migration used to fail after 90% of transfer.

By making the changes in project setting **BATCH SIZE** under TOOLS > PROJECT SETTINGS > GENERAL> MIGRATION to 1000 and **TIME OUT** to 1000, it completed successfully.

### Connection closed
Cannot truncate target table. Reason: ExecuteReader requires an open and available Connection. The connection's current state is closed.

**solution**: Go to Tools > Project Settings > General and in the left pane click on Migration and then in the right pane, in the section Misc, change **Data migration timeout in minutes** property to something larger (the default value was 15; I changed it to 300).

By making the changes in project setting BATCH SIZE under TOOLS > PROJECT SETTINGS > GENERAL> MIGRATION to 1000 and TIME OUT to 1000, it completed successfully.

### Login Failed for User
Microsoft SQL Server, Error: 18456

check and update user permissions: grant public and sysadmin roles

and also add server login in configuration:
* Open your SQL Server Management Studio
* Right click on the database server and go to properties
* Choose the security option and check "**SQL Server and Windows authentication mode**"
* Enable TCP/IP connection in SQL Configuration Manager
* Restart your SQL server

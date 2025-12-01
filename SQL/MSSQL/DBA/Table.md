# Table

## Get table description
```sql
SELECT
  obj.name AS table_name, col.name AS column_name, ep.value AS column_description
FROM sys.objects obj
INNER JOIN sys.schemas s
  ON obj.schema_id = s.schema_id
INNER JOIN sys.columns col
  ON obj.object_id = col.object_id
LEFT JOIN sys.extended_properties ep
  ON obj.object_id = ep.major_id AND col.column_id = ep.minor_id AND ep.name = 'MS_Description'
WHERE
  obj.type_desc = 'USER_TABLE' AND s.name = 'schema-name' AND obj.name = 'table-name'
```

## Delete versioned table records in sql server
- 1. Upscale: As the database is full, upscale quota limit
- 2. Disable system versioning temporarily
- 3. Batch Delete Data from `Main Table`: Execute the batch delete script on the main temporal table (`my_schema.sales`) to move old records to the history table without overwhelming the log.
- 4. Batch Delete Data from `History Table`: Temporarily disable versioning and execute the batch delete script on the history table (`my_schema_history.sales`).
- 5. Re-enable system versioning and link to the history table again
- 6. Shrink the Database: Run the `DBCC SHRINKDATABASE ('My_DB')` command to reclaim the unused space from the data and log files. This is the step that will physically reduce the database size.
- 7. Downscale (Optional): Once the size has been safely reduced and the database is below the old quota limit, you can safely return to the Azure Portal and scale the database back down to its original size limit, if you wish to save cost.

### Disable system versioning temporarily
```sql
ALTER TABLE [my_schema].[sales]
SET (SYSTEM_VERSIONING = OFF);
```

### Delete records
```sql
WHILE 1=1
BEGIN
    DELETE TOP (20000)
    FROM [my_schema].[sales]
    WHERE as_of_timestamp < '2024-01-01';
    IF @@ROWCOUNT = 0 BREAK;
END
```

### Delete all records if no longer in use
```sql
TRUNCATE TABLE [my_schema].[sales];
```

### Re-enable system versioning and link to the history table again
```sql
ALTER TABLE [my_schema].[sales]
SET (SYSTEM_VERSIONING = ON (HISTORY_TABLE = [my_schema_history].[sales]));
```

### Check table type
```sql
SELECT
    s.name AS SchemaName,
    t.name AS TableName,
    t.temporal_type AS TemporalType,
    t.temporal_type_desc AS TemporalTypeDesc
FROM sys.tables AS t
JOIN sys.schemas AS s
	ON t.schema_id = s.schema_id
LEFT JOIN sys.tables AS ht
	ON t.history_table_id = ht.object_id
ORDER BY
    s.name, t.name;
```

### Check table space usage
```sql
SELECT
    s.name AS schema_name,
    t.name AS table_name,
    SUM(a.total_pages) * 8 / 1024 / 1024 AS used_gb,
    p.rows AS row_count
FROM
    sys.tables t
JOIN
    sys.schemas s ON t.schema_id = s.schema_id
JOIN
    sys.indexes i ON t.object_id = i.object_id
JOIN
    sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
JOIN
    sys.allocation_units a ON p.partition_id = a.container_id
WHERE
    t.is_ms_shipped = 0  -- Exclude system tables
    AND i.type <= 1      -- Include only heap (0) or clustered index (1)
GROUP BY
    s.name, t.name, p.rows
ORDER BY
    s.name, t.name;
```

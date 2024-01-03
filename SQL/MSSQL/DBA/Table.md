# Table

## Get table description
```sql
SELECT obj.name AS table_name, col.name AS column_name, ep.value AS column_description
FROM sys.objects obj
INNER JOIN sys.schemas s ON obj.schema_id = s.schema_id
INNER JOIN sys.columns col ON obj.object_id = col.object_id
LEFT JOIN sys.extended_properties ep ON obj.object_id = ep.major_id AND col.column_id = ep.minor_id AND ep.name = 'MS_Description'
WHERE obj.type_desc = 'USER_TABLE' AND s.name = 'schema-name' AND obj.name = 'table-name'
```

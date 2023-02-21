# Foreign key

## listed all referencing tables
```
SELECT OBJECT_NAME(f.parent_object_id) AS referencing_table, 
       COL_NAME(fc.parent_object_id, fc.parent_column_id) AS referencing_column, 
       OBJECT_NAME(f.referenced_object_id) AS referenced_table, 
       COL_NAME(fc.referenced_object_id, fc.referenced_column_id) AS referenced_column
FROM sys.foreign_keys AS f
INNER JOIN sys.foreign_key_columns AS fc ON f.object_id = fc.constraint_object_id
where OBJECT_NAME(f.referenced_object_id) = 'referenced_table' 
  and COL_NAME(fc.referenced_object_id, fc.referenced_column_id) = 'referenced_column'
ORDER BY referencing_table;
```

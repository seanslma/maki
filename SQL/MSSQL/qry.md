# query

```sql
USE [test]
DECLARE @Command nvarchar(max), @ConstraintName nvarchar(max), @TableName nvarchar(max), @ColumnName nvarchar(max)
SET @TableName = 'rec.get'
SET @ColumnName = 'LAST_UPDATE'
SELECT @ConstraintName = name
    FROM sys.default_constraints
    WHERE parent_object_id = object_id(@TableName)
        AND parent_column_id = columnproperty(object_id(@TableName), @ColumnName, 'ColumnId')

SELECT @Command = 'ALTER TABLE ' + @TableName + ' DROP CONSTRAINT ' + @ConstraintName  
EXECUTE sp_executeSQL @Command

SELECT @Command = 'ALTER TABLE ' + @TableName + ' ADD CONSTRAINT ' + @ConstraintName + ' DEFAULT (''1900-01-01'') FOR ' + @ColumnName 
EXECUTE sp_executeSQL @Command
```
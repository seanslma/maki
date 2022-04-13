# Table edit

## delete table data
```sql
delete from my_table_name;
```

## Reset AutoIncrement in SQL Server after Delete
```sql
SELECT MAX(my_column_name) as vmax FROM my_table_name #get max val
DBCC CHECKIDENT('db.schema.my_table_name', RESEED, vmax-1) #reset autoincrement seed
```

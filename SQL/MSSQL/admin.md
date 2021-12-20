# admin

## stop server
SQL Server agent is dependent on SQL Service. \\
So before stopping MSSQL, Server agent service needs to be stopped. 
```dos
sc stop sqlserveragent
sc stop mssqlserver
```

## create a user
or use UI and add the roles: public and sysadmin 
  CREATE USER Mary WITH PASSWORD = '********';
  
## show users
```sql
select name as username,
       create_date,
       modify_date,
       type_desc as type,
       authentication_type_desc as authentication_type
from sys.database_principals
where type not in ('A', 'G', 'R', 'X')
      and sid is not null
      and name != 'guest'
order by username;  
```

## create db
```sql
CREATE DATABASE test;
```

## show dbs
```sql
SELECT name FROM master.sys.databases;
SELECT name FROM master.dbo.sysdatabases;

--exlude system dbs
SELECT * FROM master.sys.databases d WHERE d.database_id > 4
SELECT * FROM master.sys.databases d WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');
```

## get table cols
```sql
Select table_name, column_name, data_type, ordinal_position 
From INFORMATION_SCHEMA.COLUMNS 
Where table_catalog = 'cat' and table_schema = 'sch' and TABLE_NAME = 'tbl';
```

## get table keys
```sql
SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_CATALOG = 'CAT' AND TABLE_SCHEMA ='SCH' AND TABLE_NAME = 'TBL'
order by ORDINAL_POSITION;
```

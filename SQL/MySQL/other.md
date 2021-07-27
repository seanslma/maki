## other

start mysql server:
C:\> "C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqld" --console

### basic
```sql
show full processlist;

show variables like "%timeout%";

#full-text search
SELECT * FROM schema.table
WHERE MATCH (reason) AGAINST ('x-y-z' IN BOOLEAN MODE);

#command line
mysql -h host -P port -u user -p db
```

### DBA
```sql
--mysql server version
SHOW VARIABLES LIKE '%version%';

--show tables in db
use dbname;
show tables;

--show table index
SHOW INDEX FROM mytable;

--show column info
--obtain information about table structure
describe tbl;
--displays information about the columns in a given table. It also works for views
show columns from tbl;

--get tbl size in db
SELECT table_name AS 'Table',
       ROUND((data_length + index_length) / 1024 / 1024, 2) AS 'SizeMB'
FROM information_schema.tables
WHERE table_schema = 'db_name'
ORDER BY SizeMB DESC
;

--get db size and free space
SELECT table_schema AS 'DBName',
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) AS 'SizeMB',
       ROUND(SUM(data_free)/ 1024 / 1024, 1) AS 'FreeSpaceMB'
FROM information_schema.tables 
WHERE table_schema = 'db_name'
GROUP BY table_schema
; 

--find db tables with specific column names
SELECT DISTINCT TABLE_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME IN ('column1', 'column2') AND TABLE_SCHEMA='dbname'
;

--find db with specific table name
select table_schema, table_name 
from information_schema.tables 
where table_name like '%xyz%'
;

--get table number of columns
SELECT COUNT(*) AS ncl 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_schema = 'db' AND table_name = 'tbl'
;

```
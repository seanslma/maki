# Admin

by default, mysql8 enabled -log-bin, can be disabled by skip-log-bin

```sql
--drop db
DROP DATABASE [IF EXISTS] db_name;
--drop table
DROP TABLE IF EXISTS table1, table2;
```

# restart
mysql did not release memory, restart can release 1.5GB
## check version
```sql
SHOW VARIABLES LIKE '%version%';

show create table my_table_name;
```

## log timestamp
change report time to local
  [mysqld]
  log_timestamps = SYSTEM

## change root password
in inti.txt add:\\
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('MyNewPass');

in cmd:\\
mysqld --init-file=C:\init.txt --console

update user set authentication_string=password('password') where user='root'; 

## Dump and Reload Method
when dump all databases, please remember to exclude the system dbs, otherwise you will have issue to log into the server.
```sql
--all dbs
mysqldump --all-databases > dump.sql
mysql < dump.sql

--all tables
mysqldump db_name > dump.sql
mysql db_name < dump.sql

--one table
mysqldump db_name t1 > dump.sql
mysql db_name < dump.sql

--optimized
mysqldump --opt mydatabase > dump.sql

--disable tables locking during the dump in InnoDB
mysqldump dbname --single-transaction > dump.sql

--restore another way
mysql -uroot -p --default-character-set=utf8 foo
mysql> SET names 'utf8'
mysql> SOURCE foo.dump
```

## Rename database name
```dos
mysqldump -u username -P 3306 -p -R oldDbname > oldDbname.sql
mysqladmin -u username -P 3306 -p create newDbname
mysql -u username -P 3306 -p newDbname < oldDbname.sql
```

## REPAIR TABLE Method
the REPAIR TABLE method is only applicable to MyISAM, ARCHIVE, and CSV tables
```sql
CHECK TABLE t1;
REPAIR TABLE t1;
mysqlcheck db_name [tbl_name]
mysqlcheck --repair --databases db_name
mysqlcheck --repair --all-databases
```

## repair key
Error: Incorrect key file for table '.\db\tbl_name.MYI'; try to repair it

```mysql
REPAIR TABLE tbl_name USE_FRM;
```

The USE_FRM option is available for use if the .MYI index file is missing or if its header is corrupted. This option tells MySQL not to trust the information in the .MYI file header and to re-create it using information from the .frm file. This kind of repair cannot be done with myisamchk

## save a few db tables
```dos
@echo off

set db=test
set tbl=xxx_tbl
set file="C:\db_tbl.sql"

set mysqlexe="C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe"
set mysqldumpexe="C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe"

rem Dump db tables to sql file
%mysqldumpexe% -h sql.server -P 3306 -u usr -p %1 %db% %tbl% > %file%
          
echo all done!
```

## copy db to another server
```dos
@echo off

set dbnew=new_db
set dbold=old_db
set dbfile="C:\db.sql"

set mysqlexe="C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe"
set mysqldumpexe="C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe"

rem Dump db to sql file
%mysqldumpexe% -h sql.server -P 3306 -u usr -p %1 %dbold% > %dbfile%
rem only dump structure: %mysqldumpexe% -d -h sql.server -P 3306 -u usr -p %1 %dbold% > %dbfile%
rem Create an empty db
%mysqlexe% -h sql.server -P 3306 -u usr -p %1 -e "create database if not exists %dbnew%;"
rem Import the db
%mysqlexe% -h sql.server -P 3306 -u usr -p %1 %dbnew% < %dbfile%             

echo all done!
```

## alter table performance
https://www.percona.com/forums/questions-discussions/mysql-and-percona-server/957-alter-table-performance-with-myisam

The workaround which I found so far is really ugly, however I've seen users using it with good success. 
  - You can create table of the same structure without keys, 
  - Load data into it to get correct .MYD, 
  - Create table with all keys defined and copy over .frm and .MYI files from it,
  - followed by FLUSH TABLES. 
  - Now you can use REPAIR TABLE to rebuild all keys by sort, including UNIQUE keys.

## check database / table size
```sql
--sizes of all of dbname
SELECT table_schema AS database, 
       SUM(index_length) / 1024 / 1024 / 1024 AS ind_GB,
       SUM(data_length) / 1024 / 1024 / 1024 AS dat_GB,
       SUM(data_free) / 1024 / 1024 / 1024 AS dfr_GB
FROM information_schema.TABLES 
GROUP BY table_schema
order by dat_GB;

--size of one database
SELECT table_schema as dbname,
       ROUND(SUM(data_length + index_length) / 1024 / 1024 / 1024, 2) as size_GB  
FROM information_schema.tables 
where table_schema = 'database_name'
GROUP BY table_schema; 

--sizes of all tables in a specific database
SELECT table_name AS tb,
(data_length / 1024 / 1024 / 1024) AS dat_GB, 
(index_length / 1024 / 1024 / 1024) AS ind_GB 
FROM information_schema.TABLES
WHERE table_schema = 'database_name'
ORDER BY (data_length + index_length) DESC;
```

## list tables with a specific colname
```sql
SELECT t.TABLE_NAME, t.data_length/1024/1024/1024 as dsz, t.index_length/1024/1024/1024 as isz
FROM INFORMATION_SCHEMA.tables as t
WHERE t.TABLE_SCHEMA = 'mydb' and t.table_type = 'BASE TABLE'
and t.table_name in 
(
  SELECT distinct c.TABLE_NAME
  FROM INFORMATION_SCHEMA.COLUMNS as c
  WHERE c.COLUMN_NAME = 'mycol' AND c.TABLE_SCHEMA = 'mydb' 
)
ORDER BY (t.data_length + t.index_length) asc;
```

## check database last update time
```sql
SELECT table_schema as db, max(update_time) as upd_time
FROM   information_schema.tables
WHERE  table_schema = 'mydb'
group by table_schema;
```

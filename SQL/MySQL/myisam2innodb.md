# MyISAM to InnoDB
## swap tables
```sql
RENAME TABLE old_table TO tmp_table, new_table TO old_table, tmp_table TO new_table;
```

## alter table
```sql
ALTER TABLE db.tbl
DROP PRIMARY KEY,
ADD PRIMARY KEY (`dt`,`id`) USING BTREE,
ENGINE = InnoDB
PARTITION BY RANGE (YEAR(`DATETIME`)) (
  PARTITION l2016 VALUES LESS THAN (2016),
  PARTITION l2019 VALUES LESS THAN (2019),
  PARTITION l2021 VALUES LESS THAN (2021),
  PARTITION l2022 VALUES LESS THAN (2022)
);
```

## dump data to csv file
```bat
@echo off

set db=%1
set tb=%2

set curdir=%~dp0
set tbdir="C:/ProgramData/MySQL/MySQL Server 8.0/Data/tmp"

set par=--fields-terminated-by=0x2C --fields-optionally-enclosed-by=0x22 --fields-escaped-by=0x5C --lines-terminated-by=0x0a
set dumpexe="C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"

echo %date% %time% table: %db%.%tb%
%dumpexe% --defaults-extra-file=%curdir%sql_svr.cnf --tab=%tbdir% %db% %tb% %par%
echo %date% %time% all done!
```

## load csv file to InnoDB
```bat
@echo off

set db=%1
set tb=%2

set curdir=%~dp0
set tbdef=C:/ProgramData/MySQL/MySQL Server 8.0/Data/tmp/%tb%.sql
set tbfile=C:/ProgramData/MySQL/MySQL Server 8.0/Data/tmp/%tb%.txt

set par=CHARACTER SET latin1 FIELDS TERMINATED BY 0x2C OPTIONALLY ENCLOSED BY 0x22 ESCAPED BY 0x5C LINES TERMINATED BY 0x0a
set sqlexe="C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"

echo %date% %time% table: %db%.%tb%_myisam

%sqlexe% --defaults-extra-file=%curdir%sql_svr.cnf %db% < "%tbdef%"
echo %date% %time% created innodb table with partitions

set sql_qry="LOAD DATA INFILE '%tbfile%' INTO TABLE %db%.%tb%_myisam %par%"
%sqlexe% --defaults-extra-file=%curdir%sql_svr.cnf --local-infile -e %sql_qry% --show-warnings
echo %date% %time% loaded data to new innodb table

echo %date% %time% all done!
```

# MyISAM to InnoDB

## dump data to csv file
```dos
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
```dos
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

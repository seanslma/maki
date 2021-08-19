# backup
  * disable slow log 
  * change tmp dir to a large drive
  * change repair params to large values

## compress
Defragmentation will not only recover space, it will also help the queries run faster.\\
After dumping and import the data can become larger, compress it
  optimize table tb1, tb2
  mysqlcheck -o db tb #mysqlcheck uses “OPTIMIZE TABLE” command
  mysqlcheck -o db    #all tbs
  mysqlcheck -o -A    #all dbs
## check process
  select * from INFORMATION_SCHEMA.PROCESSLIST where db = 'dbname';

## log-slow-queries
If you are importing using: mysql -u user -p db_name < db.sql, check that you do **NOT** have "log-slow-queries" turned on.
  show global variables like '%slow%';
  set global slow_query_log = 'OFF';

## get all tables in db
```sql
select table_name as 'tbl'
from information_schema.tables
where table_schema = 'database_name';
```

## Lost connection during query when dumping
possible solutions, increase the variables values:
  mysqldump --net-read-timeout=7200 --net-write-timeout=7200 
            --net-buffer-length=32704 --max_allowed-packet=1024M 

use --compress (does not work):
  mysqldump --defaults-extra-file=$dir/svr1.cnf $db $tb | 
  mysql --defaults-extra-file=$dir/svr2.cnf --compress $db


## dump to tsv
when using LOAD DATA INFILE, the character set should be set to the character set of the source csv file. This again should be the same as the character set in the definition of the table. So when using mysqldump to create the csv files, the character set should also be set to the character set in the table.

get table character set:\\
SHOW FULL COLUMNS FROM db.tb;
```dos
mysqldump -h host -P port -u user -ppass --tab=/dir mydb mytable
$ mysql -h localhost -u root -p
mysql> LOAD DATA INFILE '/tmp/mytable.txt' INTO TABLE mytable;

set qry=USE db1;LOAD DATA LOCAL INFILE '!file!' INTO TABLE !table!
set pa1=FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"^""'
set pa2=LINES TERMINATED BY '\n' character-set latin1 IGNORE 1 LINES;
set sql_qry=%qry% %pa1% %pa2%
mysql -u root --password=%password% -e "sql_qry" --verbose --show-warnings
```

## dump to csv
LOAD DATA INFILE requires txt data path in the **server data folder**\\
LOAD DATA LOCAL INFILE is slower as a copy has to be made to the server disk
```dos
mysqldump -h host -P port -u user -ppass --tab=/dir mydb mytable
mysqldump --tab=/tmp --fields-terminated-by=, --fields-enclosed-by='"' --lines-terminated-by=0x0d0a db1
$ mysql -h localhost -u root -p
mysql> LOAD DATA INFILE '/tmp/mytable.txt' INTO TABLE mytable;

LOAD DATA INFILE 'E:\\wamp\\tmp\\customer.csv' INTO TABLE customer
CHARACTER SET 'utf8'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

This does not work in windows:
```
mysqldump --defaults-extra-file=D:\sqlbackup\sqlsvr.cnf --tab="D:\sqlbackup\dump_files" db tb --fields-terminated-by=',' --fields-optionally-enclosed-by='"' --fields-escaped-by='\' --lines-terminated-by='\n'
```
Must use hex in windows
mysqldump --defaults-extra-file=D:\sqlbackup\sqlsvr.cnf --tab="D:\sqlbackup\dump_files" db tb --fields-terminated-by=0x2C --fields-optionally-enclosed-by=0x22 --fields-escaped-by=0x5C --lines-terminated-by=0x0a
```

## dump db with each table in a separate file
redirect the query to another database
```sh
#!/bin/bash

fdb=dump_dbs.txt
dir="/media/data/test"
typ="BASE TABLE"

create_list=$(( $#==0 ? 1 : 0 ))
 
timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

i=0 
echo $(timestamp) dump dbs
while read db; do
    ((++i))  
    ftb=$dir/$db"_tbs.txt"
    if [ $create_list -eq 1 ]; then
	qry='SELECT table_name FROM information_schema.tables WHERE table_schema='\'${db}\'' and table_type='\'${typ}\'' order by data_length asc;'
        mysql --defaults-extra-file=$dir/svr_fr.cnf --skip-column-names -e "${qry}" >$ftb
    fi    
    echo $(timestamp) "  " db: $db
    j=0 
    while read tb; do
        ((++j))
        echo $(timestamp) "    "$j table: $tb 
        mysqldump --defaults-extra-file=$dir/svr_fr.cnf $db $tb | mysql --defaults-extra-file=$dir/svr_to.cnf $db
    done <$ftb 
done <$fdb

echo $(timestamp) all done!
```

## dump db with each table in a separate file
```sh
#!/bin/bash

fdb=fdt_dbs.txt
dir="/media/data/test"
op1="--tab=$dir" 
op2=" --default-character-set=latin1 --fields-terminated-by=\t --lines-terminated-by=\r\n"

create_list=$(( $#==0 ? 1 : 0 ))
 
timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

echo $(timestamp) dump dbs
i=0 
while read db; do
    ((++i))  
    ftb=$dir/$db"_tbs.txt"
    if [ $create_list -eq 1 ]; then
        qry='select table_name from information_schema.tables where table_schema='\'${db}\'' order by table_name;'
        mysql --defaults-extra-file=$dir/sqlsvr.cnf --skip-column-names -e "${qry}" > $ftb
    fi    
    echo $(timestamp) "  " db: $db
    j=0 
    while read tb; do
        ((++j))
        echo $(timestamp) "    "$j table: $tb 
        mysqldump --defaults-extra-file=$dir/sqlsvr.cnf $op1 $op2 $db $tb
        mv $tb".sql" $db"_"$tb".sql"
        mv $tb".txt" $db"_"$tb".txt"
    done <$ftb 
done <$fdb

echo $(timestamp) all done!
```

## dump db with each table in a separate file
```dos
@echo off

setlocal EnableDelayedExpansion
 
set fdb=fdt_dbs.txt
set dirwd=%~dp0
set dirwn=C:\ProgramData\MySQL\MySQL Server 8.0\Data\#dump_tmp
set dirto=%dirwn:\=/%
set dirfr=\\sql.server\test
set par=CHARACTER SET latin1 FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\r\n';

rem net use "\\sql.server" pwd /user:workgroup\usr

echo %dirto%/%fdb%
 
echo %date% %time% load dbs
rem copy /z %dirfr%\%fdb% %dirto%\%fdb%
set i=0
for /f "usebackq" %%a in ("%dirto%/%fdb%") do (
    set /a i=!i!+1
    echo !date! !time!  !i! db: %%a
    rem copy /z %dirfr%\%%a_tbs.txt %dirto%\%%a%_tbs.txt
    set j=0
    for /f "usebackq" %%b in ("%dirto%/%%a_tbs.txt") do (
        set /a j=!j!+1
        echo !date! !time!    !j! table: %%b
        rem copy /z %dirfr%\%%a_%%b.sql %dirto%\%%a_%%b.sql
        mysql --defaults-extra-file=%dirwd%svr_to.cnf %%a < "%dirto%/%%a_%%b.sql"
        rem copy /z %dirfr%\%%a_%%b.txt %dirto%\%%a_%%b.txt
        set sql_qry=USE %%a;LOAD DATA INFILE '!dirto!/%%a_%%b.txt' INTO TABLE %%b %par%
        mysql --defaults-extra-file=%dirwd%sql_server.cnf -e "!sql_qry!" --show-warnings
    )    
)

rem net use "\\xx-xx.xx.xx" /delete

echo %date% %time% all done!
```
## disbale key checking
It sounds like your import is slowing down--processing fewer rows per second--as it progresses. That probably means MySQL is checking each new row to see whether it has key-conflicts with the rows already inserted.

A few things you can do:

Before starting, disable key checking:
  SET FOREIGN_KEY_CHECKS = 0;
  SET UNIQUE_CHECKS = 0;
  
After ending restore your key checking:
  SET UNIQUE_CHECKS = 1;
  SET FOREIGN_KEY_CHECKS = 1;

mysqldump can be made to create a dump with that disables keys:\\ 
  mysqldump --disable-keys
Similarly,
  mysqldump --extended-insert --no-autocommit
will make the dumped sql file contain a variant of my suggestion about using transactions.

https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html#option_mysqldump_disable-keys

For each table, surround the INSERT statements with /*!40000 ALTER TABLE tbl_name DISABLE KEYS */; and /*!40000 ALTER TABLE tbl_name ENABLE KEYS */; statements. This makes loading the dump file faster because the indexes are created after all rows are inserted. This option is effective only for nonunique indexes of **MyISAM** tables. By default, the key checking is disabled.


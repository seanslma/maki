# IO

## load/save from/to file/table
```sql
#load file to table
LOAD DATA INFILE 'data.csv' INTO TABLE my_db.my_table;

#save table to file
SELECT a,b,a+b 
INTO OUTFILE '/tmp/result.csv'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
FROM test_table;
```

the file path:\\
/var/lib/mysql/<databasename>\\
.\bin\mysql\mysql5.6.17\data\db\file.csv

## csv to table
  mysql –u username –p --local-infile somedatabase
  
```sql
USE database_name;
LOAD DATA LOCAL INFILE '/home/export_file.csv'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;
```
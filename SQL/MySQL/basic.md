# Basic

## Delete table data
```sql
TRUNCATE TABLE my_table_name;
```

## create db
```sql
CREATE SCHEMA IF NOT EXISTS `dbname`;
CREATE TABLE tbl_new LIKE tbl_old;
```

## copy table
```sql
--copy structure and data
create table tbl_new as select * from tbl_old;
--copy structure with indexes and triggers
create table tbl_new LIKE tbl_old; 
insert into tbl_new select * from tbl_old;
```

## show dbs/tabls
```sql
SHOW SCHEMAS;
SHOW DATABASES;

SELECT table_name as tbl,
FROM information_schema.TABLES
WHERE table_schema = 'db_name'
ORDER BY table_name;
```

```sql
--delete all from table
delete from db.tbl;

--insert into another table
insert ignore into db.t2
SELECT * 
FROM db.t1
where datecol between '2017-06-30 00:00:00' and '2018-07-02 00:00:00';
```

## Emulate ROW_NUMBER
```sql
--add a row number for each row, reset it to 1 when customer number changes
SELECT 
    @row_number:=CASE
        WHEN @customer_no = customerNumber THEN @row_number + 1
        ELSE 1
    END AS num,
    @customer_no:=customerNumber as CustomerNumber,
    paymentDate,
    amount
FROM
    payments,(SELECT @customer_no:=0,@row_number:=0) as t
ORDER BY customerNumber;
```

## insert ignore vs replace

insert ignore - if key/row exists or error, skip insertion

replace - if key/row exists, delete the match row, and insert again; ON DELETE CASCADE will cause significant issues

```sql
INSERT INTO t1 (a,b,c) 
VALUES (1,2,3),(4,5,6)
  ON DUPLICATE KEY 
UPDATE c=VALUES(a)+VALUES(b);
```

## group_concat fields

```sql
--default limit is 1024 characters
SET group_concat_max_len=100000000
--syntax
GROUP_CONCAT([DISTINCT] expr [,expr ...]
             [ORDER BY {unsigned_integer | col_name | expr}
                 [ASC | DESC] [,col_name ...]]
             [SEPARATOR str_val])
--example             
SELECT student_name,
     GROUP_CONCAT(DISTINCT test_score 
                  ORDER BY test_score DESC SEPARATOR ';')
FROM student
GROUP BY student_name;             
```

## Select row with max value for one field and group by another field

```sql
--good solution
SELECT t.nam, t.val, t.cnt
FROM tbl as t
INNER JOIN 
( SELECT nam, MAX(cnt) AS max_cnt
  FROM tbl
  GROUP BY nam 
) AS m
ON t.nam = m.nam AND t.cnt = m.max_cnt;
```



# alter table

directly using the alter command is very slow.

```mysql
-- only for MYISAM
create table tbl_tmp like tbl;
alter table tbl_tmp add column colx int not null;
alter table tbl_tmp disable keys;
insert into tble_tmp select *,0 from tbl;
alter table tbl_tmp enable keys;
rename table tbl to tbl_old, tbl_tmp to tbl;
```

## ALTER TABLE Method
```sql
Alter TABLE my_table_name 
Add fd1 float NULL, 
add fd2 float NULL;

ALTER TABLE my_table_name 
MODIFY fld INTEGER [not null];

ALTER TABLE my_table_name 
MODIFY COLUMN name VARCHAR(255);

ALTER TABLE my_table_name
ADD INDEX `fld_name` (`fld_name`)

alter table my_table_name 
drop primary key, add primary key(k1, k2, k3);
```
# query

## checksum
  CHECKSUM TABLE db.tbl;

## par
```sql
SELECT variable_value FROM information_schema.global_variables 
WHERE variable_name IN ('slow_query_log','slow_query_log_file','long_query_time');
```

## move records
wrap the insert and delete into one transaction to avoid data loss
```sql
DECLARE EXIT HANDLER FOR SQLEXCEPTION, SQLWARNING, NOT FOUND
BEGIN 
  ROLLBACK; 
  CALL ERROR_ROLLBACK_OCCURRED; 
END;

START TRANSACTION;
INSERT INTO table_new SELECT a,b,c FROM table_old WHERE x = 'something';
DELETE FROM table_old WHERE x = 'something';
COMMIT;
```

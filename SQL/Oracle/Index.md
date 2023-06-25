# Index

## hints of key for optimizer
```sql
SELECT /*+ index(t my_tbl_pk)*/ DATETIME, QUALITY 
FROM schema.tbl t  
WHERE datetime > to_date('01-Oct-2021 00:00', 'DD-MON-YYYY HH24:MI')
ORDER BY 1;
```

# DateTime

## define
```sql
define dt="TO_DATE ('2022-09-01', 'yyyy-mm-dd') + 1";
SELECT &dt + 3 new_date
FROM DUAL;
```

## add 5 minutes
```sql
select dt + INTERVAL '5' MINUTE as dt
from my_table;
```

## string to datetime
```sql
SELECT TO_DATE('2024-01-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS') AS datetime_value from dual
```

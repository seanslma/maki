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

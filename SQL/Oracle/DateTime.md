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

## add intervals
To substract a datetime duration from date in oracle sql query, we can use
- `- 1/24`: only for date
- `- interval '1' hour`: for date and timestamp, also works in duckdb
- commonly used intervals: day, hour, minute, second

## string to datetime
```sql
SELECT TO_DATE('2024-01-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS') AS datetime_value from dual
```

## make oracle sql query work in duckdb
```py
query = (
    query
    .replace('to_date(', 'strptime(')  # to_date(:start_date, 'yyyy-mm-dd')
    .replace('yyyy-mm-dd', '%Y-%m-%d') # strptime(:start_date, '%Y-%m-%d')
    .replace(':', '$') # binding sign, can be questionable for %H:%M:%S
)
```

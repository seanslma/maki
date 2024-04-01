# Rank

## select max and second max
do not use distinct - it's super slow.

Note that this is not correct if we have multiple records with max datetime
```sql
SELECT datetime_column
FROM (
    SELECT datetime_column,
           ROW_NUMBER() OVER (ORDER BY datetime_column DESC) AS rn
    FROM your_table
) ranked
WHERE rn <= 2;
```

Use `dense_rank()`
```sql
SELECT distinct datetime_column
FROM (
    SELECT datetime_column,
           DENSE_RANK() OVER (ORDER BY datetime_column DESC) AS rn
    FROM your_table
) ranked
WHERE rn <= 2;
```

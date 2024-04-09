# Rank

## select max and second max
do not use distinct - it's super slow
```sql
SELECT datetime_column
FROM (
    SELECT datetime_column,
           ROW_NUMBER() OVER (ORDER BY datetime_column DESC) AS rn
    FROM your_table
) ranked
WHERE rn <= 2;
```

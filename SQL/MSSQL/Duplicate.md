# Duplicate

## duplicate records
```sql
select
    product_name,
    start_date,
    end_date,
    STRING_AGG(p_type, ', ') AS typ,
    STRING_AGG(CAST(p_price AS VARCHAR(10)), ', ') AS price,
    count(*) as cnt
from my_tbl
where p_price > 10
group by product_name, start_date, end_date
having count(*) > 1;
```

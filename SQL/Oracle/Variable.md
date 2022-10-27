# Variable

## define and use variable
```sql
define col = 'date';
define day = to_date('2022-07-01', 'YYYY-MM-DD');
SELECT '&&col' from my_table where date > &&day;
```

```sql
define val = 12;
SELECT * from my_table where value > &&val;
```

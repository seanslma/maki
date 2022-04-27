# Variable

## define and use variable
```sql
define col = 'date';
SELECT '&&col' from my_table;
```

```sql
define val = 12;
SELECT * from my_table where value > &&val;
```

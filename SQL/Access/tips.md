# tips

## add row_number
```sql
select t.*, 
      (select count(*) from t 
       where a.sort_field>=sort_field
      ) as rid 
from t as a order by a.sort_field;
```

## max of columns
```sql
select max(v) as maxv
from ( 
  (select v1 as v from t)
  union
  (select v2 as v from t)
  union
  (select v3 as v from t)
) as a
```
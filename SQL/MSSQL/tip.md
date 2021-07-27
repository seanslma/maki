# tip

## max of columns
```sql
select f1, max(d) vmax, f3
from t unpivot (d for v in (v1,v2,v3)) as u
group by f1, f3 
go

SELECT [Other Fields],
  (SELECT Max(v) FROM (VALUES (date1), (date2), (date3),...) AS value(v)) as [MaxDate]
FROM [YourTableName]
```
# Function

## find functions with specific string
```sql
SELECT * 
FROM ALL_OBJECTS 
WHERE OBJECT_TYPE IN ('FUNCTION','PROCEDURE','PACKAGE') and lower(object_name) like '%data%';
```

## show function definition
```sql
select text 
from all_source 
where type = 'FUNCTION' and name = 'my_func_name'
order by line;
```

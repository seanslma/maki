# Admin

## check sessions
```sql
select username, osuser, min(logon_time) as min_time, max(logon_time) as max_time, status, module, count(*) as sessions
from v$session 
where status = 'active'
group by username, osuser, status, module;
```

## find table with specific column
```sql
select owner as schema, table_name, column_name 
from all_tab_columns 
where lower(column_name) like '%juri%';
```

## find views with specific string
```sql
SELECT view_name, text
FROM all_views
where lower(view_name) like '%data%';
```

## find functions with specific string
```sql
SELECT * 
FROM ALL_OBJECTS 
WHERE OBJECT_TYPE IN ('FUNCTION','PROCEDURE','PACKAGE') and object_name like '%data%';
```

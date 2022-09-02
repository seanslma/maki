# Admin

## check sessions
```
select username, osuser, min(logon_time) as min_time, max(logon_time) as max_time, status, module, count(*) as sessions
from v$session 
where status = 'active'
group by username, osuser, status, module;
```

## find table with specific column
```
select owner as schema, table_name, column_name 
from all_tab_columns 
where lower(column_name) like '%juri%';
```

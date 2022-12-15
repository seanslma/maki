# Admin

## check sessions
```sql
select username, osuser, min(logon_time) as min_time, max(logon_time) as max_time, status, module, count(*) as sessions
from v$session 
where status = 'active'
group by username, osuser, status, module;
```

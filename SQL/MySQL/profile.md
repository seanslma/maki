# Profiling

## settings
```sql
SHOW PROCESSLIST;
show variables like 'innodb%'
SHOW TABLE STATUS FROM `db` LIKE 'tbl';
```

## profiling
https://dev.mysql.com/doc/refman/8.0/en/general-thread-states.html

```
mysql> SET PROFILING=1;
mysql> SHOW TABLES;
mysql> SELECT * FROM foo;
mysql> SET PROFILING=0;   --deprecated from 5.6.7
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW PROFILES;
+----------+------------+-------------------+
| Query_ID | Duration   | Query             |
+----------+------------+-------------------+
|        1 | 0.09270400 | SHOW TABLES       |
|        2 | 0.00026400 | SELECT * FROM foo |
+----------+------------+-------------------+
2 rows in set (0.05 sec)

mysql> SHOW PROFILE FOR QUERY 2;
+----------------------+----------+
| Status               | Duration |
+----------------------+----------+
| starting             | 0.000053 |
| checking permissions | 0.000009 |
| Opening tables       | 0.000032 |
| System lock          | 0.000010 |
| init                 | 0.000028 |
| optimizing           | 0.000003 |
| statistics           | 0.000012 |
| preparing            | 0.000008 |
| executing            | 0.000003 |
| Sending data         | 0.000068 |
| end                  | 0.000004 |
| query end            | 0.000007 |
| closing tables       | 0.000008 |
| freeing items        | 0.000013 |
| logging slow query   | 0.000003 |
| cleaning up          | 0.000003 |
+----------------------+----------+
16 rows in set (0.04 sec)
```

## new method
```sql
#change statement settings (default YES)
UPDATE performance_schema.setup_instruments
SET ENABLED = 'YES', TIMED = 'YES'
WHERE NAME LIKE '%statement/%';

#change stage settings (default NO for properties != 'progress')
UPDATE performance_schema.setup_instruments
SET ENABLED = 'YES', TIMED = 'YES'
WHERE NAME LIKE '%stage/%';

#change consumers settings
UPDATE performance_schema.setup_consumers
SET ENABLED = 'YES'
WHERE NAME LIKE '%events_statements_%';

UPDATE performance_schema.setup_consumers
SET ENABLED = 'YES'
WHERE NAME LIKE '%events_stages_%';

#disable other threads for instrument
UPDATE performance_schema.threads
SET INSTRUMENTED = 'NO'
WHERE TYPE='FOREGROUND' AND PROCESSLIST_USER NOT LIKE 'user_john';

#1. RUN QUERY
select * from mytable where col like '124%';

#2. identify EVENT_ID 
SELECT @eid:=EVENT_ID, TRUNCATE(TIMER_WAIT/1000000000000,6) as Duration, SQL_TEXT
FROM performance_schema.events_statements_history_long WHERE SQL_TEXT like '%10001%'
order by EVENT_ID desc limit 1;

#3. retrieve stage events
SELECT event_name AS Stage, TRUNCATE(TIMER_WAIT/1000000000000,6) AS Duration
FROM performance_schema.events_stages_history_long WHERE NESTING_EVENT_ID=@eid;

#change settings back to default
update performance_schema.setup_instruments
SET ENABLED = 'NO', TIMED = 'NO'
WHERE NAME LIKE '%stage/%' and properties != 'progress';  

update performance_schema.setup_consumers
set enabled = 'NO'
WHERE NAME = 'events_statements_history_long';

update performance_schema.setup_consumers
set enabled = 'NO'
WHERE NAME LIKE '%events_stages_%';
```

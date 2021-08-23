# percona-toolkit

## pt-online-schema-change with partitions

Will create triggers to synchronize the changes between old and new tables. It might be slow but the downtime is minimized.

https://www.percona.com/blog/2015/09/09/testing-mysql-partitioning-pt-online-schema-change/

```sql
#direct command
ALTER TABLE test.tbl PARTITION BY HASH(id) partitions 4;

#pt-online
pt-online-schema-change h=localhost, D=test, t=tbl --recursion-method none --execute 
--alter "PARTITION BY HASH(id) partitions 4"
```

For testing, if we want to 1) keep the original table; 2) do not swap the tables; 3) do not drop the triggers, we should use
```sql
pt-online-schema-change h=localhost, D=test, t=tbl --recursion-method none --execute 
--no-swap-tables --no-drop-old-table --no-drop-new-table --no-drop-triggers  
--alter "PARTITION BY HASH(id) partitions 4"
```

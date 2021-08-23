# InnoDB

DROP a huge InnoDB table, there will be some unavoidable some downtime for the server.

https://dev.to/jung/why-you-simply-don-t-drop-a-huge-innodb-table-in-production-18j2

This is better:
```sql
DELETE FROM tbl;
OPTIMIZE TABLE tbl;
DROP TABLE tbl;
```

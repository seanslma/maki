# Date time

https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms180878(v=sql.105)?redirectedfrom=MSDN

New version:

https://docs.microsoft.com/en-us/sql/relational-databases/native-client-odbc-date-time/data-type-support-for-odbc-date-and-time-improvements?view=sql-server-ver16

## ISO 8601 Format (not good for new version)
Date:
- `YYYYMMDD`

Datetime:
- `YYYY-MM-DDThh:mm:ss[.nnnnnnn][{+|-}hh:mm]`
- `YYYY-MM-DDThh:mm:ss[.nnnnnnn]Z` (UTC, Coordinated Universal Time)

## DateTime2 in new version
```
Datetime2	SQL_TYPE_TIMESTAMP 'yyyy-mm-dd hh:mm:ss[.9999999]'
```

## convert string to date
option 1: `cast`. Can't set the format
```sql
SELECT CAST('01' + 'Sep25' AS DATE) as dd_mon_yy; -- 2025-09-01
SELECT CAST('01' + 'Jan50' AS DATE) as dd_mon_yy; -- 1950-01-01 two digit year cutoff is 2049
```

option 2: `convert`
https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-ver16
```sql
SELECT CONVERT(DATE, '01' + 'Sep25', 6) AS dd_mon_yy;
SELECT CONVERT(DATE, '01' + 'Jan50', 6) as dd_mon_yy; -- 1950-01-01 two digit year cutoff is 2049
```

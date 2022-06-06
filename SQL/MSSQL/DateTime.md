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

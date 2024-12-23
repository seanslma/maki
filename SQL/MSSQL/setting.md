# setting

## memory
By default, SQL Server’s max memory is 2147483647 – a heck of a lot more than you actually have.  Trivia time – that’s the max number for a signed 32-bit integer.  SQL Server will just keep using more and more memory until there’s none left on the system.

Our simple “starter” rule of thumb is to leave 4GB or 10% of total memory free, whichever is LARGER on your instance to start with, and adjust this as needed.
```
Server -> Properties -> Memory -> Max server memory
T-SQL: EXEC sys.sp_configure 'max server memory (MB)', '2048'; RECONFIGURE;
```
  
## logging
You can't do without transaction logs in SQL Server, under any circumstances. The engine simply won't function.

You CAN set your recovery model to SIMPLE [other than FULL] on your dev machines - that will prevent transaction log bloating when tran log backups aren't done.

There is a third recovery mode not mentioned above. In cases where you are going to be doing any type of bulk inserts, you should set the DB to be in "BULK/LOGGED". This makes bulk inserts move speedily along and can be changed on the fly [**A new database inherits its recovery model from the model database**].
```sql
USE master;
ALTER DATABASE model SET RECOVERY BULK_LOGGED; --change
ALTER DATABASE model SET RECOVERY SIMPLE; --change it back
```

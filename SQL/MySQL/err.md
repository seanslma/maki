# error

## the host does not support ssl connections
add 'SslMode=none'

## table is marked as crashed and should be repaired
https://www.a2hosting.com/kb/developer-corner/mysql/repairing-mysql-databases-and-tables

This error can appear at any time, especially after a forced shutdown of MySQL database or due to the crash of the entire server.

repair the table
  mysqlcheck -u usr -ppsw -r db tb

**Recovering MySQL Crashed Tables**:
  # myisamchk -s /var/lib/mysql/*/*.MYI
Running this command will list the crashed MySQL tables, with a message as follows:
  MyISAM-table '/var/lib/mysql/dbname/table_name.MYI' is marked as crashed and should be repaired

## Unable to connect to any of the specified MySQL hosts
https://www.codeproject.com/Questions/728680/Unable-to-connect-to-any-of-the-specified-MySQL-2

change server to localhost OK!

The error you are getting indicates it can't resolve the host name which is a dns issue. Whatever the server name in your connection string is, the name cannot be resolved.

If the database is on the same machine as the web server you can use **localhost** for the server name.

if its on a different machine you can try to ping it by name and it will probably give you the same error if it can't resolve the name. If you know the ip address of the machine with MySQL, you can edit your **hosts file** and add a row like

192.168.0.x hostname

On windows your hosts file should be in Windows\System32\Drivers\etc folder

## wrong query results
select * from db.tbl
where datecol = '2020-04-30 07:05:00' and namecol = 'John';

Repair the index fixed the issue
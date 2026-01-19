# MySQL

To install MySQLdb on Windows go to this link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient \\
Download the appropriate .whl for your Python version: python -m pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl
```sh
python -m pip install sqlalchemy-access
```

## module 'time' has no attribute 'clock'
update sqlalchemy to the latest version as time.clock is removed from python 3.8 and later versions

## Connect to mdb
```py
# connect to db
try:
    drv = '{Microsoft Access Driver (*.mdb)}'
    con = pyodbc.connect(f'DRIVER={drv};DBQ=' + dbpath)
except pyodbc.InterfaceError:
    drv = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    con = pyodbc.connect('DRIVER={drv};DBQ=' + dbpath)
cursor = con.cursor()

# query
cursor.execute("Select * from tbl")
rows = cursor.fetchall()

# close connection
cursor.close()
con.close()
```

## MySQL query to csv
```py
import pandas as pd
import MySQLdb as db

con = db.connect(host=svr,port=prt,user=usr,passwd=pwd,db=dbn,connect_timeout=30) #sec
qry = f'''select c1, c2
          from simulation
          where c1 = '{a}' and c2 = {b};'''
df = pd.read_sql(qry, con=con)
df.to_csv('file.csv', mode='w', index=False, header=True)
```

## performance
Executemany is often not much faster than performing individual inserts in a loop. This is true not only for pyodbc but for other Python ODBC layers as well.

A commonly-suggested workaround is to use a bulk copy utility such as the bcp utility for Microsoft SQL Server, but Microsoft Access does not have such a stand-alone utility. The MS Access equivalent is to use VBA code to import data from text files via VBA's DoCmd.TransferText method.

If you really need to accomplish your task via ODBC from within Python, then one alternative that might offer a modest performance gain would be to

create a temporary table with no indexes, possibly in a separate database file,
insert the data into the temporary table while autocommit=False with a .commit() at the end, and then
INSERT INTO real_table (...) SELECT ... FROM temp_table

## MS SQL Connection Error
[answer](https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox)

Two thoughts on what to check:

1) Your connection string is wrong. There's a way to get a known good connection string directly from the ODBC Administrator program (taken from http://www.visokio.com/kb/db/dsn-less-odbc). These instructions assume you're using an MDB, but the same process will work for a paradox file

On a typical client PC, open Control Panel -> Administrative Tools -> Data Sources.
Select the File DSN tab and click Add.

Select the appropriate driver (e.g. "Microsoft Access Driver (*.mdb)") and click Next
Click Browse and choose where you want to save the .dsn file (this is a temporary file you are going to delete later).
Click Next then Finish.

You will be shown the vendor-specific ODBC setup dialog. For example, with Microsoft Access, you might only need to click Select and browse to an existing .mdb file before clicking OK.
Browse to the location of the .dsn file and open using Notepad.
In the DSN file you might see something similar to:
```
[ODBC]
DRIVER=Microsoft Access Driver (*.mdb)
UID=admin
UserCommitSync=Yes
Threads=3
SafeTransactions=0
PageTimeout=5
MaxScanRows=8
MaxBufferSize=2048
FIL=MS Access
DriverId=25
DefaultDir=C:\
DBQ=C:\db1.mdb
To convert the above to the full connection strring:
```
Omit the first [ODBC] line
Put curly braces around all values containing spaces
Put all name=value pairs on one line, separated by semicolons.
This gives you the full connection string. In this example, the string becomes:

DRIVER={Microsoft Access Driver (*.mdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;axScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DefaultDir=C:\;DBQ=C:\db1.mdb

2) 32/64 bit mismatch. I've had troubles when mixing 32-bit python with 64-bit drivers, or vice-versa. You may want to check your Python interpreter and database driver line up.

## simple obfuscation
can save password and other server info in a file in the user's temporal folder. the first time ask the user to input the info and later just read the info from the file. Or do some simple obfuscation.

```py
#get password
getpass.getpass()

#encode
def enco(k, s):
    s = ''.join([chr((ord(s[i]) + ord(k[i % len(k)])) % 256) for i in range(len(s))])
    return base64.urlsafe_b64encode(s.encode()).decode()
#decode
def deco(k, s):
    s = base64.urlsafe_b64decode(s).decode()
    return ''.join([chr((ord(s[i]) - ord(k[i % len(k)]) + 256) % 256) for i in range(len(s))])
```

# Error

## pyodbc fast_executemany data type varchar to numeric error
Error converting data type varchar to numeric 8114 when Inserting into SQL Server using select from values using fast_executemany

https://github.com/mkleehammer/pyodbc/issues/976

fast_executemany needs to determine the types of all the parameters in advance so it can allocate the parameter data array. 
As your trace shows, pyODBC has trouble determining those types because they're ambiguous, and the errors follow. 
The best solution (which also avoids sending needless data to the server) is to not do that.

https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5

Solution: According to the Github issue from the pyodbc repository [2], pyodbc internally passes all decimal values as strings because of some discrepancies and bugs related to decimal points used by various database drivers. 

This means that when my data has a value of 0.021527 or 0.02, both of those values may not be accepted because my SQL Server data type was specified as NUMERIC(18,3).

`df['val'] = [format(v, '.3f') for v in df['val']]`

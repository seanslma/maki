# Error

## pyodbc fast_executemany data type varchar to numeric error
Error converting data type varchar to numeric 8114 when Inserting into SQL Server using select from values using fast_executemany

https://github.com/mkleehammer/pyodbc/issues/976

fast_executemany needs to determine the types of all the parameters in advance so it can allocate the parameter data array. 
As your trace shows, pyODBC has trouble determining those types because they're ambiguous, and the errors follow. 
The best solution (which also avoids sending needless data to the server) is to not do that.

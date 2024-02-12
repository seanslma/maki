# Issue

## Error code 0x68 (104) (SQLEndTran)
`pyodbc.OperationalError: ('08S01', '[08S01] [Microsoft][ODBC Driver 17 for SQL Server]TCP Provider: Error code 0x68 (104) (SQLEndTran)')`
- https://www.linuxquestions.org/questions/programming-9/persistent-db-connection-after-waking-up-a-computer-from-sleep-4175615332
- https://techcommunity.microsoft.com/t5/azure-database-support-blog/lesson-learned-359-tcp-provider-error-code-0x68-104/ba-p/3834127

Solution: 
https://docs.sqlalchemy.org/en/20/dialects/mssql.html#pyodbc-pooling-connection-close-behavior

PyODBC uses internal pooling by default, which means connections will be longer lived than they are within SQLAlchemy itself. 
As SQLAlchemy has its own pooling behavior, it is often preferable to disable this behavior. 
This behavior can only be disabled globally at the PyODBC module level, before any connections are made:
```py
import pyodbc
pyodbc.pooling = False
# don't use the engine before pooling is set to False
engine = create_engine("mssql+pyodbc://user:pass@dsn")
```

# Security

## encrypt connection string
database connection string contains username and password so it should be encrypted.


Encrypt mssql connection string using ODBC Driver's Encryption:
- https://learn.microsoft.com/en-us/sql/connect/odbc/using-always-encrypted-with-the-odbc-driver?view=sql-server-ver16
- https://stackoverflow.com/questions/62390326/pyodbc-ms-sql-server-connection-with-encrypt-yes-not-connecting
```py
import sqlalchemy as sa

conn_str = (
    r'mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server;Encrypt=yes'
)
engine = sa.create_engine(conn_str)

```

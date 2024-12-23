# TSL

## tls 1.2 support
https://learn.microsoft.com/en-gb/troubleshoot/sql/database-engine/connect/tls-1-2-support-microsoft-sql-server

## python connection: ubuntu 22.04 and old sql server
openssl 3.0: 
https://github.com/microsoft/msphpsql/issues/1112

issue:
```
sqlalchemy.exc.OperationalError: (pyodbc.OperationalError) (
'HYT00', '[HYT00] [Microsoft][ODBC Driver 17 for SQL Server]Login timeout expired (0) (SQLDriverConnect)'
)
```

config:
- SQL Server: 12.0.4100.1
- ODBC Driver 17 (18)

Solutions:
- option 1: upgrade server to latest version
- option 2: modify `/etc/ssl/openssl.cnf`
  ```
  [system_default_sect]
  MinProtocol = TLSv1.2
  # CipherString = DEFAULT@SECLEVEL=1
  CipherString = DEFAULT:@SECLEVEL=0
  ```
  Change last `CipherString` line from `CipherString = DEFAULT:@SECLEVEL=2` to `CipherString = DEFAULT:@SECLEVEL=0`

  dockerfile
  ```dockerfile
  USER root
  
  # workaround for ubuntu 22.04 and ms odbc driver 17 with sql server 12.0
  # https://github.com/microsoft/msphpsql/issues/1112
  RUN head -n -1 /etc/ssl/openssl.cnf > openssl_temp_file && \
      echo "CipherString = DEFAULT:@SECLEVEL=0" >> openssl_temp_file && \
      mv openssl_temp_file /etc/ssl/openssl.cnf
  
  USER user
  ```

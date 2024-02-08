# MSSQL

## Configure SQL Server to use encrypted connection
SQL Server Configuration Manager
- SQL Server Network configuration
- Protocols for `<your-sql-server>`
- Force Encryption: Yes
- And choose the certificate

## Check encryption is enabled or not
- On server machine use SQL Server Configuration Manager
- On server machine use PowerShell:
  `Get-Item -Path HKLM:\SOFTWARE\Microsoft\MSSQL\Server\Current Version\Security`
- Check in SQL Server Management Studio (SSMS):
  ServerName -> Properties -> Security -> Force Encryption
- Transact-SQL (T-SQL) Query
  ```sql
  SELECT session_id, encrypt_option
  FROM sys.dm_exec_connections;
  -- or
  SELECT encryption_level, cryptographic_provider, algorithm_name
  FROM sys.dm_cryptographic_providers;
  ```

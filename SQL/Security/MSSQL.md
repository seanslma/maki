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
  SELECT *
  FROM sys.dm_exec_connections;
  -- or
  SELECT session_id, encrypt_option
  FROM sys.dm_exec_connections;
  -- or (not work)
  SELECT encryption_level, cryptographic_provider, algorithm_name
  FROM sys.dm_cryptographic_providers;
  -- get more info
  SELECT s.host_name, s.program_name, s.login_name, s.session_id, s.total_elapsed_time, c.encrypt_option
  FROM sys.dm_exec_sessions as s 
  join sys.dm_exec_connections as c
  on c.session_id = s.session_id
  order by s.host_name;
  ```

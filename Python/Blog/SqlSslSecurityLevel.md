# Login Timeout From Ubuntu 22.04 To SQL Server Database

Recently I upgraded Ubuntu from 18.04 to 22.04 and Python from 3.9 to 3.12. Suddenly my connection to an SQL Server failed with `login timeout expired`.

After some debugging and testing I fixed the issue. It's good to share here what I did and the solution. Hopefully, it will be helpful to you as well.

## The Error Message
When trying to connect to an SQL server database created a few years ago, I received the error:
```
sqlalchemy.exc.OperationalError: (pyodbc.OperationalError) (
'HYT00', '[HYT00] [Microsoft][ODBC Driver 17 for SQL Server]Login timeout expired (0) (SQLDriverConnect)'
)
```
The error is actually caused by not using workload identity, and pod-iid-identity was not setup!

## Checking The Issue
Initially, I thought it was due to the OpenSSL version as Python 3.12 by default uses OpenSSL 3.0. However, we have another SQL server database that still works fine after the upgrading. This led me to check the SQL Server version and just found out that the old version `12.0.2000.8` does not support SSL/TLS 3.0. Based on the error message and the SQL Server version, I quickly worked out the solution with some google searches.

## The Solution
There are two solutions or workarounds.

### Option 1: Upgrading SQL Server Version
Obviously the first option is upgrading the SQL Server version, as we already know that a newer version of SQL Server still works. However, if you are not the person with the permission to do the upgrading or you have other important things in your list, this option might not be good.

### Option 2: Downgrading SSL/TLS Security Level
Ubuntu 22.04 typically uses OpenSSL 3.x, so the `CipherString` for SSL/TLS connections in Ubuntu 22.04 defaults to a security level of 2. As the old version SQL Server does not support a security level of 2, we can downgrade the security level as a temporal workaround (**note** that doing this may compromise the security).

Now for the workaround, in the openssl config file `/etc/ssl/openssl.cnf`, we only need to change the last `CipherString` line from `CipherString = DEFAULT:@SECLEVEL=2` to `CipherString = DEFAULT:@SECLEVEL=0`.

If working with docker images, you can add the following to your Dockerfile:
```dockerfile
USER root

# workaround for ubuntu 22.04 and odbc driver 17 with sql server 12.0
RUN head -n -1 /etc/ssl/openssl.cnf > openssl_cnf_temp_file && \
    echo "CipherString = DEFAULT:@SECLEVEL=0" >> openssl_cnf_temp_file && \
    mv openssl_cnf_temp_file /etc/ssl/openssl.cnf

USER <your-user-name>
```

## References
- https://github.com/microsoft/msphpsql/issues/1112

# Config

## set tnsnames.ora and sqlnet.ora
These two files must be set for connection to the oracle database for Oracle Client.

## TNS_ADMIN
This env var is used to point the folder for tnsnames.ora file. check it in cmd: `echo %TNS_ADMIN%`

If the `TNS_ADMIN` is not set, the Oracle `instantclient` path should be included in the `PATH` and the tnsnames folder should be mounted to `/network/admin/` under the `PATH`.

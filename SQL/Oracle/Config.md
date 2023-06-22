# Config

## TNS_ADMIN
This env var is used to point the folder for tnsnames.ora file. check it in cmd: `echo %TNS_ADMIN%`

If the `TNS_ADMIN` is not set, the Oracle path should be included in the `PATH`.

## set tnsnames.ora and sqlnet.ora
These two files must be set for connection to the oracle database

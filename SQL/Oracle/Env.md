# Env

## Naming Parameters
By default, the `tnsnames.ora` file is located in the `ORACLE_HOME/network/admi`n directory. 
Oracle Net will check the other directories for the configuration file. For example, the order checking the tnsnames.ora file is as follows:
  - The directory specified by the `TNS_ADMIN` environment variable. If the file is not found in the directory specified, then it is assumed that the file does not exist.
  - If the TNS_ADMIN environment variable is not set, then Oracle Net checks the `ORACLE_HOME/network/admin` directory.

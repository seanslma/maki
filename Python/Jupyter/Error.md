# Error

## No module named 'pysqlite2'
This is because the `sqlite3.dll` could not be found that triggered the error.

Solution: download the dll from `https://www.sqlite.org/download.html` and put it in the right folder.
```
Traceback (most recent call last):
  File "\lib\site-packages\jupyter_server\services\sessions\sessionmanager.py", line 14, in <module>
    import sqlite3
  File "\lib\sqlite3\__init__.py", line 57, in <module>
    from sqlite3.dbapi2 import *
  File "\lib\sqlite3\dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ImportError: DLL load failed while importing _sqlite3: The specified module could not be found.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
...
  File "\lib\site-packages\jupyter_server\services\sessions\sessionmanager.py", line 17, in <module>
    from pysqlite2 import dbapi2 as sqlite3  # type:ignore[no-redef]
ModuleNotFoundError: No module named 'pysqlite2'
```

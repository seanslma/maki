# basic

## find the mpl_tools directory
```py
import importlib
importlib.import_module('mpl_toolkits').__path__

#check version
python -m pip freeze | findstr matplotlib

#check type
isinstance(i, int)
isinstance(s, str)

#install module
python -m pip install numpy
```

## pyinstaller
It is possible to compile python scripts to an executable using the pyinstaller module. Helps with version control and not having to rely on module dependencies.

Pyinstaller won't install nested dependencies that it can't see and it isn't obvious that it hasn't worked until runtime. You can work through package at a time and either add them to the hidden_imports list in the spec_file or in the command line or in hook files. All doable, just a little iterative.

## Install MySQLdb on Windows for Python 3
To install MySQLdb on Windows go to this link \\
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient\\
Download the appropriate .whl for your Python version.
```sh
python -m pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl
```

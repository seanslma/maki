# Package

## create package
https://packaging.python.org/en/latest/

### setup.py
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

`setup.py` serves two primary functions:
- It’s the file where various aspects of your project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section below.
- It’s the command line interface for running various commands that relate to packaging tasks. To get a listing of available commands, run python setup.py --help-commands.

Create this `setup.py` before run `versioneer install`
```py
from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
```

### setup.cfg
`setup.cfg` is an ini file that contains option defaults for setup.py commands.

Use `git` versioneer:\
https://github.com/python-versioneer/python-versioneer/blob/master/INSTALL.md

### README.md
All projects should contain a readme file that covers the goal of the project.

### MANIFEST.in
A `MANIFEST.in` is needed when you need to package additional files that are not automatically included in a source distribution.

### LICENSE.txt
Every package should include a license file detailing the terms of distribution.

## attempted relative import with no known parent package
```py
from ..utils import check_date
```
The previous line will crash with the error if run the code from a subfolder and import the methods from the parent folder. In this case, function call must be from the parent folder.

## nested package
When install a package into a subdirectory of another package as an editable package via pip, we need to use `pkgutil`.
- https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil
- in `__init__.py`: `__path__ = __import__('pkgutil').extend_path(__path__, __name__)`

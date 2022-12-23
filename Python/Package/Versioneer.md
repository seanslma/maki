# Versioneer
https://stackoverflow.com/questions/53724616/update-version-number-with-versioneer-and-github

`versioneer` will get the version number from git tag + state of the repository.

https://jacobtomlinson.dev/posts/2020/versioning-and-formatting-your-python-code/

## step 1: create `setup.py`
```py
from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
```
All other info can be put into the `setup.cfg` file.

## step 2: create `setup.cfg`
Still not support pyproject.toml
```
[versioneer]
VCS = git
style = pep440
versionfile_source = pkg/_version.py
versionfile_build = pkg/_version.py
tag_prefix =
parentdir_prefix = pkg-
```

## step 3: create `pkg/__init__.py`
run `versioneer install`

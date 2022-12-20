# Versioneer
https://jacobtomlinson.dev/posts/2020/versioning-and-formatting-your-python-code/

## setup.py
```py
from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
}    
```
All other info can be put int the `setup.cfg` file.

## setup.cfg
`versioneer install`
```
[versioneer]
VCS = git
style = pep440
versionfile_source = pkg/_version.py
versionfile_build = pkg/_version.py
tag_prefix =
parentdir_prefix =
```

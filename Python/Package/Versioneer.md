# Versioneer
https://stackoverflow.com/questions/53724616/update-version-number-with-versioneer-and-github

`versioneer` will get the version number from git tag + state of the repository.

https://jacobtomlinson.dev/posts/2020/versioning-and-formatting-your-python-code/

## versioneer vs setuptools-smc
- https://setuptools-git-versioning.readthedocs.io/en/stable/comparison.html
- https://rse.shef.ac.uk/blog/2023-09-18-python-packaging/#:~:text=Setuptools%2Dscm,on%20now%20deprecated%20setup.py%20.
- https://discuss.python.org/t/how-to-single-source-a-packages-version-when-publishing-to-pypi-using-github-action/50982/17

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

# Setup

https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/

https://setuptools.pypa.io/en/latest/userguide/declarative_config.html

## setup.py
```py
from setuptools import setup
import versioneer

if __name__ == '__main__':
    setup(
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )
```

## setup.cfg
```
[metadata]
name = dev
description = My dev repo
url = https://github.com/usr/repo

[options]
include_package_data = True
package_dir = 
    = src
packages = find:

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    pkg-run = my.pkg.main:cli   
```

## pyproject.toml
use `pyproject.toml` instead of `setup.cfg`: 
https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
```
[build-system]
requires = ['setuptools>=42', 'versioneer-518']
build-backend = 'setuptools.build_meta'

[project]
name = "pkg"
description = 'My package description'
dependencies = [
    "requests",
    'importlib-metadata; python_version<"3.8"',
]

[project.urls]
homepage = 'https://pkg.org'
documentation = 'https://pkg.org/docs/'
repository = 'https://github.com/usr/repo'

[project.entry-points]
pkg-run = 'my.pkg.main:cli'

[tool.setuptools]
include-package-data = true 

[tool.setuptools.packages.find]
include = ['pkg', 'pkg.*']
namespaces = false

[tool.versioneer]
VCS = "git"
style = "pep440"
versionfile_source = "pkg/_version.py"
versionfile_build = "pkg/_version.py"
tag_prefix = "v"
parentdir_prefix = "pkg-"

[tool.black]
line-length = 88
target-version = ['py39']
skip-string-normalization = true #disable string double quotes normalization
include = '\.pyi?$'
preview = false
```

# pyproject.toml

## use `pyproject.toml` instead of `setup.cfg`:
https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
```toml
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

# Setup

https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/

## setup.py
```py
from setuptools import setup

if __name__ == '__main__':
    setup()
```

## setup.cfg
```
[metadata]
name = dev
url = https://github.com/usr/repo
summary = My dev repo

[options]
include_package_data = True
package_dir = 
    = src
packages = find_namespaces:

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    pkg = my.pkg.main:cli
```

## pyproject.toml
```
[build-system]
requires = ["setuptools>=42", "versioneer-518"]
build-backend = "setuptools.build_meta"
```

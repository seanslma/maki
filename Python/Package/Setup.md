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

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

[options]
package_dir = 
    src
packages=find:

[options.packages.find]
where=src
```

## pyproject.toml
```

```

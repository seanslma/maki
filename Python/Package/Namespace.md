# Namespace

## Merging two Python packages into one namespace
Option 1: pkgutil (legal)
- Use a special `__init__.py` file at the root of the namespace package that explicitly tells Python to extend its path
- `from pkgutil import extend_path;__path__ = extend_path(__path__, __name__)` or
- `__path__ = __import__('pkgutil').extend_path(__path__, __name__)`

Option 2: no `__init__.py`
- omit the `__init__.py` file in the top-level directory of the shared namespace
- packaging with `setuptools`, have to use `find_namespace_packages`
  ```py
  # In setup.py or pyproject.toml
  from setuptools import setup, find_namespace_packages
  setup(
      name='my_company-core',
      ...
      packages=find_namespace_packages(where='src'),
      package_dir={'': 'src'},
  )
  ```

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

## inspect namespaces in a package
- use `dir` to list all objects
- use `inspect` to check object types
```py
import inspect
import polars as pl

def list_polars_namespaces_to_file(module, file_object, indent=0, max_level=5):
    """
    Recursively lists all "namespaces" (sub-modules and significant objects)
    within a given module, writing to a file with a maximum level depth.
    """
    if indent >= max_level:
        return
    prefix = "  " * indent
    for name in sorted(dir(module)):
        if name.startswith("_"):  # Skip private/internal attributes
            continue
        obj = getattr(module, name)
        if inspect.ismodule(obj) and obj.__name__.startswith('polars.'):
            # If it's a sub-module within polars
            file_object.write(f"{prefix}{name}\n")
            list_polars_namespaces_to_file(obj, file_object, indent + 1, max_level)
        elif inspect.isclass(obj) or inspect.isfunction(obj) or isinstance(obj, (int, float, str, bool, list, dict, set)) or (
            hasattr(obj, '__module__') and obj.__module__ and obj.__module__.startswith('polars.')
        ):
            # Consider classes, functions, common data types, and other polars-related objects
            file_object.write(f"{prefix}{name}\n")

max_depth = 5
output_filename = "./polars_namespaces.txt"
with open(output_filename, "w") as f:
    f.write("polars\n")
    list_polars_namespaces_to_file(pl, f, indent=1, max_level=max
```

# Import

https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/

## `import m` 
- searches for a module named m, 
- creates a module object for that module, and 
- assigns the module object to the variable

A `module` is anything that Python considers a module and knows how to create a module object for, includeing things like:
- Python files, 
- directories and 
- built-in modules written in C

A `module object` is a Python object that acts as a namespace for the module's names. 
The names are stored in the module object's dictionary (available as m.__dict__), so we can access them as attributes.

## Regular packages
If a directory contains a `__init__.py` file, it's considered to be a regular package.

## Namespace packages
- does not need the `__init__.py` file
- can place contents of a package across multiple locations

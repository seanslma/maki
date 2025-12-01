# Issue

## import pyarrow.lib as _lib
ImportError: DLL load failed while importing lib: The specified procedure could not be found.

solution:
```sh
pip install --upgrade pyarrow
```

## pyarrow read string column with all None values
https://arrow.apache.org/docs/python/generated/pyarrow.Table.html
- Be aware that Series of the `object` dtype don't carry enough information to always lead to a meaningful Arrow type.
- In the case that we cannot infer a type, e.g. because the DataFrame is of length 0 or the Series only contains None/nan objects, the type is set to `null`.
- This behavior can be avoided by constructing an explicit schema and passing it to this function

Related issues:
- https://github.com/apache/arrow/issues/2110
- https://github.com/apache/arrow/issues/19053

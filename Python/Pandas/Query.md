# Query

## TypeError: unhashable type
Pandas query error: TypeError: unhashable type: 'numpy.ndarray'
- Caused by `numexpr` package, the default engine. 
- Can change engine to: `df.query('', engine='python')`, but not efficient.
- Best to indicate using the python semantics: `df.query('', parser='python')` - not always work.

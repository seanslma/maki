# Query

## TypeError: unhashable type
Pandas query error: TypeError: unhashable type: 'numpy.ndarray'
- Caused by `numexpr` package, the default engine. 
- Can change engine to: `df.query('', engine='python')`, but not efficient.
- Best to indicate using the python semantics: `df.query('', parser='python')` - not always work.

## `&` vs `and`
https://stackoverflow.com/questions/21415661/logical-operators-for-boolean-indexing-in-pandas

`&` in pandas and numpy is element-wise logical-and while `and` only works for two boolean values.

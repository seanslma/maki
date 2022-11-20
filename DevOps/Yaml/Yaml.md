# yaml

## string quotes
https://leopathu.com/content/string-quotes-yaml-file

Strings containing any of the following characters must be quoted
- it's more convenient to use single quotes, without escaping any backslash \
  `:, {, }, [, ], ,, &, *, #, ?, |, -, <, >, =, !, %, @, \`
- double quotes provide a way to express arbitrary strings, by using \ to escape characters and sequences
  `"Add new line\n"`

## strings must be quoted
- string represents a boolean value (true or false)
- string is null or ~ (otherwise, it would be considered as a null value)
- string looks like a number, such as integers (e.g. 2), floats (e.g. 3.14) and exponential numbers (e.g. 1e7) (otherwise, it would be treated as a numeric value)
- string looks like a date (e.g. 2014-12-31) (otherwise it would be automatically converted into a Unix timestamp)

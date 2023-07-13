# String

## string quotes
https://leopathu.com/content/string-quotes-yaml-file

https://stackoverflow.com/questions/19109912/yaml-do-i-need-quotes-for-strings-in-yaml

https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines/21699210#21699210

Strings containing any of the following characters must be quoted
- `{ } [ ] < > = ! @ # % & * - ? : , | \` not always true, depending on where the character is
- it's more convenient to use single quotes, without escaping any backslash \
- double quotes provide a way to express arbitrary strings, by using \ to escape characters and sequences
  `"Add new line\n"`

## strings must be quoted
- string is `true` or `false` (otherwise, it would be treated as a boolean value)
- string is `null` or `~` (otherwise, it would be considered as a null value)
- string looks like a `number`, such as integers (11), floats (3.14) and exponential numbers (1e2) (otherwise, it would be treated as a numeric value)
- string looks like a `date` (e.g. 2014-12-31) (otherwise it would be automatically converted into a Unix timestamp)

Strings only need quotation if (the beginning of) the value can be misinterpreted as a data type or the value contains a ":" (could get misinterpreted as key):
- `foo: "{{ bar }}"` can be misinterpreted as datatype dict
- `foo: "bar:baz"` can be misinterpreted as key
- `>` interior line breaks are stripped out
  ```
  key: >
    A long
    string here.
  ```
- `|` interior line breaks are preserved as `\n`
  ```
  key: |
    A long
    string here.
  ```
- `>-` or `|-` no line breaks at the end

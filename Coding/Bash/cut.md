# cut

cut parts of lines from specified files or piped data and print the result to standard output.

## basic options
- `-f` (--fields): 1,3 [select 1 and 3]; -4 [select 1 to 4]
- `-c` (--characters): -c4- [select from 4th character to end]
- `-b` (--bytes): -b1 [select 1st byte]

## other options
- `-d` delimiter specified instead of default “TAB”
- `--output-delimiter` specify output delimiter, default to input delimiter
- `-s` (--only-delimited) not print lines without delimiters
- `--complement` exclude selected

## Example: get row field based on delimiter
Select field 4
```
> (echo '"title":"Math & Physics"' | cut -d '"' -f 4)
Math & Physics
```

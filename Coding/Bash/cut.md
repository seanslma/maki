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

## get second field
```sh
> echo '192.168.0.2 #test' | cut -d'#' -f2 #eq: awk -F'#' '{print $2}'
test
```

## get field based on delimiter
Select field 4
```sh
> echo '"title":"Math & Physics"' | cut -d '"' -f 4
Math & Physics
```

Delimiter has multiple spaces
```sh
tr -s ' ' | cut -d ' ' -f 8
```
use `tr` command along with squeeze option (`-s` flag ) to convert all multiple consecutive spaces to a single space.

## get value in square brackets
```sh
> echo 'dev:[1.0.0]' | cut -d'[' -f2 | cut -d']' -f1
1.0.0
```

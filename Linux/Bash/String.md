# String

## Quotes or not
Quote it if it can 
- be empty
- contain spaces (or any whitespace really)
- contain special characters (wildcards)
- not require word splitting and wildcard expansion

Not quoting strings with spaces 
- often leads to the shell breaking apart a single argument into many

### Single quotes
Single quotes protect the text between them verbatim.
- want to suppress interpolation and special treatment of backslashes

### Double quotes
Double quotes are suitable when variable interpolation is required or single quotes are required in the string.
- want to suppress word splitting and globbing
- ant the literal to be treated as a string, not a regex

## sed
replace `{"title":"` with nothing: `sed 's/{"title":"//g'`

## cut
```
> (echo '"title":"Math & Physics"' | cut -d '"' -f 4)
Math & Physics
```


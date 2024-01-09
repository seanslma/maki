# Match

## excel can't MATCH or VLOOKUP on column with mixed text and numbers
https://stackoverflow.com/questions/71755390/excel-cant-match-or-vlookup-on-column-with-mixed-text-and-numbers

A column with both integer and text values, the `match` does not work.

Solution
```vb
=INDEX(Details!E:E, MATCH(B2&"", Details!D:D&"", 0))
```

This is better than vlookup especially for large data sets
```vb
=VLOOKUP(B2&"", Details!D:E&"", 2, FALSE)
```

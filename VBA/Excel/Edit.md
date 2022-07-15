# Edit

## newline in cell text
```vb
"First Line" & Chr(10) & "Second Line"
```

## non-breaking space
Can be used to replace special chars such non-breaking space
```
substitue(A1, char(160), "")

# code() char to ascii code
# char() ascii code to char
```

## insert/delete rows/columns
```VB
Range("A4:A5").EntireRow.Insert/Delete
Range("A4:B4").EntireColumn.Insert/Delete

'format from above row
Rows(5).Insert , xlFormatFromLeftOrAbove
'format from below row
Rows(5).Insert , xlFormatFromRightOrBelow
```

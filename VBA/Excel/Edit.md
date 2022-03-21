# Edit

## insert/delete rows/columns
```VB
Range("A4:A5").EntireRow.Insert/Delete
Range("A4:B4").EntireColumn.Insert/Delete

'format from above row
Rows(5).Insert , xlFormatFromLeftOrAbove
'format from below row
Rows(5).Insert , xlFormatFromRightOrBelow
```

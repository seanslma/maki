# range

## range from cell value
  INDIRECT(CONCATENATE("A",B2))

## get subrange
```vb
'remove first row
set subrng=rng.offset(1).resize(rng.rows.count-1)
'remove first col
set subrng=rng.offset(0,1).resize(rng.rows.count, rng.columns.count-1)
```

## generic getrng
```vb
Function RngFirst(rng As Range) As Range
    'first cell in rng
    Set RngFirstCell = iif(rng.Cells.count = 1, rng, rng.Cells(1))
End Function

Function RngLastCUsedXlDown(rng0 As Range, Optional rowOffset As Long = 0) As Range
    'find last consecutively used cell at or below rng
    Dim rng As Range: Set rng = RngFirst(rng0).offset(rowOffset)
    Set RngLastCUsedXlDown = iif(IsEmpty(rng.offset(1, 0).Value), rng, rng.End(xlDown)) 'next cell is blank
End Function

Function RngLastCUsedXlRight(rng0 As Range, Optional colOffset As Long = 0) As Range
    'find last consecutively used cell at or after rng
    Dim rng As Range: Set rng = RngFirst(start0).offset(0, colOffset)
    Set RngLastCUsedXlRight = iif(IsEmpty(rng.offset(0, 1).Value), rng, rng.End(xlToRight)) 'next cell is blank        
End Function

Function GetRng(rng0 As Range, 
                Optional nrow As Long = -1, Optional ncol As Long = -1, _
		Optional rowOffset As Long = 0, Optional colOffset As Long = 0, _
		Optional xlDown As Boolean = True, Optional xlRight As Boolean = False, _
		Optional rowShift As Long = 0, Optional colShift As Long = 0) As Range
    Dim rng As Range: Set rng = RngFirst(rng0).offset(rowOffset, colOffset)
    If nrow = -1 Then nrow = iif(xlDown, RngLastCUsedXlDown(rng, rowOffset:=rowShift).row - rng.row + 1, rng0.rows.count - rowOffset)
    If ncol = -1 Then ncol = iif(xlRight, RngLastCUsedXlRight(rng.offset(rowShift, colShift)).Column - rng.Column + 1, rng0.Columns.count - colOffset)
    Set GetRng = rng.Parent.Range(rng, rng.offset(nrow - 1, ncol - 1))
End Function
```
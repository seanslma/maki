# Formatting

## conditional formatting
```
Sub Formatting()
  Set RngTable1 = Range(“A1:A10”)
  RngTable1.FormatConditions.Delete
  RngTable1.FormatConditions.Add Type:=xlCellValue, Operator:=xlBetween, _
        Formula1:="=100", Formula2:="=200"
  RngTable1.FormatConditions(1).Interior.Color = RGB(255, 0, 0)
End Sub
```

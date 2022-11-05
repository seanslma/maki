# trick

## IsEmpty returns true for "" cell
```vb
If val = "" Or IsEmpty(val) Then
  v = "Blank"
End If
```

## IsNumeric returns true for empty cell
```vb
Function ValIsNumber(ByVal val As Variant) As Boolean
    If IsError(val) Then
        ValIsNumber = False
    Else
        ValIsNumber = (Len(val) > 0 And IsNumeric(val))
    End If
End Function
```

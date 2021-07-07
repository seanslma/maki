# trick

## IsNumeric returns true for empty cell

```vb
If Len(val) > 0 And IsNumeric(val) Then
  v = val
End If
```
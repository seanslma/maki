# trick

## IsNumeric returns true for empty cell

```vb
If Len(val) > 0 And IsNumeric(val) Then
  v = val
End If
```

## IsEmpty returns true for "" cell
```vb
If val = "" Or IsEmpty(val) Then
  v = "Blank"
End If
```

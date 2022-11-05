# Hidden rows/cols

## get hidden rows/cols
```vb
' Determine the hidden rows
For i = 1 To 1048576
   If Rows(i).Hidden Then
     
   End If
Next i
' Determine the hidden columns
For i = 1 To 16384
   If Columns(i).Hidden Then
     
   End If
Next i
```

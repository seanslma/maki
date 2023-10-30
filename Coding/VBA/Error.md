# error
  
## catch error
```vb
Sub GotoExample()
    On Error GoTo Err
    
    Dim x As Long, y As Long
    x = 4
    y = 4 / 0
    x = 8
    
Done:
    Exit Sub
Err:
    Select Case MsgBox("Error: " & Err.Description, vbAbortIgnore+vbDefaultButton1)
    Case vbAbort
        End
    Case vbIgnore
        Ignore
    End Select    
End Sub
```

## check error value
https://stackoverflow.com/questions/66054898/excel-error-testing-cells-without-error-gives-type-mismatch-cverrxlerrna

```vb
TypeName(val) = "Error"
IsError(val)
```

`Variant/Error` cannot be compared to anything other than a `Variant/Error`, otherwise will throw a `type mismatch` error.
So if we need to check sepecif errors, we need first to ensure it's a `Variant/Error` value
```vb
If IsError(val) Then
    ' Variant/Error comparisons are safe here
    If val = CVErr(xlErrNA) Then
        ' we have the #N/A error
    Else
        ' cell contains an error, but it's not #N/A
    End If
End If
```

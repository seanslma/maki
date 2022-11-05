# error

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


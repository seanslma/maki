## perf

### Turn off screen updates and auto calculations
```vb
Public Sub DisableXlUpdate()
    If Application.Calculation = xlCalculationManual Then
        WaitAutoCalculationToFinish
    End If
    
    Application.StatusBar = ""
    Application.ScreenUpdating = False
    Application.EnableAnimations = False
    Application.Calculation = xlCalculationManual
End Sub
 
Public Sub EnableXlUpdate()
    WaitAutoCalculationToFinish
    Application.StatusBar = False
    Application.ScreenUpdating = True
    Application.EnableAnimations = True    
End Sub

Public Sub WaitAutoCalculationToFinish()
    Application.Calculation = xlCalculationAutomatic
    Do Until Application.CalculationState = xlDone
        DoEvents
    Loop
End Sub   
```

### Using ranges and arrays
```vb
'read all the values at once from the Excel cells, put into an array
val = Range("A1:C10000").Value2
'change the values in the array, not the cells 
For rw = LBound(val, 1) To UBound(val, 1)
  For cl = LBound(val, 2) To UBound(val, 2)
    v = val (rw, cl)
    If v > 0 Then 
      val(rw, cl) = v * v
    End If
  Next
Next
'write all the results back to the range at once
Range("A1:C10000").Value2 = val
```

### Bypass the clipboard (copy and paste)
```vb
'copy everything (formulas, values and formatting)
Range("A1").Copy Destination:=Range("A2")

'copy values only
Range("A2").Value2 = Range("A1").Value2

'copy formulas only
Range("A2").Formula = Range("A1").Formula     
```
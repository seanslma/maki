# CSV

## to_csv filtered only
```vb
Sub ToCSV(rng as Range, csvPath as String, optional visibleOnly as Boolean = True, optional wb As Workbook = Nothing)
    Application.DisplayAlerts = False
    Application.ScreenUpdating = False

    If visibleOnly Then
        Set rng = rng.SpecialCells(xlCellTypeVisible)
    End If
    rng.Copy

    Dim wsName as String
    If wb = Nothing Then
        wsName = Nothing
        Set wb = Application.Workbooks.Add        
    Else
        wsName = Format(Now, "tmp-ws-yyyyMMdd-hhmmss")
        wb.Sheets.Add.Name = wsName
    End If
    wb.ActiveSheet.Paste
    wb.SaveAs Filename:=csvPath FileFormat:=xlCSV, CreateBackup:=False
    If wsName = Nothing
        wb.Close SaveChanges:=False
    Else
        wb.Sheets(wsName).Delete
    End If    
    
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
End Sub
```

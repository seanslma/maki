# CSV

## sheet to csv
```vb
Sub SheetsToCSV()
    csv_dir = "C:\csv"
    xl_file = "C:/tmp/my_excel.xlsx"
    sheet_names = "sheet1:sheet2:sheet3"
    
    Set xl = CreateObject("Excel.Application")
    Set wb = xl.Workbooks.Open(xl_file)
    Set fs = CreateObject("Scripting.FileSystemObject")
    csv_file = csv_dir & "/" & fs.GetFileName(xl_file)
    For Each sheet_name In Split(sheet_names, ":")
        wb.Sheets(sheet_name).Activate
        csv_filepath = csv_file & sheet_name & ".csv"
        Debug.Print "Saving csv file: " & csv_filepath
        wb.SaveAs csv_filepath, 6 'csv_format = 6
    Next
    wb.Close False
    xl.Quit
End Sub
```

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
        wsName = "tmp.ws-" & TimestampID
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

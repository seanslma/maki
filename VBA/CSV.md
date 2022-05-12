# CSV

## csv to sheet
```vb
Sub CSVToSheet()
    strrngfr = "A1"
    filename = "my.csv"

    Dim csvRows As Variant: csvRows = ReadCsvRows(filename)
    
    Dim i0 As Long: i0 = LBound(csvRows)
    Dim nrow As Long: nrow = UBound(csvRows) - i0 ' last row is empty, separated by crlf, also include header
    Dim ncol As Long: ncol = ArrLen(Split(csvRows(LBound(csvRows)), ","))
    
    Dim i As Long
    Dim j As Long
    Dim vals As Variant
    ReDim arr(0 To nrow - 1, 0 To ncol - 1) As Variant
    For i = 0 To nrow - 1
        vals = Split(csvRows(i - i0), ",") '0-based index
        For j = 0 To ncol - 1
            arr(i, j) = vals(j)
        Next
    Next
    
    Dim rg As Range
    Set rg = Range(strrngfr).Offset(RowOffset:=0).Resize(RowSize:=nrow, ColumnSize:=ncol)
    rg.Value = arr
End Sub
```

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

# CSV

WB.SaveAS issues:
- will drop first empty line
- will save only Range.Text (not value/value2)

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

## to_csv advanced
```vb
Sub SheetsToCSV()
    dir = ThisWorkbook.Path
    xl_file = "my.xlsx"
    sheet_names = "a:b:c"
    
    Set xl = CreateObject("Excel.Application")    
    Debug.Print "Opening Excel file: " & xl_file
    Set wb = xl.Workbooks.Open(dir & "\" & xl_file)
    
    Dim rng As Range
    csv_file = dir & "\" & xl_file
    For Each sheet_name In Split(sheet_names, ":")
        With wb.Sheets(sheet_name).UsedRange
            nrow = .Rows.Count + .Row - 1
            ncol = .Columns.Count + .Column - 1
            Set rng = wb.Sheets(sheet_name).Range("A1").Resize(RowSize:=nrow, ColumnSize:=ncol)
            arr = rng.Value
            arr2 = rng.Value2
        End With        
        csv_filepath = csv_file & sheet_name & ".csv"       
        ArrValToCSV arr, arr2, csv_filepath
        Debug.Print "Saved csv file: " & csv_filepath
    Next
    wb.Close SaveChanges:=False    
    xl.Quit
    Debug.Print "Done"
End Sub

Sub ArrValToCSV(arr As Variant, arr2 As Variant, ByVal filename As String)
    Set fs = CreateObject("Scripting.FileSystemObject")
    If fs.FileExists(fielname) Then
        Kill filename
    End If
    Open filename For Output As #1
            
    Dim Line As String
    s = ArrShape(arr)
    If s(0) = 0 Then
        If VarType(arr) = vbDate Then
            Line = CStr(arr)
        ElseIf VarType(arr) = vbString Then
            Line = """" & CStr(arr2) & """"
        Else
            Line = CStr(arr2)
        End If
        Print #1, Line
    ElseIf s(0) = 1 Then
        Line = ""
        For i = s(1) To s(2)
            If VarType(arr(i)) = vbDate Then
                Line = Line & CStr(arr(i))
            ElseIf VarType(arr(i)) = vbString Then
                Line = Line & """" & CStr(arr2(i)) & """"
            Else
                Line = Line & CStr(arr2(i))
            End If
            If i < s(2) Then
                Line = Line & ","
            End If
        Next
        Print #1, Line
    Else
        For i = s(1) To s(2)
            Line = ""
            For j = s(3) To s(4)
                If VarType(arr(i, j)) = vbDate Then
                    Line = Line & CStr(arr(i, j))
                ElseIf VarType(arr(i, j)) = vbString Then
                    Line = Line & """" & CStr(arr2(i, j)) & """"
                Else
                    Line = Line & CStr(arr2(i, j))
                End If
                If j < s(4) Then
                    Line = Line & ","
                End If
            Next
            Print #1, Line
        Next
    End If
    
    Close #1
End Sub

Function ArrShape(arr As Variant) As Variant()
    d = ArrDim(arr)
    If d = 0 Then
        ArrShape = Array(0, 1, 1, 1, 1)
    ElseIf d = 1 Then
        ArrShape = Array(1, LBound(arr), UBound(arr), 1, 1)
    Else
        ArrShape = Array(2, LBound(arr), UBound(arr), LBound(arr, 2), UBound(arr, 2))
    End If
End Function

Function ArrDim(arr As Variant) As Long
On Error GoTo Err
    Dim i As Long
    Dim tmp As Long
    i = 0
    Do While True
        i = i + 1
        tmp = UBound(arr, i)
    Loop
Err:
    ArrDim = i - 1
End Function
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

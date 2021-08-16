# io

## write to file
```vb
Open "C:\test.csv" For Output As #1
Write #1, "xyz"
Close #1
```   

## read csv file
```vb
'read csv including header as array of strings
Function ReadCsv(filename As String) As String()
    Dim csvText As String
    csvText = ReadUtf8(filename)
    ReadCsv = Split(csvText, vbCrLf)
End Function
```     

## vb original method

```vb
Function ReadUtf8(fileName As String) As String
    On Error Resume Next
    Dim fnum As Integer
    Dim flen As Long
    fnum = FreeFile 'get unused file
    Open fileName For Binary Access Read Shared As #fnum
    If Err.Number <> 0 Then
        ErrMsgBox "File is not found: " & fileName, "File Reading Error"
    End If
    flen = LOF(fnum)
    ReadUtf8_vba = Space$(flen)  'Space$(LOF(fnum)) creates a string the size of the file
    Get #fnum, , ReadUtf8_vba
    Close #fnum
    
    If flen = 0 Then
        ErrMsgBox "File is empty: " & fileName, "File Reading Error"
    End If
End Function
```


## ADODB stream method

```vb
'need reference to ADODB
'Tools > References > Check the checkbox in front of "Microsoft ActiveX Data Objects 6.1 Library"
Function ReadUtf8_ado(fileName As String) As String
    Dim stream As ADODB.stream
    Set stream = New ADODB.stream
    stream.Charset = "utf-8"
    stream.Open
    On Error GoTo Nofile
    
    stream.LoadFromFile fileName
    ReadUtf8_ado = stream.ReadText() & ""
    stream.Close
    Set stream = Nothing
    Exit Function

Nofile:
    stream.Close
    Set stream = Nothing
    ErrMsgBox "Error Number: " & Err.Number & vbCrLf & _
        "Error Description: " & Err.Description & vbCrLf & "File: " & fileName, "File Reading Error"
End Function
```

## Export named ranges

```vb
Sub CopyNamedRanges()
    For Each x In ActiveWorkbook.Names
        Workbooks("Book2.xls").Names.Add Name:=x.Name, RefersTo:=x.Value
    Next
End Sub
```

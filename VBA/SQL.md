# sql

## create table
```vb
Public Sub CreateMDBTable(cnn As ADODB.Connection, table As String, cols As Variant, ctys As Variant)
On Error GoTo Errhandler
    DeleteMDBTable cnn, table
    
    Dim i As Long
    Dim qry As String: qry = "create table " & table & " ("    
    For i = LBound(cols) To UBound(cols)
        qry = qry & cols(i) & " " & ctys(i) & IIf(i < UBound(cols), ",", ");")
    Next
    cnn.Execute qry
    Exit Sub
    
Errhandler:
    MsgBox "Please close your MDB", vbCritical, "Error in creating MDB table"
End Sub

Public Sub DeleteMDBTable(cnn As ADODB.Connection, table As String)
    On Error Resume Next
    cnn.Execute "drop table " & table & ";"
    On Error GoTo 0
End Sub
```

## query to array
```vb
Public Function QueryToArray(cnn As ADODB.Connection, qry As String) As Variant
    Dim rs As ADODB.Recordset: Set rs = CreateObject(ADODB.Recordset)
    rs.Open qry, cnn, adOpenStatic, adLockOptimistic
    
    Dim records As Variant
    
    rs.MoveLast
    Dim cnt As Long: cnt = rs.RecordCount
    Dim j As Long
    Dim i As Long: i = 0
    rs.MoveFirst
    While Not rs.EOF
        If IsEmpty(records) Then
            ReDim records(0 To cnt - 1, 0 To rs.fields.Count - 1)
        End If
        For j = 0 To rs.fields.Count - 1
            records(i, j) = rs(j)
        Next
        i = i + 1
        rs.MoveNext
    Wend
    rs.Close
    
    QueryToArray = records
End Function
```

## array to table
```vb
Public Sub WriteArrayToTable(cnn As ADODB.Connection, table As String, records As Variant)
    Dim i, j As Integer
    Dim rs As ADODB.Recordset: Set rs = New ADODB.Recordset
    
    rs.Open table, cnn, adOpenKeyset, adLockOptimistic, adCmdTable
    With rs
        For i = LBound(records, 1) To UBound(records, 1)
            .AddNew
            For j = LBound(records, 2) To UBound(records, 2)
                .fields(j) = records(i, j)
            Next
            .Update
        Next
    End With
    rs.Close
    Set rs = Nothing
End Sub
```

## get record count
### client-side cursor type
```vb
Dim qry As String: qry = "select id, name from my_tbl"
Dim rs As ADODB.Recordset: Set rs = New ADODB.Recordset

'client-side cursor
rs.CursorLocation = adUseClient
rst.Open qry, CurrentProject.Connection

'returns actual recordcount
Debug.Print "Client-side rs record count: " & rs.RecordCount
rs.Close
```

### server-side cursor types
```vb
Dim qry As String: qry = "select id, name from my_tbl"
Dim rs As ADODB.Recordset: Set rs = New ADODB.Recordset

'return -1
rs.Open qry, CurrentProject.Connection, adOpenForwardOnly
rs.Close

'return either -1 or actual count, depends
rs.Open qry, CurrentProject.Connection, adOpenDynamic
rs.Close    

'return valid count; if -1 specifying lock type as adLockOptimistic may fix the issue
rs.Open qry, CurrentProject.Connection, adOpenKeyset
rs.Close   

'return valid count; if -1 specifying lock type as adLockOptimistic may fix the issue
rs.Open qry, CurrentProject.Connection, adOpenStatic
rs.Close     
```

## get odbc
```VB
Public Function GetMySQLODBCDriverStr() As String
    GetMySQLODBCDriverStr = "DRIVER={" & GetODBCStr("MySQL") & "};"
End Function

Public Function GetODBCStr(typ As String) As String
    Dim entryNames As Variant
    entryNames = GetRegEntryNames("SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers")
    
    Dim odbc As String: odbc = ""
    If Not IsEmpty(entryNames) Then
        Dim eName As Variant
        For Each eName In entryNames
            If (InStr(eName, typ)) Then
                odbc = eName
                Exit For
            End If
        Next
    End If

    If odbc = "" Then
#If Win64 Then
            MsgBox "You need to install 64 bit " & typ & " ODBC Driver!"
#Else
            MsgBox "You need to install 32 bit " & typ & " ODBC Driver!"
#End If
        End
    End If

    GetODBCStr = odbc
End Function

Public Function GetRegEntryNames(keyPath) As Variant
    Const HKEY_LOCAL_MACHINE = &H80000002
    Dim entryNames As Variant
    Dim valueTypes As Variant
    Set reg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\default:StdRegProv")
    reg.EnumValues HKEY_LOCAL_MACHINE, keyPath, entryNames, valueTypes
    GetRegEntryNames = entryNames
End Function


```

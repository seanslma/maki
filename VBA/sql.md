# sql

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
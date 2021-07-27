# other

MDB via C#

MDB via Python

## Check Outlook version
Open Outlook 2013 and click File in the top left hand corner. Now click Office Account, then About Office 2013. The version type will be displayed on the right hand side. You will have either 32-bit or 64-bit.

## Code

```sql
--list all objects in access
SELECT * FROM MSysObjects

--datetime format
SELECT * from nslp 
where ProfileName  = 'NSLP' and ProfileArea = 'VICAGL' 
and SettlementDate between #07/01/2017# and #06/30/2018#;

--cross join
SELECT *
FROM (select id from details) b, (select detail from details) c;

--distinct item
SELECT distinct a.ID, a.Name, a.Value
FROM t_Area as a;
```

```vb
' Close and Delete object
DoCmd.Close acTable, strTblNam 'close the table if it is open
DoCmd.DeleteObject acTable, strTblNam 'delete the table if it exists
```

```vb
' Check if table exists
Function TableExists(strTableName As String)
    Dim i As Integer
    Dim Exists As Boolean
    Exists = False
    CurrentDb.TableDefs.Refresh
    For i = 0 To CurrentDb.TableDefs.Count - 1
        If strTableName = CurrentDb.TableDefs(i).Name Then
            Exists = True 'Table Exists
            Exit For
        End If
    Next i
    TableExists = Exists
End Function
```

```vb
' Check if object is open
Function ObjectIsOpen(strName As String, intObjectType As Integer) As Boolean
' intObjectType can be: 0-acTable, 1-acQuery, 2-acForm, 3-acReport, 4-acMacro, 5-acModule
    On Error Resume Next
    ObjectIsOpen = (SysCmd(acSysCmdGetObjectState, intObjectType, strName) <> 0)
     
    If Err <> 0 Then
        ObjectIsOpen = False
    End If
End Function
```

Note that the order of the day and month in the date (default mm/dd/yyyy) is independent of the system culture setting.

## Export Objects
```vb
Sub ExportObject(typ As String, nam As String, db As String)
    DoCmd.TransferDatabase acExport, "Microsoft Access", db, ObjTyp(typ), nam, nam, False
End Sub
```

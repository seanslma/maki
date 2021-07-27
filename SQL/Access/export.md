# ExportObjs

```vb

Sub ClearErrs()
    mdb = "C:\acc.mdb"
    
    qry1 = "update tbl set col=0 where col2 = 'xyz';"
    qry2 = "delete * from tbl where col = 'xyz';"
    
    Dim db As Access.Application
    Set db = GetObject(mdb)
    db.DoCmd.RunSQL qry1
    db.DoCmd.RunSQL qry2
    
    MsgBox "All Done!"
End Sub

Public Sub MainFn()
    Dim dbTo As String
    dbTo = "C:\acc.mdb"
    
    'rename objects
    RnmObjs dbTo    
    
    'delete objects
    DelObjs dbTo
    
    'export objects
    ExpObjs dbTo
 
    MsgBox "All Done!"
End Sub

Sub RnmObjs(mdb As String)
    On Error GoTo Error_Handler
    Dim db As Access.Application
    Set db = GetObject(mdb)
    
    'tables
    RenameObject db, "tbl", "nam_old", "nam_new"
    
Error_Exit:
    On Error Resume Next
    db.Application.Quit
    Set db = Nothing
    Exit Sub
 
Error_Handler:
    MsgBox "Error " & Err.Number & vbCrLf & Err.Description, vbCritical, "Error in RenameObjects!"
    Resume Error_Exit
End Sub

Sub DelObjs(mdb As String)
    On Error GoTo Error_Handler
    Dim db As Access.Application
    Set db = GetObject(mdb)
    
    'tables
    DeleteObject db, "tbl", "tbl_x"
    
Error_Exit:
    On Error Resume Next
    db.Application.Quit
    Set db = Nothing
    Exit Sub
 
Error_Handler:
    MsgBox "Error " & Err.Number & vbCrLf & Err.Description, vbCritical, "Error in DeleteObjects!"
    Resume Error_Exit
End Sub

Sub ExpObjs(dbTo As String)
    On Error GoTo Error_Handler
    
    'tables
    ExportObject dbTo, "tbl", "tbl_x", True

    'queries
    ExportObject dbTo, "qry", "insert_qry"
    
    'forms
    ExportObject dbTo, "frm", "x_subform"
    
Error_Exit:
    On Error Resume Next
    Exit Sub
 
Error_Handler:
    MsgBox "Error " & Err.Number & vbCrLf & Err.Description, vbCritical, "Error in ExportObjects!"
    Resume Error_Exit
End Sub

Sub RenameObject(db As Access.Application, typ As String, nam_old As String, nam_new As String)
    db.DoCmd.Rename nam_old, ObjTyp(typ), nam_new
End Sub

Sub DeleteObject(db As Access.Application, typ As String, nam As String)
    db.DoCmd.DeleteObject ObjTyp(typ), nam
End Sub
 
Sub ExportObject(db As String, typ As String, nam As String, Optional strucOnly As Boolean = False)
    DoCmd.TransferDatabase acExport, "Microsoft Access", db, ObjTyp(typ), nam, nam, strucOnly
End Sub
 
Function ObjTyp(typ As String) As AcObjectType
    Select Case typ
        Case "frm"
            ObjTyp = acForm
        Case "mco"
            ObjTyp = acMacro
        Case "mod"
            ObjTyp = acModule
        Case "qry"
            ObjTyp = acQuery
        Case "rpt"
            ObjTyp = acReport
        Case "tbl"
            ObjTyp = acTable
        Case Else
            ObjTyp = acDefault
    End Select
End Function

Public Sub ExportObjects(db As String)
    On Error GoTo Error_Handler
 
     ' Tables
    For Each tdf In CurrentDb.TableDefs
        If Left(tdf.Name, 4) = "MSys" Then    'Ignore/Skip system tables
            ExportObject "tbl", obj.Name, db
        End If
    Next tdf
    
    ' Queries
    For Each qdf In CurrentDb.QueryDefs
        If Left(qdf.Name, 1) = "~" Then     'Ignore/Skip system generated queries
            ExportObject "qry", obj.Name, db
        End If
    Next qdf
    
    ' Forms etc
    For Each obj In CurrentProject.AllForms, AllReports, AllMacros, AllModules
        ExportObject "frm", obj.Name, db
    Next obj
 
Error_Handler_Exit:
    On Error Resume Next
    Set qdf = Nothing
    Set tdf = Nothing
    Set obj = Nothing
    Exit Sub
 
Error_Handler:
    MsgBox "Error Number: " & Err.Number & vbCrLf & _
           "Error Description: " & Err.Description, _
           vbCritical, "Error in Export Objects!"
    Resume Error_Handler_Exit
End Sub

```


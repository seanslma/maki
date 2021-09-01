# basic

Option Compare Text 'replace case insensitive

VBA default is passing variable ByRef

Use long not integer as integer will be converted to long and the performance will be affected

```vb
'check empty array
Len(Join(NewSnapshots, "")) = 0

'get address of named range 'data'
=ADDRESS(ROW(data),COLUMN(data),4) & ":" & ADDRESS(ROW(data)+ROWS(data)-1,COLUMN(data)+COLUMNS(data)-1,4)

'get comment
Function GetComment(xCell As Range) As String
   On Error Resume Next
   GetComment = xCell.Comment.Text
End Function

'get defined variable value
val = Worksheets(wsName).Range("varName").Value2

```

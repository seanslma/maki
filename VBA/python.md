# python

## call python
```vb
Sub RunPython()
    Dim wsh As Object: Set wsh = VBA.CreateObject("Wscript.Shell")
    Dim pyExe: pyExe = """python.exe"""
    Dim pyScript As String: pyScript = """" & ThisWorkbook.Path & "/my_python_script.py"""
    'wsh.Run pyExe & " " & pyScript
        
    Dim windowStyle As Integer: windowStyle = 0 '0-hide
    Dim waitOnReturn As Boolean: waitOnReturn = True
    wsh.Run "cmd.exe /S /C python " & pyScript, windowStyle, waitOnReturn
End Sub	
```
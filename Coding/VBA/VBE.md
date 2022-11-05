## other

### Visual Basic Editor (VBE)
  The VBE is Excel’s code area.
  Clicking Developer tab, then Visual Basic in the Code group.
  A shortcut for accessing the VBE is Alt-F11.
  
### Jump to Procedure/Function
  Select Some Procedure then hit Shift-F2
  And Ctrl-Shift-F2 takes you back
  
### Turn Off Annoying Error Alerts in VBE
  In VBE (Alt-F11) Tools > Options -> Auto Syntax Check

### Only popup MsgBox for unhandled error
  In VBE (Alt-F11) Tools > Options -> General -> Error Trapping -> Break on unhandled errors
  
### Method and Function
  VBA method should use Call with (), or use ',' to separate parameters
  Call Meth(a,b,c) or Meth a,b,c
  
### Show message in progress bar
  Application.StatusBar = "Macro running"
  
### Excel disappears when run macro
This is because vba will not recompile the vba when "CompileOnDemand" = False

Reg.exe add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "ForceVBALoadFromSource" /t REG_DWORD /d "1" /f
Reg.exe add "HKCU\Software\Microsoft\VBA\7.1\Common" /v "CompileOnDemand" /t REG_DWORD /d "0" /f 
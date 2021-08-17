# excel

python -m pip install xlrd==1.2.0

```python
#change number to Excel column letters
def ExcelNumToLetter(num):    
    letter = ''
    dividend = num
    while dividend > 0:
       modulo = (dividend - 1) % 26
       letter = chr(65 + modulo) + letter
       dividend = int((dividend - modulo) / 26)
    return letter
```


## win32com.client error
  python -m pip install pywin32 #this might be blocked by corporate firewall

raise AttributeError("%s.%s" % (self._username_, attr))
AttributeError: Excel.Application.Workbooks

When attributes on Excel.Application do not exist, it is usually because the Excel application is open (possibly hidden) and it is in a modal loop such as editing a cell or an open/save file dialog.

## Python call VBA MessageBox
```python
import win32api
import win32con

win32api.MessageBox(0, "My message", "title", win32con.MB_OK) #0 means on top of other windows
```

## py call vba
```python
import win32com.client

xlApp = win32com.client.DispatchEx('Excel.Application')
wb = xlApp.Workbooks.Open(Filename=yourworkbookname.xlsm)
xlApp.Run('macroName')
```


## vba call py

RetVal = Shell("<full path to python.exe> " & "<full path to your python script>")


## Excel to csv
```python
def create_vbs(dir):
    vbscript = """
           xxxxxxxxxxxx
    """
    file = os.path.join(dir, 'ExcelToCSV.vbs')
    with open(file,'wb') as f:
        f.write(vbscript.encode('utf-8'))
    return file
    
exefile = r'C:\ExcelToCsv.vbs'
xl_file = r'C:\WBook.xlsx'
csvpath = f'C:\output' 
call(['cscript.exe', exefile, xl_file, csvpath, "Sheet1:Sheet2"])
```

```VBScript ExcelToCSV.vbs
if WScript.Arguments.Count < 3 Then
    WScript.Echo "Usage should be: ExcelToCsv <xls/xlsx file> <csv path> <ws_name1:ws_name2>"
    Wscript.Quit
End If

csv_format = 6

xl_file = Wscript.Arguments.Item(0)
csv_path = WScript.Arguments.Item(1)
worksheet_names_str = WScript.Arguments.Item(2)

Set xl = CreateObject("Excel.Application")
Set wb = xl.Workbooks.Open(xl_file)

Set fso = CreateObject("Scripting.FileSystemObject")
for each worksheet_name in Split(worksheet_names_str,":")
    csvfile = FSO.BuildPath(csv_path, worksheet_name & ".csv")
    wb.Worksheets(worksheet_name).Activate
    wb.SaveAs csvfile, csv_format
next

wb.Close False
xl.Quit
```

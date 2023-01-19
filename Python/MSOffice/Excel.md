# Excel

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
    
def num_to_col(n):
    col = ''
    while n > 0:
        n, r = divmod (n - 1, 26)
        col = chr(r + ord('A')) + col
    return col

def col_to_num(col):
    n = 0
    for c in col:
        n = n * 26 + ord(c) - ord('A') + 1
    return n    
```
http://timgolden.me.uk/pywin32-docs/win32api.html

## win32com.client error
  python -m pip install pywin32 #this might be blocked by corporate firewall

raise AttributeError("%s.%s" % (self._username_, attr))
AttributeError: Excel.Application.Workbooks

When attributes on Excel.Application do not exist, it is usually because the Excel application is open (possibly hidden) and it is in a modal loop such as editing a cell or an open/save file dialog.

## Avoid hidden rows/cols (DO NOT USE `openpyxl` - too slow when it's not readonly)
https://towardsdatascience.com/how-to-load-excel-files-with-hidden-rows-and-columns-into-pandas-19d445fa5c47
```python
import openpyxl 

hidden_rows_idx = [
    row - 2
    for row, dimension in ws.row_dimensions.items() 
    if dimension.hidden
]

# List of indices corresponding to all hidden columns
hidden_cols_idx = [
    string.ascii_uppercase.index(col_name) 
    for col_name in [
        col 
        for col, dimension in ws.column_dimensions.items() 
        if dimension.hidden
    ] 
]
```

## Python call VBA MessageBox
```python
import win32api
import win32con

win32api.MessageBox(0, 'My message', 'title', win32con.MB_OK) #0 means on top of other windows
win32api.MessageBox(0, 'My message', 'title', win32con.MB_OKCANCEL | win32con.MB_ICONERROR) 
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
def sheets_to_csv(
    excel_filepath: str,
    sheet_names: List[str],
    csv_dir: str = None,
) -> None:
    """
    Convert Excel sheets to csv files.
    """
    csv_dir = csv_dir or os.path.dirname(excel_filepath)
    vbsfile = os.path.join(csv_dir, 'ExcelSheetsToCSV.vbs')
    create_sheets2csv_vbs(vbsfile)

    from subprocess import call
    call(['cscript.exe', vbsfile, csv_dir, excel_filepath, ':'.join(sheet_names)])

    if os.path.isfile(vbsfile):
        os.remove(vbsfile)
```
    
```python
with open(filepath,'wb') as f:
    f.write(inspect.cleandoc(vbscript).encode('utf-8'))
```    

```VBScript SheetsToCSV.vbs
If WScript.Arguments.Count < 3 Then
    WScript.Echo "Parameters: <csv_dir> <xl_file> <sheet1:sheet2...>"
    WScript.Quit
End If
csv_dir = WScript.Arguments.Item(0)
xl_file = WScript.Arguments.Item(1)
sheet_names = WScript.Arguments.Item(2)
Set xl = CreateObject("Excel.Application")
Set wb = xl.Workbooks.Open(xl_file)
Set fs = CreateObject("Scripting.FileSystemObject")
csv_file = csv_dir & "/" & fs.GetFileName(xl_file)
For Each sheet_name In Split(sheet_names, ":")
    wb.Worksheets(sheet_name).Activate
    wb.SaveAs csv_file & sheet_name & ".csv", 6 'csv_format = 6
Next
wb.Close False
xl.Quit
```

## Excel column letter to number
```python
def col_num(col: str) -> int:
    n = 0
    for c in col:
        n = n * 26 + ord(c) - 64 #ord('A')=65
    return n - 1
    
def col_rng(rng: str) -> Iterator[int]:
    cols = rng.split(':')
    return range(col_num(cols[0]), col_num(cols[-1]) + 1)

def col_ind(cols: str) -> List[int]:
    return [i for col in colstr.split(',') for i in col_rng(col)]    
```

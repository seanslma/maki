# How to fix a corrupted Excel file with high CPU usage

Excel's formula calcuation is multi-threaded and you have a decent computer hardware, but occationally your Excel file will freeze or even without responding for a while. In a even worse case, you have to terminate your Excel applications as it uses all the remaining CPU and you cannot do anything.

Here we discuss a commonly encountered problem when using Excel and the possible solutions to the issue.

## Issues
At some point, when you open your Excel file for editing, you are frustrated that the Excel file does not allow you do anything. 

Note that sometimes you can open the Excel file. But after editing some contents and trying to save the file the Excel became not responding again. Even turning off the Calculation option to `Manual` does not help.

Commonly encountered issues include:
- The Excel became blank and not responding
- The Excel bottom status showing `Calculating (4 Threads): 0%` for a long time without any progress
- Your Excel file size is large but there is not much data in the worksheets

These issues can be caused by many factors. If this is only related to a specific file and the same issue can be observed on different machines, it's most likely that this file was corrupted.

## Solutions
### Deleting excessive empty rows with formulas
A common problem for Excel files created without VBA is that such an Excel file has many formulas copied to the far bottom with many empty rows. This is created to allow more rows in the future. But these empty rows will significantly increase the file size and increase the time to calculate the formulas.

So we need to delete such empty rows. If the number of rows is large you will find it's not convenient to delete all the empty rows from the Excel. In this case, you can delete the rows with VBA scripts as list here (please backup your file before doing any fix):
```vb
Sub DeleteEmptyRowsAtSheetEnd()
    xlFile = "C:/Test.xlsx"        ' Excel filepath
    sheetNames = "Sales:Marketing" ' The name of the sheets
    Const checkColumn As Long = 1  ' Based on which column to check empty rows
    
    Set xl = CreateObject("Excel.Application")
    Set wb = xl.Workbooks.Open(xl_file)

    For Each sheet_name In Split(sheetNames, ":")
        Set ws = wb.Sheets(sheet_name)
        ' Find the last non-empty row in the specified column
        lastRow = ws.Cells(ws.Rows.Count, checkColumn).End(xlUp).Row
        Debug.Print sheet_name & " last non-empty row: " & lastRow
        ' Delete all rows below the last non-empty row
        ws.Rows((lastRow + 1) & ":" & ws.Rows.Count).Delete
    Next
    Debug.Print "Now save workbook"
    wb.Close True
    Debug.Print "Done"
    xl.Quit
End Sub
```

### Replacing low performance Excel functions by more efficient functions
We also need to avoid slow Excel calculation methods such as vlookup (replace them with index and match), votile methods etc.

### Replacing Excel formulas by VBA code
If the previous two step still cannot solve the issue, we need to consider using VBA instaed of the formulas to do some of the calculations.

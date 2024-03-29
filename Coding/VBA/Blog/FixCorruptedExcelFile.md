# How to fix a corrupted Excel file with high CPU usage

If you've ever experienced Excel freezing or using excessive CPU, you know how frustrating it can be. Here we discuss a commonly encountered problem with high CPU usage and provide practical solutions to optimize your Excel worksheets.


## Issues
At some point, when you open your Excel file for editing, you are frustrated that the Excel file does not allow you do anything.

Note that sometimes you can open the Excel file. But after editing some contents and trying to save the file the Excel becomes not responding again. It does not help even by turning off the calculation with the calculation option being set to `Manual`.

Commonly encountered issues include:
- The Excel becomes blank and not responding
- The Excel bottom status is showing `Calculating (4 Threads): 0%` for a long time without any progress
- The Excel CPU usage keeps high for a long time and the Excel uses all the remaining CPU
- Your Excel file size is large but there is not much data in the worksheets

These issues can be caused by many factors. If this is only related to a specific file and the same issue can be observed on different machines, it's most likely that this file was corrupted.


## Solutions
Here we discuss the steps to optimize your Excel file to avoid the mentioned issues.

### Deleting excessive empty rows with formulas
A common problem for Excel files is that there are too many formulas copied to the far bottom with many empty rows. This is created to allow more rows in the future. But these empty rows will significantly increase the file size and increase the time to calculate the formulas.

So we need to delete such empty rows. If the number of rows is large you will find it's not convenient to delete all the empty rows from the Excel. In this case, you can delete the empty rows with the VBA scripts provided here (please backup your file before doing any fix, and also change the values of the three variables `xlFile`, `sheetNames`, and `checkColumn` accordingly):
```vb
Sub DeleteEmptyRowsAtSheetEnd()
    xlFile = "C:/Test.xlsx"        ' Excel filepath
    sheetNames = "Sales:Marketing" ' The name of the sheets
    Const checkColumn As Long = 1  ' Based on which column to check empty rows

    Set xl = CreateObject("Excel.Application")
    Set wb = xl.Workbooks.Open(xlFile)

    For Each sheetName In Split(sheetNames, ":")
        Set ws = wb.Sheets(sheetName)
        ' Find the last non-empty row in the specified column
        lastRow = ws.Cells(ws.Rows.Count, checkColumn).End(xlUp).Row
        Debug.Print sheetName & " last non-empty row: " & lastRow
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
Excel includes a variety of functions, and some of them are known to be slower than others, especially when dealing with large datasets.

Here is a list of some slower Excel functions along with alternatives that generally offer better performance:
- **VLOOKUP/HLOOKUP**: Alternative **INDEX-MATCH**
- **SUMPRODUCT**: Alternative **SUMIFS** or **SUMPRODUCT with * operator**
- **COUNTIF**: Alternative **COUNTIFS**
- **OFFSET**: Alternative **INDEX**
- **ARRAY FORMULAS**: Alternative: Use **SUMIFS**, **INDEX-MATCH**, or other non-array alternatives
- **INDIRECT**: INDIRECT can be slow and volatile. Avoid using INDIRECT if possible.

Remember to use `ChatGPT` or `Bard` to help you to convert the formulas to the more efficient alternatives.

### Replacing Excel formulas by VBA code
If your Excel will be used doing complicated work and you find the Excel calculation is still very slow after the modification based on the previous two steps, please consider using VBA scripts instead of Excel formulas to do some of the calculations.

For example, in VBA we can create a dictionary instead of using the `INDEX-MATCH` functions to lookup values. By using VBA scripts, we only need to trigger the calculation when everything is ready. Thus we can significantly reduce the amount of calculation required.

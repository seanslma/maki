# How to fix a corrupted Excel file with high CPU usage

Excel's formula calcuation is multi-threaded and you have a decent computer hardware, but occationally your Excel file will freeze or even without responding for a while. In a even worse case, you have to terminate your Excel applications as it uses all the remaining CPU and you cannot do anything.

Here we discuss a commonly encountered problem when using Excel and the possible solutions to the issue.

## Issues
At some point, when you open your Excel file for editing, you are frustrated that the Excel file does not allow you do anything. Commonly issues include:
- The Excel became blank and not responding
- The Excel bottom status showing `Calculating (4 Threads): 0%` for a long time without any progress
- Your Excel file size is large but there is not much data in the worksheets

These issues can be caused by many factors. If this is only related to a specific file and the same issue can be observed on different machines, it's most likely that this file was corrupted.

## Solutions
### Deleting excessive empty rows with formulas
A common problem for Excel files created without VBA is that such an Excel file has many formulas copied to the far bottom with many empty rows. This is created to allow more rows in the future. But these empty rows will significantly increase the file size.

So we need to delete such rows (use VBA as number of rows can be large and cannot be finshed in UI - file saving will take a long time without any progress). After deleting these empty rows the file can also be much smaller.

### Replacing low performance Excel functions by more efficient functions
We also need to avoid slow Excel calculation methods such as vlookup (replace them with index and match), votile methods etc.

### Replacing Excel formulas by VBA code
If the previous two step still cannot solve the issue, we need to consider using VBA instaed of the formulas to do some of the calculations.

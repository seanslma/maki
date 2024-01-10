# How to fix a corrupted Excel file with high CPU usage

## high cpu
Sometimes, the Excel file can be very slow even without response. For example, after editing some data the status shows `Calculating (4 Threads): 0%` for a long time without any progress and the cpu usage is high.

This can be caused by many factors (check online for all possible issues). If this is only related to a specific file and have the same issue on different machines, this file can be corrupted.

## solution
A common problem is that such Excel files has many formulas copied to the far bottom with many empty rows. So we need to delete such rows (use VBA as number of rows can be large and cannot be finshed in UI - file saving will take a long time without any progress). After deleting these empty rows the file can also be much smaller.

We also need to avoid slow Excel calculation methods such as vlookup (replace them with index and match), votile methods etc.

If the previous two step still cannot solve the issue, we need to consider using VBA instaed of the formulas to do some of the calculations.

# Error

## Add a new line in form label
In a label caption, use the Shift+ Enter keys.

## Operation must use an updateable query
This happens when update and join are used together.\\
Solution: Add **DISTINCTROW** after **UPDATE**, example\\
```sql 
UPDATE DISTINCTROW g 
INNER JOIN v ON v.name = g.name AND v.id = g.id
SET gs.val = v.val
; 
```

## Cannot Open Database". It may not be a database ... or the file may be corrupt
reached the limit: 2 gigabytes, minus the space needed for system objects.


## error: 2501-The RunSQL action was canceled
The error is due to the Application.SecurityAutomation that is not set to "low" on forehand.

If you never accessed the file manually then it is not a trusted document for you yet and the run time error appears.

Hence, 2 alternatives:
1. You manually open it, enable content and make it a trusted document and then do your thing in VBA.
2. Or: before you start the query, insert:
```vba 
app.AutomationSecurity = msoAutomationSecurityLow 
app.DoCmd.RunSQL "blahblah"
app.AutomationSecurity = msoAutomationSecurityByUI
```

## Subform object is empty
The name in the VBA code must be the name of **control** [the yellow rectangle], e.g. xxx_subform.Requery

## Empty query records
when the query result is empty the control's form is not accessible, using 'subform.Form' will get a crash. in this case, we need to directly check the number of records in the query result by using 'n = DCount("*", "Qry_duplicate_bus_gen")'

when incorrectly set the data source for the main form and the data source record is empty, the form does not show, the combobox in the form does not update, and the control's form [subform.Form] could not accessed.

## Building SQL Queries with Date/Time Criteria in VBA
https://codekabinett.com/rdumps.php?Lang=2&targetDoc=date-time-data-type-vba-access

Date values need to be properly formatted for embedding in the SQL-String of a query in VBA.

The Jet-/Ace-Database-Engine, however, is stricter about dates. It will only recognize date-strings in either the US-Date-Format (MM/DD/YYYY) or the international ISO-Format (YYYY-MM-DD).

To deal with this issue, we have to explicitly format any date value in the international ISO-Date-Format by using the Format-Function for your date:
```vb
sql = "SELECT * FROM tbl " & _
      "WHERE DateValue >= #" & Format(aDateVariable, "yyyy-mm-dd") & "# " & _
      "  AND DateValue < #" & Format(anotherDateVariable, "yyyy-mm-dd hh:nn:ss") & "#;"
```      

## dao.dbengine.120
Python error: pywintypes.com_error: "Operation unavailable", "Class not registered"

the problem (and issue) is that installing office 2016 does not install an “exposed” version of the .120 engine.

The simple solution here is to install the data connectivity components for office, or a version of the Access runtime.

Install: Microsoft Access Database Engine 2010 Redistributable\\
https://www.microsoft.com/en-ca/download/details.aspx?id=13255

## Error 3033: You do not have the necessary permissions to use …
To overcome this slight problem, you need to create a shortcut and link the MDW (Microsoft Access Workgroup information file) with the MDB.

"C:\Program Files\Microsoft Office\Office16\MSACCESS.EXE" "c:\test.mdb" /wrkgrp "C:\Users\sma\AppData\Roaming\Microsoft\Access\System.mdw" /user

Solution: incorrectly tried to export Msys... table.  

## cannot delete from specified tables
Delete cannot combine with select statement; join with distinctrow is OK!
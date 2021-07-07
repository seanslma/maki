# excel

### hide ribbon
Ctrl + F1

### Find named ranges
Ctrl + G

### shortcut key

add newline: Ctrl + j
  
refresh or recalculate cell values: F9

move between sheets: Ctrl + PgUp/Dn

add filter: Shift + Ctrl + l

create chart: Ctrl + F1

goto cell: Ctrl + g

recalc all cells: CTRL + ALT + SHIFT + F9

show formulas: Ctrl + `

### col letter to number
=COLUMN(INDIRECT("D1"))

### interpolation
forecast only works for perfectly linear spaced data for interpolation\\
=FORECAST(f2,INDEX($c$2:$c$37,MATCH(f2,$b$2:$b$37,1)):INDEX($c$2:$c$37,MATCH(f2,$b$2:$b$37,1)+1),INDEX($b$2:$b$37,MATCH(f2,$b$2:$b$37,1)):INDEX($b$2:$b$37,MATCH(f2,$b$2:$b$37,1)+1))  f2:x_new, c:y, b:x

  
* copy cols to col (x is the matrix name, G1 is the first cell in destination)
  =OFFSET(x, MOD(ROW()-ROW($G$1),ROWS(x)), TRUNC((ROW()-ROW($G$1))/ROWS(x)), 1, 1)
  
* copy rows to col (x is the matrix name, G1 is the first cell in destination)
  =OFFSET(x, TRUNC((ROW()-ROW($G$1))/COLUMNS(x)), MOD(ROW()-ROW($G$1),COLUMNS(x)), 1, 1)
  
* text to date
  =value("2019-02-02 12:55:00")
  
```excel
MAX(INDIRECT("A"&B1&":A"&B2))
```

* get dir of current workbook

```excel
=LEFT(CELL("filename",A1),FIND("[",CELL("filename",A1))-1)
```

### Add-In error
Error: Object variable or With block variable not set

Since the add-in was registered with excel, the following line succeeded:\\
**Set addin = Application.COMAddIns("My AddIn")**\\
But since it was disabled, the object was not created and\\
**Set automationObject = addin.Object**
resulted in Nothing

Solution: File -> Options -> Add-Ins -> Select the type of that Add-In and click 'Go' -> Enabled it

### Unhide cols
When hide and unhide do not work, it is possible that the panel is freezed.

### change module names
select the module and press F4

### get value based on row number
=INDEX(A1:E100,row,col)

=AVERAGE(OFFSET($C$1,E2-1,0,E3-E2,1))

### force vba rebuid
Reg.exe add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v "ForceVBALoadFromSource" /t REG_DWORD /d "1" /f
Reg.exe add "HKCU\Software\Microsoft\VBA\7.1\Common" /v "CompileOnDemand" /t REG_DWORD /d "0" /f

### excel locked for editing
first delete the hidden ownership file, in the same folder, using a dos command 'dir' and 'del'

then perhaps need to check which user locks the file using cmd mmc (Microsoft Management Console) by adding opened files (need server admin permission).

### check if a cell is referenced or not
  Formulas > Trace Dependents
  Formulas > Remove Arrows > Remove Dependent Arrows
  
### Find links (external references) in a workbook
  'does not work for formula in conditional format,
  Find and Replace -> Options 
  -> [Find what]=.xl, [Within box]=Workbook,[Look in]=Formulas 
  -> Find All
  'use findlink.xlam instead: https://www.manville.org.uk/software/findlink.htm
  -> Data -> BMA Group -> Find Links

### ArrayFormula does not work when including INDIRECT function
why? do not need to input the brackets but use Shift + Ctrl + Enter
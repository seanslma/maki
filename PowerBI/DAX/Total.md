# Total

https://community.powerbi.com/t5/Quick-Measures-Gallery/Measure-Totals-The-Final-Word/m-p/547907

https://community.powerbi.com/t5/DAX-Commands-and-Tips/Dealing-with-Measure-Totals/td-p/63376

## calculate total use a different formula
The total is the sum of the values in each row for a value of `AnotherTbl[AnotherCol]`
```
MyCalculatedCol = 
    VAR __row_val = MyMeasure    
    VAR __is_row = HASONEFILTER(MyTable[MyColInTbl])
RETURN
    if(__is_row, 
        __row_val, 
            VAR __tbl = SUMMARIZE(MyTable, AnotherTbl[AnotherCol], "@val", [MyMeasure]) 
            VAR __tot = SUMX(__tbl, [@val])
        RETURN __tot
    )
```

# Matrix

## subtotal
customize subtotals and totals:
https://community.powerbi.com/t5/Desktop/Different-DAX-calculations-for-different-row-hierarchies-in-a/m-p/2136701#M788896
```
Switch = 
var _territoty=1
var _region=2
var _Total=3
return 
IF (
    ISINSCOPE ( 'Table'[Region] ),
    IF ( ISINSCOPE ( 'Table'[Territory] ), _territoty, _region ),
    _Total
)
```

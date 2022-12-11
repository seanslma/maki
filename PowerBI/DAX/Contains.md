# Contains

## val of tab1 in tab2
https://community.powerbi.com/t5/Desktop/DAX-query-to-compare-a-value-in-one-table-to-see-if-it-exists-in/m-p/57029#M23247

If just use COUNTROWS(Tab2) by itself, you'd get the total number of rows for that table showing up for every row in Tab1.
```
InTable2 = CALCULATE(COUNTROWS(Tab2), FILTER(Tab2, Tab2[Id]=Tab1[Id], Tab2[Type]="Dev"))
```

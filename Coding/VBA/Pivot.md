# pivot table

```vb
'change Pivot Table Data Source Range Address
pivot_sht.PivotTables(PivotName).ChangePivotCache 
    ThisWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:=NewRange)
      
'ensure Pivot Table is Refreshed
pivot_sht.PivotTables(PivotName).RefreshTable

'get number of rows
nrw = pivot_sht.PivotTables(PivotName).TableRange1.Rows().Count
```
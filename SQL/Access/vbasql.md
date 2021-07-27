# vba

## pass parameters
```sql
SELECT [case] & '_' & Format(start_year,"yy") & Format(end_year,"yy") AS Expr1, 
       [startyear] AS start_year, 
       [endyear] AS end_year
FROM tbl
WHERE id=[idx];
```

```vb
Set cmd.ActiveConnection = CurrentProject.Connection
cmd.CommandText = "Insert_Tbl"
cmd.Execute , Array(txtCase, (year - 1) & "-07-01", year & "-07-01", txtCase), adCmdStoredProc
```

## get table row count
```vb
Cnt = DCount("*", "TableName")
Cnt = DCount("[FieldName]", "TableName")
'will not be used
Dim rs As DAO.Recordset
Set rs = db.OpenRecordset("SELECT Count([FieldName]) AS RecCount FROM TableName;")
r.MoveLast
Cnt = rs.RecordCount
rs.Close
```

## delete with inner join
```sql
DELETE FROM Table_A 
WHERE myid IN 
( SELECT myid 
  FROM Table_B 
  WHERE Table_A.myid = Table_B.myid 
);
```

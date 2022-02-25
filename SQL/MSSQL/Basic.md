# Basic

## temporal table 
```sql
CREATE TABLE #tmp1 (id INT, name VARCHAR(25), value float)  
INSERT INTO #tmp1 VALUES (1, 'John', 1.1), (2, 'Ana', 2.2) 
SELECT * FROM #tmp1
DROP TABLE #tmp1
```

## json variable
```sql
DECLARE @json1 nvarchar(100)
SET @json1 = N'[{"a": "1"}, {"a": NULL}]'
```

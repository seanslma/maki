# ANSI NULLS

## test ANSI NULLS ON / OFF
```sql
CREATE TABLE #tmpx (i int, v float);
INSERT INTO #tmpx VALUES (1, 1.1), (2, null);

SET ANSI_NULLS ON;
GO

DECLARE @val float;
set @val=1;

select * from #tmpx where v <> @val;
GO

# compare column with column does not work
select t2.* from #tmpx as t2
join (select * from #tmpx) as t1
on t1.i = t2.i
where t1.v <> t2.i
GO

DECLARE @json1 nvarchar(100);
SET @json1 = N'[{"i": 1, "v": null}, {"i": 2, "v": 3.3}]';

MERGE #tmpx WITH (XLOCK, ROWLOCK) AS t
USING ( 
    SELECT * FROM OPENJSON(@json1) 
        WITH (i int, v float) 
) AS j
ON t.i = j.i
WHEN MATCHED AND t.v <> j.v
THEN UPDATE
    SET t.v = j.v
WHEN NOT MATCHED BY TARGET THEN
    INSERT (i, v) VALUES (j.i, j.v)
;
GO
```

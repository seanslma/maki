# PartitionBy

https://www.sqlshack.com/sql-partition-by-clause-overview/

PartitionBy will calculate the aggregated value in each partition and broadcast the value back to each row; can add original col as well - so the row number will not decrease.

```sql
IF OBJECT_ID(N'tempdb..#tmpx') IS NOT NULL
BEGIN
	DROP TABLE #tmpx
END
;

CREATE TABLE #tmpx (i int, j int, v float);
INSERT INTO #tmpx VALUES (1, 1, 1), (1, 1, 2), (1, 2, 3);

SELECT i, 
       AVG(v) AS AvgV, 
       MIN(v) AS MinV 
FROM #tmpx
GROUP BY i;

SELECT i, v,
       AVG(v) OVER(PARTITION BY i order by j desc) AS AvgV, 
       MIN(v) OVER(PARTITION BY i) AS MinV
FROM #tmpx;

-- why the average different???
SELECT i, v,
       AVG(v) OVER(PARTITION BY i order by j asc) AS AvgV, 
       MIN(v) OVER(PARTITION BY i) AS MinV
FROM #tmpx;
```

## combine with groupby
```sql
SELECT i, j,
    AVG(AVG(v)) OVER(PARTITION BY i order by j) AS AvgV
FROM  #tmpx
GROUP BY i;
```

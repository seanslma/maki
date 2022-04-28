# PartitionBy

https://www.sqlshack.com/sql-partition-by-clause-overview/

PartitionBy will calculate the aggregated value in each partition and broadcast the value back to each row; can add original col as well - so the row number will not decrease.

```sql
CREATE TABLE #tmpx (i int, v float);
INSERT INTO #tmpx VALUES (1, 1), (1, 2), (1, 3), (2, 9);

SELECT i, 
       AVG(v) AS AvgV, 
       MIN(v) AS MinV, 
       SUM(v) AS SumV
FROM #tmpx
GROUP BY i;

SELECT i, 
	   v,
       AVG(v) OVER(PARTITION BY i) AS AvgV, 
       MIN(v) OVER(PARTITION BY i) AS MinV, 
       SUM(v) OVER(PARTITION BY i) AS SumV
FROM #tmpx
where v > 1;
```

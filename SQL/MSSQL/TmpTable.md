# Tmp Table

## create and delete tmp table
```
CREATE TABLE #tmp_tbl (
    name VARCHAR(30)
);


INSERT INTO #tmp_tbl
VALUES ('Ai'),('Cob'),('Gle');

DROP TABLE #tmp_tbl;
```

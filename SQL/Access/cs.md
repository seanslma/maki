# Basic

## Number of record count in query

Cnt = DCount("*", "Qry_xxx")

After call 'Set rs = CurrentDb.OpenRecordset(strSQL)', we must first check if the records are empty by rs.EOF\\
if not, to get the number of records, we need to call 'rs.MoveLast' before use cnt = rs.RecordCount

## Introduction to data types and field properties
https://support.office.com/en-us/article/introduction-to-data-types-and-field-properties-30ad644f-946c-442e-8bd2-be067361987c

## update t1 based on t2
```sql
UPDATE t1
INNER JOIN t2 ON t1.id = t2.id
SET t1.Unit = t2.Unit, t1.Region = t2.Region
WHERE t1.Station = 'AGL'
```
# Incremental refresh

## steps
https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview

- Add two parameters `RangeStart` (data start date) and `RangeEnd`
- Apply customer filter to the data column: right click the column ->  Date/Time Filters -> Custom Filter
- Define incremental refresh policy on the table: right click -> incremental refresh

## limitation
- cannot work for data with last_updated timestamp (upsert not supported)
- table references to the refresh table will not get all the data (not refreshed).\
  https://community.powerbi.com/t5/Desktop/incremental-refresh-on-table-by-reference/td-p/940721

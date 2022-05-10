# Data Source

## incremental refresh
https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview

- Add twp parameters `RangeStart` (data start date) and `RangeEnd`
- Apply customer filter to the data column: right click the column ->  Date/Time Filters -> Custom Filter
- Define incremental refresh policy on the table: right click -> incremental refresh 

# Basic

## DirectQuery vs Import
**DirectQuery** will run queries directly in the DB server, and all of the normal Power Query transformation features can be used.

**Import** will cache the data so the file size is larger, and has limitations on the dataset size and cannot switch back to the Directquery method.

## REST API with dynamic parameter
https://blog.crossjoin.co.uk/2016/08/23/web-contents-m-functions-and-dataset-refresh-errors-in-power-bi/

"The problem is that when a published dataset is refreshed, Power BI does some static analysis on the code to determine what the data sources for the dataset are and whether the supplied credentials are correct. Unfortunately in some cases, such as when the definition of a data source depends on the parameters from a custom M function, that static analysis fails and therefore the dataset does not refresh."

Query parameter can be overwritten:
```
Web.Contents(
 "https://data.gov.uk/api/3/action/package_search?q=apples", 
 [Query=[q="oranges"]]
)
```

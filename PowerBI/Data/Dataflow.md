# Dataflow
- https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-create
- https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-develop-solutions

## example
https://data-marc.com/2019/04/16/pimp-the-dataflows-connector-in-power-bi/

```
let
    Source = PowerBI.Dataflows(null),
    #"My WorkspaceId" = Source{[workspaceId="1123-4566-897"]}[Data],
    #"My WdataflowId" = #"My WorkspaceId"{[dataflowId="123-456"]}[Data],
    #"My First Table" = #"My WdataflowId"{[entity="my-table-name"]}[Data],
    #"My Sorted Rows" = Table.Sort(#"My First Table",{{"SALESDATE", Order.Descending}})
in
    #"My Sorted Rows"
```
- `PowerBI.Dataflows(null)` returns all dataflows in all namespaces where the logged-in user has access to on tenant level.
- `PowerBI.Dataflows()` similar to `PowerBI.Dataflows(null)`, its exact behavior might differ depending on the context and Power BI version
- `PowerBI.Dataflows([])`, not recommended. why?

## DirectQuery
- https://community.fabric.microsoft.com/t5/Service/Report-not-updating-using-Data-Flow/m-p/2977125
- https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-directquery

For connection to DataFlow, if using `import` instaed of `directquery` the report will not be updated automatically.
- For visuals using DirectQuery tables the visual will query to get the latest data from the data source.
- For visuals using imported tables the visual will only query data already imported to the dataset on the last data refresh.

To use `directquery` we should do
- subscription must be `Premium`
- Data -> Table -> right click: enable `"Include in report refresh`
- Navigate to the Premium dataflow, and set `enhanced compute engine` to `On`, and refresh the dataflow

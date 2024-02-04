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

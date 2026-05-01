# Incremental Refresh

## Move Unpivot to SQL query for folding
Unpvot will lead query becomig unfoldable - failure for incremental refresh.

Solution: move the unpivot to sql query.

```powerquery
let
    // Define the SQL command
    SqlStatement = "
        SELECT id, some_column, attribute_name, attribute_value
        FROM your_table
        UNPIVOT (
            attribute_value FOR attribute_name IN (col1, col2, col3)
        ) AS unpvt
        WHERE date_column >= @RangeStart 
          AND date_column < @RangeEnd",
    
    // Connect to the source
    Source = Sql.Database("your_server", "your_database"),
    
    // Execute Native Query with Parameters
    Data = Value.NativeQuery(
        Source, 
        SqlStatement, 
        [RangeStart = RangeStart, RangeEnd = RangeEnd], 
        [EnableFolding = true]
    )
in
    Data
```

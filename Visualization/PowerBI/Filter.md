# Filter

## TRETAS
TRETAS WILL transfers a filter context from a table to another, simulating the behavior of a physical relationship defined in the data model. 

Filter in lookup_column will be applied to target_column
```
[Filtered Measure] :=
CALCULATE (
    <target_measure>,
    TREATAS (
        VALUES ( <lookup_column> ),
        <target_column> 
    )
)

[Total Amount] :=
CALCULATE (
    SUM ( Sale[Amount] ),
    TREATAS (
        SUMMARIZE ( 'Date', 'Date'[Year], 'Date'[Month] ),
        Sale[Year],
        Sale[Month]
    )
)
```

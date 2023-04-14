# Dax table

## Datatable
```
NameQuarter = DATATABLE(
    "Name", STRING,
    "Quarter", INTEGER, 
    {
        {"Q1", 1}, {"Q2", 2},
    }
)
```

## Distinct Cols
```
NewTable = DISTINCT(SELECTCOLUMNS(
    Filter(
        OldTable,  
        OldTable[CodeId] = 1
        && OldTable[Year] >= YEAR(TODAY())-1 && OldTable[Date] >= TODAY() - 90
    ),
    "NewCol1", [OldCol1], 
    "NewCol2", [OldCol2]
))
```

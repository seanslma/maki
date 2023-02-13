# Calculate

## column with fixed value (not affected by filters)
```
VAR __val = CALCULATE(
    AVERAGE(ValTable[Value]), 
    ALL(AttributeTypes),
    AttributeTypes[Attribute] = "New"
)
```

## multiple conditions
```
VAR __val = CALCULATE(
    SUM(ValTable[Value]),
    ALL(ValTable[Year]), 
    AttributeTypes[Attribute] in {"New", "Used"},
    ValTable[Year] <= SELECTEDVALUE(ValTable[Year])
)
```

## calculate with treatas
```
VAR __val = Calculate(
    AVERAGE(Tab1[Quantity]),
    TREATAS(
        SUMMARIZE(Tab2, Tab2[RegionId], Tab2[CountryId], Tab2[SateId]),
        Tab1[RegionId],
        Tab1[CountryId],
        Tab1[StateId]
    )
)
```

## divid with sumx
```
VAR __val = DIVIDE( 
    CALCULATE(
        SUMX(
            NATURALLEFTOUTERJOIN(Tab1, Tab2),  
            Tab1[Quantity] * Tab2[Price]
        ),
        TREATAS(
            SUMMARIZE(Tab1, Tab1[RegionId], Tab1[CountryId], Tab1[StateId]),
            Tab2[RegionId],
            Tab2[CountryId],
            Tab2[StateId]
        )  
    ),
    SUM( Tab1[Quantity] )
)
```

## calculated column in Records with filter
```
HasRecords = CALCULATE(
    COUNTROWS(Tbl), 
    FILTER(
        ALL(Tbl[RecordId], Tbl[Year]), 
        Tbl[RecordId]=Records[Id] && Tbl[Year] <= YEAR(TODAY())
    )
) > 0
```

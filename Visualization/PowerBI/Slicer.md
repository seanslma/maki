# Slicer

home table
https://forum.enterprisedna.co/t/applying-two-slicers-from-the-same-field-on-table-visual/7454/10

## selected value
```
VAR __val = CALCULATE(
    SUM(Tbl[Value]), 
    ALL(Tbl[Quarter]),
    Tbl[Quarter] <= SELECTEDVALUE(Tbl[Quarter])
)
```

## sync slicers
https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers?tabs=powerbi-desktop#sync-and-use-slicers-on-other-pages

## Default max value
PowerBI will remember a constant value so we need to replace the max with a constant, e.g.
```
DateStr = 
    VAR MaxDate = MAX(Dates[Date])
    VAR SecondMaxDate = MAXX(FILTER(Dates,[Date]<MaxDate), Dates[Date])
Return 
    SWITCH(Dates[Date], MaxDate, "Today", SecondMaxDate, "Yesterday", FORMAT(Dates[Date], "yyyy-MM-dd hh:mm:ss"))
```

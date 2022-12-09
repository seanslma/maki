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

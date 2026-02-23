# Format

## Measure format
Measure format can be dynamc, so depends on the data type, you can show different number of digital places.

```dax
VAR __att = SELECTEDVALUE(AttributeTypes[Attribute])
VAR __is_integer = __att IN {"Quantity", "Count"} 
RETURN IF(__is_integer, "#,0", "#,0.00")
```

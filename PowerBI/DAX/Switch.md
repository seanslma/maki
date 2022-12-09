# Switch

```
VAR __att = SWITCH(
    SELECTEDVALUE(InputTypes[Input]),
    "Rate", 
        AVERAGE(ValTable[Value]),
    BLANK()
)
```

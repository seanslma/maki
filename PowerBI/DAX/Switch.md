# Switch

```
VAR __att = SWITCH(
    SELECTEDVALUE(InputTypes[Input]),
    "Avg", 
        AVERAGE(ValTable[Value]),
    "Max", 
        MAX(ValTable[Value]),        
    BLANK()
)
```

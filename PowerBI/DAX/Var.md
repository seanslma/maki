# Var
Variables are calculated within the scope in which they are written, and then the result of them is stored and used in the rest of the expression.

## Var vs Measure
- Var will calculate the value in advance and **store it**
- Measure can be considered a **function** and will be calculated in place with **current context**

## Wrong place to use var
https://radacad.com/caution-when-using-variables-in-dax-and-power-bi

Using var defined outside of the calculation context will lead to wrong results.

Wrong
```
Cost =     
    VAR __val = [Amount] * [Price]
    VAR __tbl = SUMMARIZE(tbl, tbl[yr], "@val", __val) //__val calculated for all years
    VAR __tot = SUMX(__tbl, [@val]))
    VAR __is_val = HASONEVALUE(tbl[yr])
    VAR __ret = IF(__is_val, __val, __tot)
RETURN
    __ret
```

Correct
```
Cost__ = [Amount] * [Price]
Cost = 
    VAR __is_val = HASONEVALUE(tbl[yr])
    VAR __ret = IF(
        __is_val,
        [Cost__],
        VAR __tbl = SUMMARIZE(tbl, tbl[yr], "@val", [Cost__])
        VAR __tot = SUMX(__tbl, [@val])
        RETURN __tot
    )     
RETURN
    __ret
```

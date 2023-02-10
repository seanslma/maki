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
Total = 
    VAR __val = [v1] + [v2]
    VAR __tbl = SUMMARIZE(tbl, tbl[yr], "@val", __val) //__val calculated for all years
RETURN
    SUMX(__tbl, [@val]))
```

Correct
```
Total = 
    VAR __tbl = SUMMARIZE(tbl, tbl[yr], "@val", [v1] + [v2])
RETURN
    SUMX(__tbl, [@val]))
```

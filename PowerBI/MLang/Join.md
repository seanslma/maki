# Join

https://learn.microsoft.com/en-us/powerquery-m/table-join

## Inner join
```
Table.Join(
    Tbl1, "CustomerID",
    Tbl2, "CustomerID",
    JoinKind.Inner
)
```

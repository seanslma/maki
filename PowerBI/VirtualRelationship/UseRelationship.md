# USERELATIONSHIP

Will activate the n-n relationship. Best to set the filter direction.

```
TotalFee = CALCULATE(
  SUM(TblFee[Fee]),
  USERELATIONSHIP(TblDept[Dept],TblFee[Dept]),
  USERELATIONSHIP(TblDept[Year],TblFee[Year])
)
```

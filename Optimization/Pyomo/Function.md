# Function
https://pyomo.readthedocs.io/en/stable/developer_reference/expressions/performance.html

## summation
- summation = sum_product
- dot_product = sum_product
```py
m.x = pyo.Param(m.I, within=pyo.Reals)
m.y = pyo.Var(m.I, bounds=(0.0, 10.0), domain=pyo.NonNegativeReals, initialize=0.001)
pyo.summation(m.x, m.y, index=m.I)
```

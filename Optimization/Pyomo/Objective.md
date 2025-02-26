# Objective

## using `summation`
```py
model.coeffs = Param(model.set_i, model.set_j, default=1) 
def obj_rule(model):
    return summation(model.coeffs, model.x)
model.obj = Objective(rule=obj_rule, sense=maximize)
```

## using expression
```py
def obj_rule(model):
    expr = 0
    for i in model.I:
        for j in model.J:
            expr += log(model.x[i,j]) + model.x[i,j]**2
    return expr
```

## using index
```py
def obj_rule(model, i, j):
    if i == j:
        return Objective.Skip
    else:
      return 2 * model.x[i,j]
model.obj = Objective(model.set_i, model.set_j, rule=obj_rule, sense=minimize)
```

## update objective
```py
m.obj = Objective(expr=m.x)
m.obj.set_value(expr=m.o.expr + m.e)

m.obj_base = m.x1 + 2 * m.x2, 
m.obj_changing = m.x1 * m.x2, 
m.obj.set_value(expr=m.base_expr + m.changing_expr)
```

## add a term to objective
```py
import pyomo.environ as pyo

# create model and var
m = pyo.ConcreteModel()
m.x = pyo.Var(within=pyo.NonNegativeReals)

# create obj
@m.Objective()
def obj(m):
    return 0
m.obj.pprint()

# add a term
m.obj += m.x**2
m.obj.pprint()
```

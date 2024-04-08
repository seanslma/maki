# Constraint

## expression
```py
model.con1 = Constraint(expr=2.0 <= model.x + model.y[0,2]) 
model.con2 = Constraint(expr=2*model.x + model.y[1,1] == 1.0)
```

## func
```py
model.par_mat = Param(model.set_i, model.set_j, default=1) 
def con_rule(model):
    return summation(model.par_mat, model.x) <= 1
model.con = Constraint(rule=con_rule)
```

## using decoration func
```py
def con_eq_rule(model, i):
    if i == 0:
        return Constraint.Skip
    return model.x[i] - model.y[i] == model.val
model.con_eq = Constraint(model.I, rule = con_eq_rule)

@model.Constraint(model.set_i)
def con_eq(model, i):
    if i == 0:
        return Constraint.Skip
    return model.x[i] - model.y[i] == model.val
```

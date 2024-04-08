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

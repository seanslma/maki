# Var

## dynamic name
```py
setattr(m, 'x', pyo.Var(domain=pyo.Reals))
```

## single var
```py
model.x = Var(within=Reals, bounds=(0,6), initialize=1.5)
```

## multi-var
```py
def bounds(model, i, j):
   return (0, None)

model.set_i = Set(initialize = [i for i in range(3)])  
model.set_j = Set(initialize = [i for i in range(3)])  
model.y = Var(model.set_i, model.set_j, within=PositiveIntegers, bounds=bounds)
```

## init
```py
def init(model, i, j):
    return i+j
model.x = Var(model.set_i, model.set_j, initialize=2.0)
model.y = Var(model.set_i, model.set_j, initialize={(0,0):1.0, (2,2): 1.1})
model.z = Var(model.set_i, model.set_j, initialize=init)
```

## fix val
```py
model.x.fix(1)
```

## lb/ub
```py
model.x.lb = 0
model.x.ub = None
```

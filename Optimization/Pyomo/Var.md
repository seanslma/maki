# Var

## dynamic name
```py
setattr(m, 'x', pyo.Var(domain=pyo.Reals))
m.add_component('x', pyo.Var(domain=pyo.Reals))
```

## single var
```py
m.x = Var(within=Reals, bounds=(0,6), initialize=1.5)
```

## indexed var
```py
m.x = VarList(initialize=qw, bounds=(l,u))
for i in range(1):
    m.x.add()
#m.x[0], m.x[1] etc.
```

## multi-var
```py
def bounds(model, i, j):
   return (0, None)

m.set_i = Set(initialize = [i for i in range(3)])  
m.set_j = Set(initialize = [i for i in range(3)])  
m.y = Var(m.set_i, m.set_j, within=PositiveIntegers, bounds=bounds)
```

## init
```py
def init(m, i, j):
    return i + j
m.x = Var(m.set_i, m.set_j, initialize=2.0)
m.y = Var(m.set_i, m.set_j, initialize={(0,0):1.0, (2,2): 1.1})
m.z = Var(m.set_i, m.set_j, initialize=init)
```

## fix val
```py
m.x.fix(1)
```

## lb/ub
```py
m.x.lb = 0
m.x.ub = None
```

# Constraint

https://pyomo.readthedocs.io/en/stable/library_reference/kernel/constraint.html
```
classpyomo.core.kernel.constraint.constraint(expr=None, body=None, lb=None, ub=None, rhs=None)
```

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

## add a new term to existing con
https://groups.google.com/g/pyomo-forum/c/Abc3GuUSe88
```py
import pyomo.environ as pyo

# create model and var
m = pyo.ConcreteModel()
m.x = pyo.Var(within=pe.NonNegativeReals)

# create a con
@m.Constraint()
def con(m):
    return 2 <= m.x    
# m.con = pyo.Constraint(expr=m.x >= 2)
m.con.pprint()

# add a new term to con
m.con._body += m.x**2
m.con.pprint()
```

## create an empty constraint and then add terms
```py
import pyomo.environ as pyo

# create model and var
m = pyo.ConcreteModel()
m.x = pyo.Var(within=pe.NonNegativeReals)

# create a con: must use tuple not expr
@m.Constraint()
def con(m):
    return (0, 0, 10)     
# m.con = pyo.Constraint(expr=(0, 0, 10))
m.con.pprint()

# add a new term to con
m.con._body += m.x**2
m.con.pprint()
```

## add constraint name
https://groups.google.com/g/pyomo-forum/c/5DgnivI1JRY

Not good.
```py
m.c = pyo.Constraint(pyo.Any)
m.c[name1] = m.x + m.y == 1
m.c[name2] = …

solver.solve(m, symbolic_solver_labels=True)
```

Good solution
```py
setattr(m, 'con_1', pyo.Constraint(expr=(0, 0, 10)))
con = getattr(m, 'con_1')
con._body += m.x
con.pprint()
```

## change constraint lhs/rhs
https://stackoverflow.com/questions/74065872/pyomo-change-bounds-of-existing-contraints

use of a mutable Param to leave a placeholder in the expression tree
```py
m.con1_rhs = Param(mutable=True, initialize=3)
m.con1 = pyo.Constraint(m.x <= model.con1_rhs)

# then to change the RHS
m.con1.rhs.set_value(3.1)
```

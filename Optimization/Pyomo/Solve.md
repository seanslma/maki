# Solve

## solve
```py
model.dual = Suffix(direction=Suffix.IMPORT) # dual vars
grb = SolverFactory('gurobi')
sol = opt.solve(model)
```
## solution
```py
ind = []
var = []
val = []
for v in instance.component_objects(pyo.Var, active=True):
    name = v.getname()
    for index in v:
        ind.append(index if v.dim() > 0 else None)
        var.append(name)
        val.append(v[index].value)
sol = {'ind': ind, 'var': var, 'val': val}
```

## objective and dual
```py
obj_val = value(model.obj)
for con in model.cons:
    print(model.dual[model.cons[con]])
```

## solution status
```py
solution.solver.termination_condition # optimal, feasible, infeasible etc.
solution.solver.termination_message # str
solution.solver.status  # stattus: ok, warning, error, aborted, or unknown 
```

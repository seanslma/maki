# Performance
https://pascua.iit.comillas.edu/aramos/simio/transpa/s_GoodOptimizationModelingPracticesPyomo.pdf

## Threads
```py
solver.options['Threads'] = int(
    (psutil.cpu_count(logical=True) + psutil.cpu_count(logical=False))/2
)
```

## Sensitivity analysis with persistent solvers
Sequential resolution of similar problems in memory
```py
solver.remove_constraint(model.ConstraintName)
model.del_component(model.SetName)
solver.add_constraint(model.ConstraintName)
```

## Distributed computing
Create the problems and send them to be solved in parallel, and retrieve the solution once solved
```py
model.ConstraintName.deactivate()
model.del_component(model.SetName)
model.ConstraintName.activate()
```

## problem formulation performance
https://pianshen.com/ask/437410350304/

slow
```py
def flows(model, et, t):
    return pyo.quicksum(
        model.in_flow[:, et, t], 
        linear=True,
        start=pyo.quicksum(model.out_flow[:, et, t], linear=True)
    ) == 0
 
model.add_component(
    'flows', 
    pyo.Constraint(model.energy_type, model.t, rule=flows)
)
```

It turns out the problem was with the **slices** `[:, et, t]`:
```py
def flows(model, et, t):
    vars = [model.in_flow[obj, et, t] for obj in model.objects_index]
    vars.extend([model.out_flow[obj, et, t] for obj in model.objects_index])
    return pyo.quicksum(vars) == 0
```

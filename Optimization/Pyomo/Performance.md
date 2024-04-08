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

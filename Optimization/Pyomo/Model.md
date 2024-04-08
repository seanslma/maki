# Model

## write lp
```py
instance.write('model.lp', io_options={'symbolic_solver_labels': True})
```

## warm start
```py
instance = model.create()
instance.y[0] = 1
instance.y[1] = 0

with pyo.SolverFactory(
    'cplex',
    solver_io='python',
    manage_env=True,
    options=connection_params,
) as opt:
    results = opt.solve(instance, tee=True, warmstart=True)
```

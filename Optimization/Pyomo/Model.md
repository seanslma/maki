# Model

## write lp
```py
instance.write('model.lp', io_options={'symbolic_solver_labels': True})
```

## warm start
- `tee` Print the progress of the solver during optimizing.
- `logfile`: We can also write the log to a file.
- `timelimit`: The solver will stop after 600 seconds and keep the best solution.
```py
instance = model.create()
instance.y[0] = 1
instance.y[1] = 0

with pyo.SolverFactory(
    'cplex',
    solver_io='python',
    manage_env=True,
    options=connection_params,
) as cpx:
    cpx.options['LogFile'] = 'model.log'
    opt.options['TimeLimit'] = 600
    cpx.options['MIGap'] = 0.000001
    results = cpx.solve(instance, tee=True, warmstart=True)
```

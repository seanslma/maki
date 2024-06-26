# Terminate optimization

## callback code
https://www.gurobi.com/documentation/current/refman/cb_codes.html

## terminate optimization using callback
- https://support.gurobi.com/hc/en-us/community/posts/360071928312-Stopping-the-program-if-best-objective-has-not-changed-after-a-while
- https://support.gurobi.com/hc/en-us/articles/360047717291-How-do-I-use-callbacks-to-terminate-the-solver
```py
import time
import gurobipy as gp
from gurobipy import GRB

def cb(model, where):
    if where == GRB.Callback.MIPNODE:
        # Get model objective
        obj = model.cbGet(GRB.Callback.MIPNODE_OBJBST)

        # Has objective changed?
        if abs(obj - model._cur_obj) > 1e-8:
            # If so, update incumbent and time
            model._cur_obj = obj
            model._time = time.time()

    # Terminate if objective has not improved in 20s
    if time.time() - model._time > 20:
        model.terminate()

m = gp.Model()
```

## callback using pyomo
https://stackoverflow.com/questions/58200552/pyomo-and-gurobi-does-pyomo-support-solver-callbacks-to-gurobi
```py
def my_callback(cb_m, cb_opt, cb_where):
    if cb_where == GRB.Callback.MIPSOL:
        cb_opt.cbGetSolution(vars = [cb_m.x, cb_m.y])
        if cb_m.y.value < (cb_m.x.value - 2) ** 2 - 1e-6:
            print('adding cut')
            cb_opt.cbLazy(_add_cut(m.x.value))

def my_callback(cb_m, cb_opt, cb_where):
    if cb_where == GRB.Callback.MIP:
        # General MIP callback
        objbst = cb_opt.cbGet(GRB.Callback.MIP_OBJBST)
        objbnd = cb_opt.cbGet(GRB.Callback.MIP_OBJBND)
        if abs(objbst - objbnd) < cb_m.gaprel * (1.0 + abs(objbst)):
            print(f'Stop early - gap achieved: {cb_m.gaprel*100}%'))
            # cb_opt.terminate() # AttributeError: 'GurobiPersistent' object has no attribute 'terminate'
            cb_opt._solver_model.terminate()

opt = pe.SolverFactory('gurobi_persistent')
opt.set_instance(m)
opt.set_callback(my_callback)
solver.solve(tee=True)
```

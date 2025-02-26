# Matrix API

## example 
```py
import time
import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB

try:
    # Create a model
    model = gp.Model('gurobi_test')

    A = sp.diags([1,2,3]) # can also be a numpy 2d array

    X = model.addMVar(3)
    C = np.array([1,2,3])
    model.addConstr(A@X >= C)

    # m = 1024; n = 8192; d = 0.2
    # B = sp.random(m, n, d, format='csr')
    # b = np.random.rand(m)
    # C = np.random.rand(n)
    # t0 = time.time()
    # X = model.addMVar(n)
    # model.addConstr(B@X >= b) # a little slower
    # # model.addMConstr(B, X, '>', b)
    # print(f'time: {time.time() - t0:.3f}')

    Y = model.addMVar(3, name='y')
    D = np.array([3,4,6])
    model.addConstr(A@Y >= D)

    # # Create variables
    # x = model.addVar(vtype=GRB.CONTINUOUS, name='x', lb=0, ub=1)
    # y = model.addVar(vtype=GRB.BINARY, name='y')

    # Set objective function (minimize cx + dxy)
    model.setObjective(C@X + X@sp.diags(D)@Y, GRB.MINIMIZE)

    # # Add constraint: x + 2y >= 1
    # model.addConstr(x + 2 * y >= 1, 'c0')

    X.setAttr('VarName', [f'x[{i}]' for i in range(3)])
    model.write('c:/test/gurobi_test.lp')

    # Optimize the model
    model.optimize()

    # Check if the optimization was successful
    if model.status == GRB.OPTIMAL:
        model.write('c:/test/gurobi_test.sol')
        print('Model is optimal.')
        print(f'Objvalue: {model.objVal}')
        print(f'Solution: x = {X.x}, y = {Y.x}')
        
    elif model.status == GRB.INFEASIBLE:
        print('Model is infeasible.')
    elif model.status == GRB.UNBOUNDED:
        print('Model is unbounded.')
    else:
        print(f'Optimization ended with status {model.status}')

except gp.GurobiError as e:
    print(f'Gurobi error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
```

# Python API

## python api overview
https://docs.gurobi.com/projects/optimizer/en/current/reference/python/overview.html
- Most modifications to an existing model are done through the attribute interface (e.g., changes to variable bounds, constraint right-hand sides, etc.).
- The main exceptions are modifications to the constraint matrix (Model.chgCoeff) and to the objective function (build an expression and call Model.setObjective).


# Performance

## gurobi performance
https://support.gurobi.com/hc/en-us/articles/360013420111-How-do-I-improve-the-time-to-build-my-model
- try using `Model.addVars()` to create a sparse tupledict of variables, then use the select(), sum(), and prod() methods to iterate over only the matching variables
- it is more efficient to build a linear or quadratic expression by modifying an existing expression rather than repeatedly creating new expressions
- the `Model.addLConstr()` method is a slightly faster alternative to the more general `Model.addConstr()`. It can be up to 50% faster, particularly for very sparse constraints
- the Python Matrix API can be significantly faster than the traditional `Model.addConstr()` process

## Gurobi python matrix:
- https://cdn.gurobi.com/wp-content/uploads/gurobipy_matrixfriendly_webinar-slides.pdf
- python matrix api: https://support.gurobi.com/hc/en-us/sections/360009927292-Python-Matrix-API

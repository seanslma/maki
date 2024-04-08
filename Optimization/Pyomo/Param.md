# Param

## default
```py
model.set_i = Set(initialize = [i for i in range(3)])  
model.set_j = Set(initialize = [i for i in range(3)])
model.par_mat = Param(model.I, model.J, default=1) # a 4x4 matrix with initial values of 1
```

## init using dict
```py
data = {(0,0): 1, (1,2): 33, (2,1): 20}
model.par_mat = Param(model.set_i, model.set_j, initialize=data, default=0) # others are zeros
```

## init using func
```py
def init(model, i, j):
    return i*i if i == j else 0
model.par_mat = Param(model.set_i, model.set_j, initialize=c_init)
```

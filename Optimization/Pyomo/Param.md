# Param

## default
```py
model.set_i = Set(initialize = [i for i in range(3)])  
model.set_j = Set(initialize = [i for i in range(3)])
model.par_mat = Param(model.I, model.J, default=1) # a 4x4 matrix with initial values of 1
```

## init using dict
```py
# initialize value must be a dict or function
data = {(0,0): 1, (1,2): 33, (2,1): 20}
model.par_mat = Param(model.set_i, model.set_j, initialize=data, default=0) # others are zeros
```

## init using func
```py
def init(model, i, j):
    return i*i if i == j else 0
model.par_mat = Param(model.set_i, model.set_j, initialize=init)
```

## update values in mutable Param
```py
ind = ['x', 'y', 'z']
val = [100, 200, 300]
m.I = Set(initiliaze=ind)
m.p = Param(m.I, initialize=dict(zip(ind, val)), mutable=True)

# update one value
m.p['x'] = 0

# update mutiple values
m.p.set_value(**{'y': 400, 'z': 500})
```

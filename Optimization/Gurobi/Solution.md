# Solution

## get solution
```py
# Print the values of all variables
for v in model.getVars():
    print(f'{v.VarName} = {v.X}')

# Retrieve the values of multiple variables at once
vars = model.getVars()
values = model.getAttr('X', vars)
names = model.getAttr('VarName', vars)

for name, val in zip(names, values):
    print(f'{name:<10} {val}')
```

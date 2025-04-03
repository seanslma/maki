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
## example
```py
def solve(self):
    self.model.optimize()

    # Check if the optimization was successful
    if self.model.status == GRB.OPTIMAL:
        print('Model is optimal. Objective value: {self.model.objVal}')
    elif self.model.status == GRB.INFEASIBLE:
        print('Model is infeasible.')
    elif self.model.status == GRB.UNBOUNDED:
        print('Model is unbounded.')
    else:
        print(f'Optimization ended with status {self.model.status}')

def get_solution(self):
    # Retrieve the values of multiple variables at once
    vars = self.model.getVars()
    names = self.model.getAttr('VarName', vars)
    values = self.model.getAttr('X', vars)
    solution = pd.DataFrame({'col': names, 'val': values})
    return solution
```

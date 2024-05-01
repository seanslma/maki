# RangeSet
inmutable

## Basic
```py
model = pyo.ConcreteModel()
model.r1 = pyo.RangeSet(1, 3)      # {1,2,3}
model.r2 = pyo.RangeSet(3)         # {1,2,3}
model.r3 = pyo.RangeSet(1, 5, 2)   # {1,3,5}
model.r4 = pyo.RangeSet(5, 1, -2)  # {1,3,5}
model.r5 = pyo.RangeSet(0, 1, 0.5) # {0, .5, 1}
```

# RangeSet with Conditional Filtering
```py
def filter_rule(model, i):
    return i % 3 == 1
model.r6 = pyo.RangeSet(1, 5, filter=filter_rule) # {1,4}
```

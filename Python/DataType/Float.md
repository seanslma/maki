# Float

## ==
The default `x == y` is equivalent to `math.isclose(x, y, rel_tol=1e-16, abs_tol=0)`
- `1.0000000000000001 == 1` will return `True`
- `0 == 0.00000000000000000000000000000000000000001` will return `False`

## !=
https://www.quora.com/How-does-one-correctly-compare-two-floats-in-Python-to-test-if-they-are-equal

floating point operation can have up to a 1/2 bit rounding. The rounding is approximately:
`|real_value − rounded_value| <= real_value * epsilon / 2`
where epsilon depends on the underlying type of the floating point:
```py
import numpy as np 
epsilon= np.finfo(float).eps 

v = 10.0 
a = v / 77 
b = a * 77 
v != b # return True
abs(v - b) > max(abs(v), abs(b)) * epsilon # reture False
```

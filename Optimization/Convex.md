# Convex

## bilinear problem
- x * y
- e^x y + y
- sin(x  + y) - x^2
```
obj: x * y
var: x, y
```

### McCormick envelopes
The McCormick Envelope is a type of **convex relaxation** used for the optimization of bilinear non-linear programming (NLP) problems:
https://optimization.cbe.cornell.edu/index.php?title=McCormick_envelopes

## Convex-Concave Procedure (CCP)
If objective is not convex but can be expressed as `f_convex - g_convex`:
- Use first order Taylor approximation to replace g_convex
- So objective will become convex
- Run multiple iterations to converge to local minimum
- No guarantee for global minimum (maybe a big issue for some problems)

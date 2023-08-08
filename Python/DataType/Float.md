# Float

## ==
The default `x == y` is equivalent to `math.isclose(x, y, rel_tol=1e-16, abs_tol=0)`
- `1.0000000000000001 == 1` will return `True`
- `0 == 0.00000000000000000000000000000000000000001` will return `False`

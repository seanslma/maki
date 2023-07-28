# Int

## round up
https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number

```py
round(2.3) # 2.0
int(2.3 + .5) # 2

math.ceil(4.2) # return int (python3) or float (python2)?
np.ceil(2.3)
```

## float precision
```py
math.ceil(10000000 * 0.00136) # 13601.0 from 13600.000000000002
```

## `//` rounding down
`floor division` (also sometimes known as `integer division`). divide the first argument by the second and round the result down to the nearest whole number, equvalent to `math.floor`?
- if one of the operands is a float in floor division, then the output will be a float
```py
rounded_up = -(-numerator // denominator)
```

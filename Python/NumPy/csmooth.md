# csmooth

## interp
```py
from scipy import interpolate
fn = interpolate.interp1d(x, y, kind='cubic')
yn = fn(xn)
```

## smooth
```py
from csaps import csaps
smooth = 0.1
yn = csaps(x, y, xn, smooth=smooth)
```

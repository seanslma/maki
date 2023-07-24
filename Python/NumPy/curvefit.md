# curvefit

```py
import numpy as np
from scipy.optimize import curve_fit
curve_fit(f, x, y, p0, sigma=sigma, absolute_sigma=True, method='dogbox')
#p0 is inital value
#sigma is the inverse of weighting
minimize: chisq = sum((r / sigma) ** 2)
```

## polynomial
```py
polyfn = np.poly1d(np.polyfit(x, y, 4, w=np.square(y)))
y_new = polyfn(x_new)
```

## sigmoid
```py
def sigmoid(x, L, x0, k, b):
    y = L / (1 + np.exp(-k * (x - x0))) + b
    return y

p0 = [4*max(y), np.max(x), 1, min(y)] #this is an mandatory initial guess
popt, pcov = curve_fit(sigmoid, x, y, p0, method='dogbox', maxfev=1000)

x_new = list(range(x[-1]+1,x[-1]+21)
y_new = sigmoid(x_new, *popt)
```

## example
```py
from numpy import exp, loadtxt, pi, sqrt
from lmfit import Model
import matplotlib.pyplot as plt

data = loadtxt('model1d_gauss.dat')
x = data[:, 0]
y = data[:, 1]

def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))

gmodel = Model(gaussian)
result = gmodel.fit(y, x=x, amp=5, cen=5, wid=1)

print(result.fit_report())

plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--', label='initial fit')
plt.plot(x, result.best_fit, 'r-', label='best fit')
plt.legend(loc='best')
plt.show()
```

## funcs
```py
def fn_exp(x, b, x0):
    #y = e^(-b * (x-x0)
    #log(y) = -b*x + bx0
    #Y = Bx + A
    return np.exp(-b * (x-x0))
def p0_exp(x, y):
    coe = np.polyfit(x, np.log(y), 1, w=range(1,len(y)+1))
    b = -coe[0]
    x0 = coe[1] / b
    return [b, x0]
def fn_powlaw(x, a, b):
    #y = a * x^b
    #log(y) = log(a) + b*log(x)
    #Y = A + bX
    return a * np.power((x), b)
def p0_powlaw(x, y):
    coe = np.polyfit(np.log(x), np.log(y), 1, w=range(1,len(y)+1))
    a = np.exp(coe[1])
    b = coe[0]
    return [a, b]
```

# LinearFit

## linear fit must pass (x0, y0)
create a linear fit that must pass a specified point (x0, y0).
- shift the data points so that the desired point (x0, y0) becomes the new origin (0, 0)
- we only need to calculate the slope (linear regression), as the intercept of the line passing through the new origin is zero
- get the intercept using (x0, y0): `y - y0 = k (x - x0) => y = kx + (y0 - kx0)`
```py
import numpy as np
import matplotlib.pyplot as plt

def constrained_linear_fit(x, y, x0, y0):
    """
    Performs a linear fit (y = kx + b) that must pass through the point (x0, y0).

    Args:
        x: Array of x-values.
        y: Array of y-values.
        x0: x-coordinate of the point the line must pass through.
        y0: y-coordinate of the point the line must pass through.

    Returns:
        tuple: (slope, intercept) of the fitted line.
    """

    if len(x) != len(y):
        raise ValueError('x and y arrays must have the same length.')

    # Modified x and y values for fitting
    x_ = x - x0
    y_ = y - y0

    # Calculate the slope (k) using a simplified linear regression
    k = np.sum(x_ * y_) / np.sum(x_**2)

    # Calculate the intercept (b) using the constraint point
    b = y0 - k * x0

    return k, b

# Example Usage
x = np.array([-300, -150, 0, 150, 300])
y = np.array([450, 290, 250, 180, 120])
x0 = 0    # Desired x-coordinate
y0 = 250  # Desired y-coordinate

slope, intercept = constrained_linear_fit(x, y, x0, y0)
print(f'Slope (k): {slope}')
print(f'Intercept (b): {intercept}')

# Generate points for plotting the fitted line
x_fit = np.linspace(min(x) - 1, max(x) + 1, 100)
y_fit = slope * x_fit + intercept

# Plotting
plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='red', label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')
plt.scatter(x0, y0, color='green', label='Constraint Point')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Constrained Linear Fit')
plt.legend()
plt.grid(True)
plt.show()
```

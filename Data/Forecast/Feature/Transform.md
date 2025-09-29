# Transform

## random noise
- For small datasets, in order to avoid overfitting, random noise can be added to the values

## log transformation
In regression problems, when the target values have a large scale or skewed distribution, gradient descent optimization can be less stable or slower to converge due to large gradient magnitudes. To address this, taking the logarithm of the target values can help normalize the scale, reduce skewness, and improve optimization stability and speed.
- Reduces Skewness: It compresses the large values and spreads out the smaller values, making the distribution more symmetrical and closer to a normal distribution.
- Stabilizes Variance: It can help address heteroscedasticity, a situation where the variance of the errors is not constant across all levels of the independent variables.
- Taking the logarithm of targets is common when the target is strictly positive and has a heavy-tailed distribution (e.g., predicting prices, incomes).
- Gradient boosting algorithms cannot extrapolate

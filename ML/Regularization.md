# Regularization

Regularization is a process of introducing additional information in order to
solve an ill-posed problem or to prevent overfitting (Wikipedia Regularization).

Advantages for applying regularization to regression:
- Preventing overfitting
- Variable selection and removal of correlated variables
- Converting ill-posed problems to well-posed by adding additional information via penalty parameter lambda

Variable selection methods:
- Ridge method: shrink coefficients of correlated variables
- LASSO (Least Absolute Shrinkage and Selection Operator) method: pick one variable and discard the others
- Elastic Net Penalty: mixture of Ridge and LASSO methods

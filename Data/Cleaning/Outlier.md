# Outlier

check outlier by hisgram and scatter plot.

## stastical method
- Q1: first quartile, median of first part
- Q3: third quartile, median of second part

Minor outlier
- Lower bound: Q1 - (1.5 * (Q3-Q1))
- Upper bound: Q3 + (1.5 * (Q3-Q1))

Major outlier
- Lower bound: Q1 - (3 * (Q3-Q1))
- Upper bound: Q3 + (3 * (Q3-Q1))

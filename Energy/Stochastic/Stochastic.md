# Stochastic

## node/scenario based formulation
`node base` and `scenario based` formulated problems are equivalent to each other.
- `node based`: each node has a set of variables and constraints - no nonanticipativity constraints
- `scenario based`:each scenario has a set of variables and constraints - nonanticipativity constraints
- difference: `node based` removes the duplicate variables and constraints in the formulation
- difference: `scenario based` is straightforward and easy to implement


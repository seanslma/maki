# Install

## install gurobipy
```sh
conda search -c https://conda.anaconda.org/gurobi gurobi
conda install -c https://conda.anaconda.org/gurobi gurobi=12.0.1
```

## gurobi lp format using notepad++ regexp
requirements:
- add `\r\n` after `: `
- add `\r\n` before ` +,-,>=,<=,=`
- ignore `   +,-` etc.

solution:
- find: `(:\s)|(?<!\s{3})(\s[+\-<>=]=?)`
- repl: `(?1\1\r\n   )(?2\r\n  \2)`

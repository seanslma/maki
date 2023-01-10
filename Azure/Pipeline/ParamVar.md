<!-- {% raw %} -->
# Parameter and Variable
https://learn.microsoft.com/en-us/azure/devops/pipelines/security/inputs?view=azure-devops

## Parameters
- Pipeline parameters can't be changed by a pipeline while it's running.
- Parameters have data types such as number and string, and they can be restricted to a subset of values.
- The setup ensures that the pipeline won't take arbitrary data.

## Variables
https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch

In YAML pipelines, we can set variables at the root, stage, and job level.

- Variables can be a convenient way to collect information from the user up front.
- We can also use variables to pass data from step to step within a pipeline.
- Newly created variables are read-write by default.

```
variables:
  a: ${{ variables.var }} #evaluated when the YAML file is compiled into a plan
  b: $(var)               #evaluated at runtime before a task executes
  b: $[variables.var]     #evaluated at runtime
```

- compile-time expression `${{ <expression> }}`: have access to `parameters` and `statically defined variables`
- runtime expression `$[ <expression> ]`: have access to `more variables` but `no parameters`

<!-- {% endraw %} -->

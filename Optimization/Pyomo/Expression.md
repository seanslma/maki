# Expression

## examples
```py
model.expr = Expression(expr=model.x + 2 * model.y[1])

def expr_rule(model, i):
    if i == 1:
        return Expression.Skip
    return model.y[i]
model.expr = Expression(model.I, rule=expr_rule)
```

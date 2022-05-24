# Bind Variable

The limit of 1000 is on the constructor of the table type (and in clauses), but if you build-up the table you don’t need to worry about such limitation.

Use table bnind variable in `in clauses` to avoid the limit of 1000 elements:
https://cx-oracle.readthedocs.io/en/latest/user_guide/bind.html
```
type_obj = connection.gettype(f'{MatappSchemaName}.Table_Name')
obj = type_obj.newobject()
obj.extend(["Smith", "Taylor"])
```

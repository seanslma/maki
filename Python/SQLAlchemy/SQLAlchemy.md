# SQLAlchemy

## print query with binding values

sql.text
```
print(query.compile(dialect=None,compile_kwargs={'literal_binds': True}))
```

sql statement
```
print(query.statement.compile(dialect=None,compile_kwargs={'literal_binds': True}))
```

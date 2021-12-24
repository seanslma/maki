# SQLAlchemy

## print query with binding values
```
print(str(query.compile(dialect=None,compile_kwargs={'literal_binds': True})))
```

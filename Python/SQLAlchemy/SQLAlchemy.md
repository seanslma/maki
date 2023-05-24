# SQLAlchemy

## print query with binding values
sql.text
```
print(query.compile(dialect=None,compile_kwargs={'literal_binds': True}))
```

sql statement
```
print(query.statement.compile(dialect=None,compile_kwargs={'literal_binds': True}))
# mssql, mysql, oracle, postgresql, sqlite
print(query.statement.compile(dialect==sqlalchemy.dialects.mssql.dialect(),compile_kwargs={'literal_binds': True}))
```

## query template
```py
query = (
    session
    .query(
        t1.c1.label('a'),
        t2.c2.label('b'),
        case([
                (t3.c3 < (x or y), x),
            ], else_=t3.c3
        ).label('c')
    )
    .select_from(t1)
    .distinct()
    .join(t2, t3)
    .filter(
        t1.c2 == p1,
        t2.c1 == p2,
        *[...],
    )
)
```

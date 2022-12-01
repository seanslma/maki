# BindParam

## value
```py
    query = sql.text(f'''
        SELECT id, code
        FROM my_tbl
        WHERE id >= :id_min AND code = :code
    ''')
    query = query.bindparams(id=id, code=code)
    return read_sql(query, session=session)
```

## list
```py
query.bindparams(
    bindparam('lst', value=list(values), type_=String, expanding=True),
)
```

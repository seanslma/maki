# SQL

## read sql
For oracle db to get lowercase col names, use `as "col_name"`
```py
import sqlalchemy as sa
import get_database_config

cfg = get_database_config('my-config-file')
url = sa.engine.url.URL.create(**cfg)
engine = sa.create_engine(url)
session = sa.orm.Session(bind=engine)

query = """
    select SALEDATE, REGION, ID, QUANTITY
    from db.SALES
    where SALEDATE = TO_DATE(:date, 'YYYY-MM-DD HH24:MI:SS')
"""
data_schema = {
    'SALEDATE': pl.Datetime('ns'),
    'REGION': pl.Utf8,
    'ID': pl.Int32,
    'QUANTITY': pl.Float32,
}
df = pl.read_database(
    query=query,
    connection=engine, #or session.connection()
    schema_overrides=data_schema,
    execute_options={'parameters': {'date': '2025-05-29 12:00:00'}},
)
```

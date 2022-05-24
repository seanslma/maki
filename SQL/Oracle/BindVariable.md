# Bind Variable

The limit of 1000 is on the constructor of the table type (and in clauses), but if you build-up the table you don’t need to worry about such limitation.

Use table bnind variable in `in clauses` to avoid the limit of 1000 elements:
https://cx-oracle.readthedocs.io/en/latest/user_guide/bind.html
```
import cx_Oracle
def get_oracle_connection():
    cnx = cx_Oracle.connect(
        user='usr', password='pwd',
        dsn="svr.example.com",
        encoding="UTF-8",
    )
    return cnx

with get_oracle_connection() as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:p1, :p2)",
                   {'p1':1, 'p2':"Some string"))
    connection.commit()
    
#CREATE OR REPLACE TYPE name_array AS TABLE OF VARCHAR2(25);
type_obj = connection.gettype(f'{MatappSchemaName}.name_array')
obj = type_obj.newobject()
obj.extend(["Smith", "Taylor"])
```

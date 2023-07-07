## Sharding

### Sharding and Partitioning
used to increase the performance of the sql server by splitting the data into different subsets

<text>
Example python code about
how to insert records to a database table
</text>
```py
# connect
con = mdb.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + dbpath)
cursor = con.cursor()

# insert records
qry = 'INSERT INTO tbl ('
qry += ','.join(list(df.head(0))) + ') VALUES ('
qry += ','.join(np.repeat('?',df.shape[1])) + ')'
vals = list(df.itertuples(index=False, name=None))
cursor.executemany(qry, vals)
cursor.commit()

# close connection
cursor.close()
con.close()
```

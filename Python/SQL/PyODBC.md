# pyodbc

## faster way to insert data
https://stackoverflow.com/questions/48006551/speeding-up-pandas-dataframe-to-sql-with-fast-executemany-of-pyodbc

## fast_executemany
pyodbc needs string even for numerical data when `fast_executemany=True`

Insert or update dataframe into table
```py
# Convert numerical values to string
for col in upd_cols:
    df[col] = df[col].map('{:.4f}'.format, na_action='ignore')

# Standardize column names
id_cols = [f'[{c}]' for c in id_cols]
upd_cols = [f'[{c}]' for c in upd_cols]
cols = id_cols + upd_cols

# Command terms
stmt_on = ' AND '.join([f'T.{i} = S.{i}' for i in id_cols])
cols_upd = ','.join([f'T.{c} = S.{c}' for c in upd_cols])
cols_ins = ','.join(cols)
cols_val = ','.join([f'S.{c}' for c in cols])

# Create parameter indicators (?, ?, ..., ?) and parameter values
param_slots = ','.join(['?'] * df.shape[1])
param_values = df.to_records(index=False).tolist()

table_full_name = f'[{schema}].[{database}].[{table_name}]'
sql_stmt = f'''
    MERGE INTO {table_full_name} WITH (XLOCK, ROWLOCK) AS T
    USING (
        SELECT * FROM
        (VALUES ({param_slots})) AS Vtmp ({cols_ins})
    ) AS S
        ON {stmt_on}
    WHEN MATCHED THEN
        UPDATE SET {cols_upd}
    WHEN NOT MATCHED BY TARGET THEN
        INSERT ({cols_ins}) VALUES ({cols_val});
'''
# Create engine
url = sa.engine.url.URL.create(**cfg)
engine = sa.create_engine(url, **kwargs, fast_executemany=True)
# Merge df with table
with engine.begin() as cnn:
    cnn.execute(sql_stmt, param_values)
```

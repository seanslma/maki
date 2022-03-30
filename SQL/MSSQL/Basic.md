# Basic

## temporal table 
```sql
CREATE TABLE #tmp1 (id INT, name VARCHAR(25), value float)  
INSERT INTO #tmp1 VALUES (1, 'John', 1.1), (2, 'Ana', 2.2) 
SELECT * FROM #tmp1
DROP TABLE #tmp1
```

## json variable
```sql
DECLARE @json1 nvarchar(100)
SET @json1 = N'[{"a": "1"}, {"a": NULL}]'
```

## merge
```sql
MERGE INTO tbl as T
USING (
  SELECT * FROM 
       (VALUES (1, 2, 3), (2, 4, 5)) AS v 
       WITH (id, col1, col2)
) AS S
ON T.id=S.id
WHEN MATCHED THEN
  UPDATE SET 
    col_a=S.col_a, col_b=S.col_b
WHEN NOT MATCHED BY TARGET THEN
  INSERT (id, cola, colb) 
  VALUES (S.id, S.cola, S.colb)  
WHEN NOT MATCHED BY SOURCE THEN
  DELTE
;
```
```python
def upsert_data(
    df : pd.DataFrame,
    table_name : str,
    id_cols: Set[str],
    connection_url: str,
) -> None:
    engine = create_engine(connection_url, fast_executemany=True)

    # Command terms
    cols = df.columns.tolist()
    stmt_on = ' AND '.join([f'T.{i} = S.{i}' for i in id_cols])
    cols_upd = ','.join([f'T.{c} = S.{c}' for c in cols if c not in id_cols])
    cols_ins = ','.join(cols)
    cols_val = ','.join([f'S.{c}' for c in cols])

    # fill `NULL` values with None
    def fill_null(val: list) -> list:
        def is_null(v):
            return isinstance(v, type(pd.NA)) or (v in ['NULL', np.nan, ''])
        return tuple(None if is_null(v) else v for v in val)

    # create parameter indicators (?, ?, ..., ?) and parameter values
    param_slots = ','.join(['?'] * df.shape[1])
    param_values = [fill_null(row.tolist()) for _, row in df.iterrows()]

    cmd = f'''
        MERGE INTO {table_name} WITH (XLOCK, ROWLOCK) AS T
        USING (
            SELECT * FROM
            (VALUES ({param_slots})) WITH ({cols_ins})
        ) AS S
            ON {stmt_on}
        WHEN MATCHED THEN
            UPDATE SET {cols_upd}
        WHEN NOT MATCHED BY TARGET THEN
            INSERT ({cols_ins}) VALUES ({cols_val})
        ;
        '''

    # merge df with table
    with engine.begin() as cnn:
        cnn.execute(cmd, param_values)
```

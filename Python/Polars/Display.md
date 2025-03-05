# Display

## show all rows and columns
if n < 0 (eg: -1), display all rows/columns
```py
with pl.Config(tbl_rows=-1, tbl_cols=-1):
    print(df)
``` 

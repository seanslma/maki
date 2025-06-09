# Config

## polars print config
when print df align numerical cols right
- `pl.Config.set_tbl_cell_numeric_alignment('RIGHT')`

numer of lines to show:
- `pl.Config.set_tbl_rows(20)` # number of rows in print

## show all rows and columns
if n < 0 (eg: -1), display all rows/columns
```py
with pl.Config(tbl_rows=-1, tbl_cols=-1):
    print(df)
``` 

# Excel

## read excel into dataframe options
https://stackoverflow.com/questions/28766133/faster-way-to-read-excel-files-to-pandas-dataframe

## compare different options
- https://www.linkedin.com/pulse/reading-xlsx-files-quickly-python-amged-elsheikh-su7ic
- https://hakibenita.com/fast-excel-python

## read excel using the light-fast calamine engine
polars is using fastexcel.

Calamine is a Rust library designed specifically for reading Excel and OpenDocument Spreadsheet files. It focuses on extracting data from these file formats, not modifying them.

install calamine
```sh
pip install fastexcel
mamba install python-calamine -y
```

polars: read excel sheet
```py
import polars as pl

dl = pl.read_excel(
    xlfl,
    sheet_name=wsnm[0],
    engine='calamine',
    read_options={'header_row': 3},
)
dl[:2]
```

The `read_options` is from `fastexcel`: https://fastexcel.toucantoco.dev/fastexcel.html
- `idx_or_name`: The index (starting at 0) or the name of the sheet to load.
- `column_names`: Overrides headers found in the document.
  If column_names is used, header_row will be ignored.
- `header_row`: The index of the row containing the column labels, default index is 0
  If None, the sheet does not have any column labels.
- `skip_rows`: Specifies how many rows should be skipped after the header.
  If header_row is None, it skips the number of rows from the start of the sheet.
- `n_rows`: Specifies how many rows should be loaded. If None, all rows are loaded
- `schema_sample_rows`: Specifies how many rows should be used to determine the dtype of a column. If None, all rows will be used.
- `use_columns`: Specifies the columns to use. Can either be:
    - None to select all columns
    - A list of strings and ints, the column names and/or indices (starting at 0)
    - A string, a comma separated list of Excel column letters and column ranges (e.g. “A:E” or “A,C,E:F”, which would result in A,B,C,D,E and A,C,E,F)
- `dtypes`: An optional dict of dtypes. Keys can be column indices or names



pandas: read excel sheet
```py
import pandas as pd

dp = pd.read_excel(
    xlfl,
    sheet_name=wsnm[0],
    engine='calamine',
    dtype_backend='pyarrow',
    skiprows=3,
    skipfooter=0,
)
dp[:2]
```

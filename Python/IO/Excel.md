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
    read_options={'header_row': 3},
    engine='calamine',
)
dl[:2]
```

pandas: read excel sheet
```py
import pandas as pd

dp = pd.read_excel(
    xlfl,
    sheet_name=wsnm[0],
    skiprows=3,
    skipfooter=0,
    engine='calamine',
    dtype_backend='pyarrow',
)
dp[:2]
```

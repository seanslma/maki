# pdf2tbl

## pdfplumber
pdfplumber: extract text and tables from pdf files

settings\\
https://github.com/jsvine/pdfplumber#extracting-tables

examples\\
https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/extract-table-nics.ipynb

```py
pdf = pdfplumber.open(file_input)
pg = pdf.pages[34]
#pg.to_image()

table_settings = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
    "intersection_x_tolerance": 15,
    "intersection_y_tolerance": 15,
    "snap_tolerance": 10,
    "edge_min_length":3
}
tbls = pg.extract_tables(table_settings)

lines = pg.extract_text().splitlines()

#seems the settings only works for first table
tbs = page.find_tables(table_settings)
height = min(page.height, tb.bbox[3])
tp = page.within_bbox((0, tb.bbox[1], page.width, height))
ts = tp.find_tables(table_settings)
if len(ts) == 0:
    continue
tl = ts[0].extract(x_tolerance=5, y_tolerance=5)
th = list(filter(None, tl[0])) #remove empty items
```

## camelot

camelot: extract tables from pdf files. also works for scanned files. cannot get page text

#install Ghostscript from: https://www.ghostscript.com/download/gsdnld.html\\
#pip install "camelot-py[cv]"

```py
tbls = camelot.read_pdf(file_input, pages='all', process_background=True)
for tbl in tbls:
    df = tbl.df
    print(f'Page: {tbl.page}')
    print(df.head(3))
    print('\n')
```

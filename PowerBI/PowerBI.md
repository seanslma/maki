# PowerBI

## table
```
Table.Combine({tbl1, tbl2})
Table.PromoteHeaders(Source, [PromoteAllScalars=true])
Table.RemoveColumns(Source,{"Col1", "Col2", "Col3"})
Table.AddColumn(Source, "ColNew", each Date.AddDays([LASTUPDATE],3))
Table.RenameColumns(Source,{{"Col1", "Region"}, {"Col2", "Zone"}})
Table.TransformColumnTypes(Source, {{"Col1", type datetime}, {"Col2", date},
  {"Col3", Int64.Type}, {"Col4", type number}, {"Col5", type text}})
Table.SelectColumns(Source,{"Col1"})

Table.Distinct(SelectedCols)
Table.SplitColumn(Source, "Col", Splitter.SplitTextByDelimiter("_",
  QuoteStyle.Csv), {"C1", "C2", "C3"})
```

## load csv
```
Source = Csv.Document(File.Contents(data_path & "file.csv"),
  [Delimiter=",", Columns=11, Encoding=1252, QuoteStyle=QuoteStyle.None]),
PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
ChangedType = Table.TransformColumnTypes(PromotedHeaders,
  {{"C1", type datetime}, {"C2", Int64.Type}}),
ChangedType2 = Table.TransformColumnTypes(ChangedType, {{"Period", type datetime}}, "en-AU")
```

## load sql
```
src = MySQL.Database("host:port", "db", [ReturnSingleDatabase=true,
   Query="select c1,c2 from tb limit 3;", CommandTimeout=#duration(0, 1, 40, 0)])

src = MySQL.Database("host:port", "db", [ReturnSingleDatabase=true]),
dbt = src{[Schema="db",Item="tb"]}[Data]
```


## run python
```
PySource = Python.Execute("from pathlib import Path#(lf)import pandas as pd#(lf)dataset = pd.DataFrame([[str(Path.home())]], columns = [1])"),
homeDir = Text.Trim(Lines.ToText(PySource{[Name="dataset"]}[Value][1])),
```

## named range
```
FolderPath= Excel.CurrentWorkbook(){[Name="NamedRange"]}[Content]{0}[Column1],
```

## Power Query Errors: Please Rebuild This Data Combination
https://www.excelguru.ca/blog/2015/03/11/power-query-errors-please-rebuild-this-data-combination/

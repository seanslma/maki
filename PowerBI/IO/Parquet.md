## parquet

## get parquet files from web api
https://community.fabric.microsoft.com/t5/Power-Query/Using-the-function-Web-Contents-with-more-than-2-options/td-p/1566974
```fs
let
  // URL of the Parquet file
  Source = Binary.Buffer(Web.Contents(
    "YOUR URL", [
      Headers = [#"Authorization"="Static Token Example",#"Content-Type"="application/json"]
    ]
  )),
  // Load the Parquet file into a table
  Table = Parquet.Document(Source)
in
  Table
```

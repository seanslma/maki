# Parquet

## Apache Arrow

## Read csv to parquet
```cs
using Apache.Arrow;

var schema = new Schema.Builder()
    .Field("id", ArrowTypeId.Int32)
    .Field("name", ArrowTypeId.String)
    .Field("age", ArrowTypeId.Int32)
    .Build();

using (var csvDataReader = new CsvDataReader("path/to/csv/file.csv", Encoding.UTF8, schema))
using (var parquetWriter = new ParquetWriter("path/to/parquet/file.parquet", schema) {
    parquetWriter.WriteTable(Table.FromReader(csvDataReader));
}
```

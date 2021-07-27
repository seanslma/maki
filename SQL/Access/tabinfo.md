# table

## C#
```csharp
var conStr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + "database.mdb";
var con = new OleDbConnection(conStr);
con.Open();

DataTable dataTable = con.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, new object[] { null, null, null, "TABLE" });
int numTables = dataTable.Rows.Count;
for (int tableIndex = 0; tableIndex < numTables; ++tableIndex) {
    String tableName = dataTable.Rows[tableIndex]["TABLE_NAME"].ToString();
    DataTable schemaTable = con.GetOleDbSchemaTable(OleDbSchemaGuid.Columns, new object[] { null, null, tableName, null });
    foreach (DataRow row in schemaTable.Rows) {
        String fieldName = row["COLUMN_NAME"].ToString(); //3
        String fieldType = row["DATA_TYPE"].ToString(); // 11
        String fieldDescription = row["DESCRIPTION"].ToString(); //27
    }
}
```

## create table
```sql
CREATE TABLE [tn](
   [Auto]                  COUNTER
  ,[Byte]                  BYTE
  ,[Integer]               SMALLINT
  ,[Long]                  INTEGER
  ,[Single]                REAL
  ,[Double]                FLOAT
  ,[Decimal]               DECIMAL(18,5)
  ,[Currency]              MONEY
  ,[ShortText]             CHAR
  ,[LongText]              MEMO
  ,[PlaceHolder1]          MEMO
  ,[DateTime]              DATETIME
  ,[YesNo]                 BIT
  ,[OleObject]             IMAGE
  ,[ReplicationID]         UNIQUEIDENTIFIER
  ,[Required]              INTEGER NOT NULL
  ,[Unicode Compression]   MEMO WITH COMP
  ,[Indexed]               INTEGER
  ,CONSTRAINT [PrimaryKey] PRIMARY KEY ([Auto])
  ,CONSTRAINT [Unique Index] UNIQUE ([Byte],[Integer],[Long])
);
CREATE INDEX [Single-Field Index] ON [tn]([Indexed]);
CREATE INDEX [Multi-Field Index] ON [tn]([Auto],[Required]);
CREATE INDEX [IgnoreNulls Index] ON [tn]([Single],[Double]) WITH IGNORE NULL;
CREATE UNIQUE INDEX [Combined Index] ON [tn]([ShortText],[LongText]) WITH IGNORE NULL;

create table [mlf_gen] (
  Generator char(255), Voltage_kV char(8), DUID char(50), ConnectionPoint_ID char(50), 
  TNI_code char(50), MLF_2021_22 float, Region char(3)
);

ALTER TABLE [aemo_mlf_2022_gen] 
  ADD CONSTRAINT PK_mlf_gen PRIMARY KEY ([Generator],[ConnectionPoint_ID]);
CREATE INDEX [Single-Field Index] ON [mlf_gen]([DUID]);
CREATE UNIQUE INDEX [Combined Index] ON [mlf_gen]([Generator],[ConnectionPoint_ID]) WITH IGNORE NULL;
```
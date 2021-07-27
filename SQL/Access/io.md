# io

## ImportExportSpecification
without specify the 'Width', the fields will be alphabetically ordered.

if there are no indexed fields, PrimaryKey should be 'Auto', otherwise it should be 'key1 key2 ...'

note that 'AppendToTable' rather than 'Destination' should be used.
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ImportExportSpecification Path="C:\Users\Public\zzz.csv" xmlns="urn:www.microsoft.com/office/access/imexspec">
    <ImportText TextFormat="Delimited" FirstRowHasNames="false" FieldDelimiter="," TextDelimiter="" CodePage="437" AppendToTable="MyNewTable">
        <DateFormat DateOrder="YMD" DateDelimiter="-" TimeDelimiter=":" FourYearDates="true" DatesLeadingZeros="false"/>
        <NumberFormat DecimalSymbol="."/>
        <Columns PrimaryKey="{Auto}">
            <Column Name="Col1" FieldName="id" Indexed="YESDUPLICATES" SkipColumn="false" DataType="Long" Width="2"/>
            <Column Name="Col2" FieldName="textfield" Indexed="NO" SkipColumn="false" DataType="YesNo" Width="1"/>
        </Columns>
    </ImportText>
</ImportExportSpecification>
```

## load csv file to db table

# Table Functions
data types: INt64.Type, type text, type logical, type datetime

## SelectColumns
Table.SelectColumns(Data, {"Date", "Value"})

## AddColumn
Table.AddColumn(Data, "YearMonth", each Date.Year([Date])*100+Date.Month([Date]), Int64.Type)

Table.AddColumn(Data, "FinYear", each 
  if Date.Month([Date]) >= 7 then Date.Year([Date]) + "-" + Text.End(Text.From(Date.Year([Date]) + 1), 2) 
  else (Date.Year([Date]) - 1) + "-" + Text.End(Text.From(Date.Year([Date])), 2), type text
)

## RemoveColumns
Table.RemoveColumns(Data,{"Id", "Period", "Version")

## RenameColumns
Table.RenameColumns(Data, {{"TypeId","Id"}, {"CountryName", "Country"}})

## TransformColumns
Table.TransformColumns(Data, {"Date", each Date.AddDays(_,1), type datetime})

## UnpivotOtherColumns
Table.UnpivotOtherColumns(Data, {"Date", "Year", "Quarter", "Type"}, "Attribute", "Value")

## SelectRows
Table.SelectRows(Data, each [Date] > RangeStart and [Date] <= RangeEnd)

# Table Functions

## SelectColumns
Table.SelectColumns(Data, {"Date", "Value"})

## AddColumn
Table.AddColumn(Data, "YearMonth", each Date.Year([Date])*100+Date.Month([Date]), Int64.Type)

Table.AddColumn(Data, "FinYear", each 
  if Date.Month([Date]) >= 7 then Date.Year([Date]) + "-" + Text.End(Text.From(Date.Year([Date]) + 1), 2) 
  else (Date.Year([Date]) - 1) + "-" + Text.End(Text.From(Date.Year([Date])), 2), text
)

## RemoveColumns
Table.RemoveColumns(Data,{"Id", "Period", "Version")

## RenameColumns
Table.RenameColumns(Data, {{"TypeId","Id"}, {"CountryName", "Country"}})

## TransformColumns
Table.TransformColumns(Data, {"Date", each Date.AddDays(_,1), type datetime})

## SelectRows
Table.SelectRows(Data, each [Date] > RangeStart and [Date] <= RangeEnd)

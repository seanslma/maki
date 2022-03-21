# Formatting

## conditional formatting
```
Sub Formatting()
  Set RngTable1 = Range(“A1:A10”)
  RngTable1.FormatConditions.Delete
  RngTable1.FormatConditions.Add Type:=xlCellValue, Operator:=xlBetween, _
        Formula1:="=100", Formula2:="=200"
  RngTable1.FormatConditions(1).Interior.Color = RGB(255, 0, 0)
End Sub
```
## color scale 2
```
Sub CondFmt_ColourScales2()
    Dim rg As Range: Set rg = Range("F5:I5")
    rg.FormatConditions.Delete
    
    'colour scale will have 2 colours
    Dim cs As ColorScale: Set cs = rg.FormatConditions.AddColorScale(ColorScaleType:=2)
    With cs
        'the first colour is white
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(255, 255, 255)
            .Type = xlConditionValueLowestValue
        End With
        
        'the third colour is red
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 0, 0)
            .Type = xlConditionValueHighestValue
        End With
    End With
End Sub
```

## color scale 3
```
Sub CondFmt_ColourScales3()
    Dim rg As Range: Set rg = Range("F5:I5")
    rg.FormatConditions.Delete
    
    'colour scale will have 3 colours
    Dim cs As ColorScale: Set cs = rg.FormatConditions.AddColorScale(ColorScaleType:=3)
    With cs
        'colour 1 is blue
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(102, 153, 255)
            .Type = xlConditionValueLowestValue
        End With
        
        'colour 2 is yellow set at value 50
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 230, 153)
            .Type = xlConditionValueNumber
            .Value = 50
        End With
        
        'colour 3 is red
        With .ColorScaleCriteria(3)
            .FormatColor.Color = RGB(255, 0, 0)
            .Type = xlConditionValueHighestValue
        End With
    End With
End Sub
```

# Formatting
https://docs.microsoft.com/en-us/office/vba/api/excel.databar.showvalue

## cell chars font size
```VB
With Sheets("Test").Range("A1")
    .Value = "Abc" & Chr(10) & "123" #new line
    .Characters(Start:=3, Length:=4).Font.Size = 6
End With
```

## cell formatting color
Get cell conditional formatting background color:
```vb
Function BgHexColor(rng As Range)
    i = rng.DisplayFormat.Interior.Color 'ColorIndex
    r = (i Mod 256)
    g = (i \ 256) Mod 256
    b = (i \ 256 \ 256) Mod 256
    
    BgHexColor = "#" & Format(Hex(r), "00") & Format(Hex(g), "00") & Format(Hex(b), "00")
End Function
```

## color scale 2
```VB
Sub CondFmt_ColorScales2()
    Dim rg As Range: Set rg = Range("F5:I5")
    rg.FormatConditions.Delete
    
    'color scale will have 2 colors
    Dim cs As ColorScale: Set cs = rg.FormatConditions.AddColorScale(ColorScaleType:=2)
    With cs
        'the first color is white
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(255, 255, 255)
            .Type = xlConditionValueLowestValue
        End With
        
        'the third color is red
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 0, 0)
            .Type = xlConditionValueHighestValue
        End With
    End With
End Sub
```

## color scale 3
```VB
Sub CondFmt_ColorScales3()
    Dim rg As Range: Set rg = Range("F5:I5")
    rg.FormatConditions.Delete
    
    'color scale will have 3 colors
    Dim cs As ColorScale: Set cs = rg.FormatConditions.AddColorScale(ColorScaleType:=3)
    With cs
        'color 1 is blue
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(102, 153, 255)
            .Type = xlConditionValueLowestValue
        End With
        
        'color 2 is yellow set at value 50
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 230, 153)
            .Type = xlConditionValueNumber
            .Value = 50
        End With
        
        'color 3 is red
        With .ColorScaleCriteria(3)
            .FormatColor.Color = RGB(255, 0, 0)
            .Type = xlConditionValueHighestValue
        End With
    End With
End Sub
```

## data bar
```VB
Sub CondFmt_DataBar()
    Dim rg As Range: Set rg = Range("E30:E44")
    rg.FormatConditions.Delete
    
    Dim db As Databar: Set db = rg.FormatConditions.AddDatabar
    With db
        .ShowValue = False
        
        'positive bar with green gradient & green border
        .BarColor.Color = RGB(0, 176, 80)
        .BarFillType = xlDataBarFillGradient
        .BarBorder.Type = xlDataBarBorderSolid
        .BarBorder.Color.Color = RGB(0, 176, 80)
        
        'the axis positioned automatically and coloured black
        .AxisPosition = xlDataBarAxisAutomatic
        .AxisColor.Color = vbBalck
        
        'negative bar with a red gradient & red border
        With .NegativeBarFormat
            .ColorType = xlDataBarColor
            .Color.Color = RGB(255, 0, 0)
            .BorderColorType = xlDataBarColor
            .BorderColor.Color = vbRed 'RGB(255, 0, 0)
        End With
    End With

End Sub
```

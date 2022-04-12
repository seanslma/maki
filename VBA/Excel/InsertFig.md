# Insert Fig


## insert
```vb
Sub InsertPicture(rng As Range, picpath As String)
    Dim pic As Shape ' -1 means original size for width and height
    Set pic = rng.Parent.Shapes.AddPicture(filename:=imgpath, LinkToFile:=msoFalse, SaveWithDocument:=msoTrue, Left:=rng.Left, Top:=rng.Top, Width:=-1, Height:=-1)
End Sub
```

## delete
```vb
Sub DeletePictures()
    Dim pic As Picture
    For Each pic In ThisWorkbook.ActiveSheet.Pictures
       pic.Delete
    Next
End Sub
```

# array

You can only redim the last dimension of a multi dimension array

## check error value
  TypeName(val) = "Error"

## check array empty
  IsEmpty(arr) 'only works for Variant


## check variant array element
(Not arr(i, j)) = -1 'not empty, arr(i,j) can be an array

when get the value of a range, we do not know it is a value or an array, we should use
```vba
dim val as variant
dim val_tmp as variant
val_tmp = worksheets("x").range("a3").value
val_tmp = worksheets("x").range("a3:a4").value
if vardim(val) > 0 then
  val = val_tmp
else
  redim val (1 to 1, 1 to 1)
  val(1,1) = val_tmp
end if 
``` 

then we need to check the dimension of the val,using 

```vba
Function VarDim(var As Variant) As Long
On Error GoTo Err
    Dim i As Long
    Dim tmp As Long
    i = 0
    Do While True
        i = i + 1
        tmp = UBound(var, i)
    Loop
Err:
    VarDim = i - 1
End Function
``` 
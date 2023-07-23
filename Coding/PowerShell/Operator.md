# Operator

## Logical and comparison operators
```ps1
-and, -or, -not, -xor
-band, -bor, -bxor #bitwise operator
-eq, -ne, -gt, -lt, -ge, -le, -like, -notlike
#all string comparisons are case insensitive by default
-ceq, -cne, -clike #add a “c” after the dash in the operator to enable case-sensitive
-ieq, -ine, -ilike #add an “i” after the dash in the operator to enable case-insensitive
–contains, –notcontains, -in,-notin
```

## Arithmetic operators
```ps1
+, -, /, *, %, ++, --, +=, -=, /+, *=

#js like converting
$s = "5"
$n = 5
$s + $n #"55"
$n + $s #10
"xy " * 2 #"xy xy "
```

## String and array manipulation operators
```ps1
–replace #"SERVER-DC2" -replace "DC","FILE", output:SERVER-FILE2
–split #"one,two,three" -split ",", 2, output: one\ntwo,three
–join
```

## Object type operators
```ps1
-is, -isnot #"world" -is [string], output:True
–as #attempt to convert an object of one type into another type, "55.2" -as [int]
250MB+1GB #output: 1335885824 bytes
```

## Format operator
```ps1
"Name is {0}; Pi is {1:N}; Today is {2:yyyy-MM-dd}" -f (Get-Content Env:\USERNAME), [math]::pi, (Get-Date)
#output: Name is Admin; Pi is 3.14; Todat is 2021-10-05
```

## Call and subexpression operators
```ps1
$cmd = "dir"
&cmd #run dir command
$service = Get-Service | select -first 1
"Service name is $($service.name)"
```

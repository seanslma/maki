# FileSys

## Get filename from path
```
$filename = Split-Path $filepath -leaf
```

## Join path and filename
```
$filepath = Join-Path -Path "$dir" -ChildPath "$filename"
```

## File without extension
```
$filename_without_ext = $file.Substring(0, $file.LastIndexOf('.'))
```

## Check file exists or not
```
if (Test-Path -Path "$filepath" -PathType "Leaf") {}
```

## List subfolder size
```
Get-ChildItem -force 'C:\Users\sma' -ErrorAction SilentlyContinue | ? { $_ -is [io.directoryinfo] } | % {
    $len = 0
    Get-ChildItem -recurse -force $_.fullname -ErrorAction SilentlyContinue | % { $len += $_.length }
     '{0,10:N3} MB  {1}' -f ($len / 1Mb), $_.fullname
}
```

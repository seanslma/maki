# FileSys

## List subfolder size
```
Get-ChildItem -force 'C:\Users\sma' -ErrorAction SilentlyContinue | ? { $_ -is [io.directoryinfo] } | % {
    $len = 0
    Get-ChildItem -recurse -force $_.fullname -ErrorAction SilentlyContinue | % { $len += $_.length }
     '{0,10:N3} MB  {1}' -f ($len / 1Mb), $_.fullname
}
```

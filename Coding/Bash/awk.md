# awk

## select table rows based on columns
Regex patterns should be put in `//` and not quoted
```
#MaxDataDiskCount MemoryInMb Name NumberOfCores OsDiskSizeInMb ResourceDiskSizeInMb
az vm list-sizes --location "australiaeast" -o table \
  | awk '(($3 == "Name" || $3 ~ /^Standard_DS/) \
      && ($2 == "MemoryInMb" || $2 >= 32000) \
      && ($4 == "NumberOfCores" || ($4 >= 4 && $4 <= 20)))'
```

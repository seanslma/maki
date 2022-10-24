# awk

## read awk command from file
```
awk -f func.awk
```

## print selected fields
- `$0` is for the entire line
- `NF` number of fields
```
awk '{print $1}'      #select 1st field
awk '{print $1, $NF}' #select 1st and last fields
```

## reverse words in line
```
awk '{for (i=NF; i>=0; i--) {printf "%s ", $i;} printf "\n"}'
```

## sum of a field
- `END` will only execute once
- `/^total/{next}` exclude first line starts with `total`
```
ls -l | awk '/^total/{next} {sum += $5}; END {print sum}'
```

## group another field by one field
- delimiter is space
- awk `associate array` is a dictionary
- `NF > 8` only when the number of fields > 8
```
awk -F" " 'NF > 8 {v[$1] += $2}; END {for (k in v) {printf "%s:%d\n", k, v[k]}}'
```

## select table rows based on columns
Regex patterns should be put in `//` and not quoted
```
#MaxDataDiskCount MemoryInMb Name NumberOfCores OsDiskSizeInMb ResourceDiskSizeInMb
az vm list-sizes --location "australiaeast" -o table \
  | awk '(($3 == "Name" || $3 ~ /^Standard_DS/) \
      && ($2 == "MemoryInMb" || $2 >= 32000) \
      && ($4 == "NumberOfCores" || ($4 >= 4 && $4 <= 20)))'
```

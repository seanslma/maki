# awk

## read awk command from file
```sh
awk -f func.awk
```

## print selected fields
- `$0` is for the entire line
- `NF` number of fields
```sh
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
```sh
ls -l | awk '/^total/{next} {sum += $5}; END {print sum}'
```

## group another field by one field
- delimiter is space
- awk `associate array` is a dictionary
- `NF > 8` only when the number of fields > 8
```sh
awk -F" " 'NF > 8 {v[$1] += $2}; END {for (k in v) {printf "%s:%d\n", k, v[k]}}'
```

## select table rows based on columns
Regex patterns should be put in `//` and not quoted. Include the header as well.
```sh
#MaxDataDiskCount MemoryInMb Name NumberOfCores OsDiskSizeInMb ResourceDiskSizeInMb
az vm list-sizes --location "australiaeast" -o table \
  | awk '(($3 == "Name" || $3 ~ /^Standard_DS/) \
      && ($2 == "MemoryInMb" || $2 >= 32000) \
      && ($4 == "NumberOfCores" || ($4 >= 4 && $4 <= 20)))'
```

**Convert string to number**
input: path_to_my_file.txt
```
NAME                    CPU(cores)   MEMORY(bytes)
dev-dashboard-6570x79   2m           533Mi
dev-task-734449-2h882   1096m        4442Mi
dev-task-734449-d5k9m   1m           4531Mi
dev-task-734449-d996d   37m          6232Mi
```
code: select names starting with `dev-task` and cpu > 1000m. `$2 + 0` will convert string to number.
```sh
pods_to_delete=$(kubectl top po -n dev \
| awk '$1 ~ /^dev-task/ && $2 ~ /m/ { sub("m", "", $2); if ($2 + 0 > 1000) print $1 }')

# test
awk '$1 ~ /^dev-task/ && $2 ~ /m/ { sub("m", "", $2); if ($2 + 0 > 1000) print $1 }' "path_to_my_file.txt"
```

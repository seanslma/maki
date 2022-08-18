# Split large file

## Git Bash
```
cd /c//tmp
split file.csv -b 500m
split file.csv file -b 500m -a 3 -d
split file.csv file -l 1000 -a 3 -d
```

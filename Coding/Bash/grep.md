# grep

## search in files
```
grep error *.log                #list files and lines with `error`
grep error ../tst/*.log */*.log #from multiple folders
grep -h error *.log             #exclude filenames
grep -c error *.log             #count matches in each file (include zero match)
grep -l error *.log             #list files with matches
grep -i error *.log             #case insensitive search
grep -v error *.log             #exclude lines with `error`
grep '[0-9]\{4\}-\{0,1\}[0-9]\{2\}-\{0,1\}[0-9]\{2\}' file #find a date
```

## delete files with matches (confirm before delete)
search all files in the current folder, not subfolders
```
rm -i $(grep -l 'debug' * )
```

## switch based on match
if multiple files provided, stop search after found 1st
```
if grep -q error tst.log ; then
    echo "found"
else
    echo "not found"
fi
```

search all files
```
if grep error tst.log > /dev/null ; then
    echo "found"
else
    echo "not found"
fi
```

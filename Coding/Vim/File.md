# file

## save and quit
```
esc -> back to command mode
:w  -> save to file
:q! -> quit
ZZ  -> save and quit
```

## 5.2 write file
```
:w filename   -> write current file to filename
:!rm filename -> delete file filename
:w            -> :'<,'>w filename, write selection to file
```

## 5.4 merge files
```
:r filename   -> write file to line below
:r !ls        -> read output of ls and put it below
```

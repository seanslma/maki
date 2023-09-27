# file

## save and quit
```
esc  -> back to command mode
:w   -> save to file
:q!  -> quit
:wq! -> save and quit
ZZ   -> save and quit
```

## 5.2 write file
```
:w filename   -> write current file to filename
:w            -> :'<,'>w filename, write selection to file
:!rm filename -> delete file filename
```

## 5.4 merge files
```
:r filename   -> read file to line below
:r !ls        -> read output of ls and put it below
```

# Search and replace

## 4.2 search
```
/text  -> search for text in the document, going forward
?text  -> search for text in the document, going backwards
n      -> move the cursor to the next instance
N      -> move the cursor to the previous instance
CTRL-O -> go back
CTRL-I -> go forward
```

## 4.3 match
```
% ->find a matching ), ], or }
```

## 4.4 substitute
```
:s/old/new      -> substitute first 'new' for 'old' in the line
:s/old/new/g    -> substitute all 'new' for 'old' in the line
:#,#s/old/new/g -> substitute between line# and line#
:8,9s/old/new/g ->replace all in line 8 to line 9
:%s/old/new/g   -> substitute all in the file
:%s/old/new/gc  -> substitute all in the file with confirmation
replace with foo (y/n/a/q/l/^E/^Y)? #q-quit, l-stop, ^e-scroll up, ^y down
```

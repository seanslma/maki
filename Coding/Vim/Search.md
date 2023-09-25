# Search and replace

## search and replace
```
/text search for text in the document, going forward
n move the cursor to the next instance.
N move the cursor to the previous instance
?text search for text in the document, going backwards

:s/a/a_text/ #only replace the first in current line
:s/a/a_text/g #replace all in current line
:8,10 s/a/a_text/g #replace all in line 8 to line 10
:%s/a/a_text/g #entire file
:%s/a/a_text/gc #entire file and confirm before replacing
replace with foo (y/n/a/q/l/^E/^Y)? #q-quit, l-stop, ^e-scroll up, ^y down
```

## 4.2 search
```
/ ->forward direction
? ->backward direction
n ->next one
N ->previous one
CTRL-O ->go back
CTRL-I ->go forward
```

## 4.3 match
```
% ->find a matching ), ], or }
```

## 4.4 substitute
```
:s/old/new   ->substitute first 'new' for 'old' in the line
:s/old/new/g ->substitute all 'new' for 'old' in the line
:#,#s/old/new/g ->substitute between line# and line#
:%s/old/new/g   ->substitute all in the file
:%s/old/new/gc  ->substitute all in the file with confirmation
```

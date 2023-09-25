# vim



## vi
```
esc  -> back to command mode
o    -> create a line below and insert
O    -> create a line above and insert
i    -> insert characters before cursor
I    -> insert characters at line front
a    -> append characters after cursor
A    -> append characters at line end
r    -> replace character
R    -> replace more than one character from the cursor
x    -> delete character
:q!  -> force quit without change
:wq! -> force save and quit

u    -> undo the last change
2u   -> undo the two last changes
U    -> undo a whole line
-r   -> redo the last undo
^R   -> redo (undo the undo's)
```

## change
```
ce  -> delete to word end and insert
c2w -> delete to 3rd word front and insert
c3e
c0
c$
```

### 5.1 execute command
  :!cmd ->execute cmd
  :!ls  ->execute ls

### 5.2 write file
```
:w filename   -> write current file to filename
:!rm filename -> delete file filename
:w            -> :'<,'>w filename, write selection to file
```

### 5.4 merge files
  :r filename ->write file to line below
  :r !ls      ->read output of ls and put it below

### 6.5 set option
:set ic     ->ignore case
:set noic   ->disable ignoring case
:set hls is ->highlight search and incremental search
:nohlsearch ->remove highligting of searches
/ignore\c   ->ignore case only in current search
:set number ->line number
:set nonumber

### 7.1 online help
<F1> key
:help
CTRL-W CTRL-W   ->to jump from one window to another
:q              ->close help window
:help w
:help c_CTRL-D
:help insert-index
:help user-manual

### 7.2 startup script
  <F1> key

## book
Vim - Vi Improved - by Steve Oualline
Learning the Vi Editor - by Linda Lamb



### save and quit
```
esc -> back to command mode
:w  -> save to file
:q! -> quit
ZZ  -> save and quit
```

### syntax highlight
put it in .vimrc
  :sy enable
  :syn enable
  :syntax enable

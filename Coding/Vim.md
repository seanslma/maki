# vim

## paste from clipboad
Keep source format
```
:set paste   #before
:set nopaste #after
```

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

## Move
Here’s a handy tip: prefacing a movement command with a number will execute that movement multiple times. So, if you want to move up six lines, enter 6k and Vim will move the cursor up six lines. If you want to move over five words, enter 5w. To move 10 words back, use 10b.

### char
```
<h jv k^ l>
h -> left
l -> right
k -> up
j -> down
```

### word
```
w  -> move forward one word
b  -> move backward one word
de -> move to end of current word
2w -> move to start of 2ed word
3e -> move to end of 3ed word
```

### line
```
0  -> moves to the beginning of the line
^  -> first non empty of the line
$  -> moves to the end of the line
```

### file
```
gg -> move to the beginning of the file
G  -> move to the end of the file
#G -> move to line#
`. -> move to the last edit
^G ->cursor location and file status
```

## change
```
ce  -> delete to word end and insert
c2w -> delete to 3rd word front and insert
c3e
c0
c$
```

## copy and paste
```
v  -> highlight one character at a time
V  -> highlight one line at a time
^v -> highlight by columns
y  -> yank text into the copy buffer (copy)
yw -> copy one word without v
yy -> copy current line without v
p  -> paste text after the current line
P  -> paste text on the current line
```

### 4.2 search
  / ->forward direction
  ? ->backward direction
  n ->next one
  N ->previous one
  CTRL-O ->go back
  CTRL-I ->go forward

### 4.3 match
  % ->find a matching ), ], or }

### 4.4 substitute
  :s/old/new   ->substitute first 'new' for 'old' in the line
  :s/old/new/g ->substitute all 'new' for 'old' in the line
  :#,#s/old/new/g ->substitute between line# and line#
  :%s/old/new/g   ->substitute all in the file
  :%s/old/new/gc  ->substitute all in the file with confirmation

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

### Searching and Replacing
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

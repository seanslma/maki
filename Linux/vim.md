# vim

## vi
```
esc #back to command mode
i #insert characters
I #to left and insert characters
a #append characters
A #to right and append characters
r #replace character
x #delete character
:q! #force quit
:wq! #force save and quit
```

## vimtutor
From the commandline you'll get "a 30 minute tutorial that teaches the most basic Vim functionality hands-on" as it calls itself.

### 1.1 moving
```
h ->left
l ->right
k ->up
j ->down
```

### 1.2 exit
```
:q! ->exit without change
 ```
 
### 1.3 delete
```
x ->delete a character
```

### 1.4 insert
```
i ->insert before cursor
I ->insert at line front
```

### 1.5 append
```
a ->insert after cursor
A ->insert at line end
```

### 1.6 save
```
:wq  ->save and exit
```

### 2.1 delete
```
dw -> delete until start of next word
```

### 2.2 delete
```
d0 -> delete to line front
d$ -> delete to line end  
```

### 2.3 motion
  de -> move to end of current word  

### 2.4 count
  2w -> move to start of 2ed word  
  3e -> move to end of 3ed word

### 2.5 count delete
  d2w -> delete until start of 2ed word  

### 2.6 line
  dd -> delete current line 
  2dd -> delete 2 lines
  
### 2.7 undo
  u ->undo last commands
  U ->undo a whole line 
  CTRL-R ->redo (undo the undo's) 
        
### 3.1 put
  p ->insert delete after cursor                

### 3.2 replace
  r ->replace one character 
  
### 3.3 change
  ce ->delete to word end and insert
  
### 3.4 more change
  c2w ->delete to 3rd word front and insert 
  c3e
  c0
  c$     

### 4.1 location
  gg ->move start of file
  G  ->move bottom of file
  #G ->move to line#
  CTRL-G ->cursor location and file status

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
  :w filename   ->write current file to filename
  :!rm filename ->delete file filename
  
### 5.3 write selection
  v  ->select text
  :w ->:'<,'>w filename, write selection to file
  
### 5.4 merge files
  :r filename ->write file to line below
  :r !ls      ->read output of ls and put it below
  
### 6.1 open
  o ->create a line below and insert
  O ->create a line above and insert

### 6.2 append
  a ->insert text after the cursor
  A ->insert text after the line

### 6.3 replace
  R ->replace more than one character from the cursor
  
### 6.4 copy and paste
v ->highlight
y ->copy
p ->paste
yw->copy one word without v
  
### 6.5 set option
:set ic     ->ignore case
:set noic   ->disable ignoring case
:set hls is ->highlight search and incremental search
:nohlsearch ->remove highligting of searches 
/ignore\c   ->ignore case only in current search
  
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
    
### Moving
h moves the cursor one character to the left.
j moves the cursor down one line.
k moves the cursor up one line.
l moves the cursor one character to the right.
0 moves the cursor to the beginning of the line.
$ moves the cursor to the end of the line.
w move forward one word.
b move backward one word.
G move to the end of the file.
gg move to the beginning of the file.
`. move to the last edit.

Here’s a handy tip: prefacing a movement command with a number will execute that movement multiple times. So, if you want to move up six lines, enter 6k and Vim will move the cursor up six lines. If you want to move over five words, enter 5w. To move 10 words back, use 10b.

### Editing
x delete the current character
d starts the delete operation
dw will delete a word
d0 will delete to the beginning of a line
d$ will delete to the end of a line
dgg will delete to the beginning of the file
dG will delete to the end of the file
u will undo the last operation
Ctrl-r will redo the last undo

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

### Copying and Pasting
    v highlight one character at a time
    V highlight one line at a time
    Ctrl-v highlight by columns
    p paste text after the current line
    P paste text on the current line
    y yank text into the copy buffer
    
### Saving and Quitting =====
    esc back to command mode
    :w save file
    :w filename save to the file
    :q! quit
    ZZ save and quit

### syntax highlighting =====
put it in .vimrc
  :sy enable
  :syn enable
  :syntax enable

# Change

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
```

## indentation
- Press `V` to start selecting in block mode
- Move cursor to select more lines
- `<` or `>` to de-indent or indent the selected rows

## set tabwidth in `.vimrc`
```
set expandtab      " Use spaces instead of tabs
set tabstop=2      " Set the width of a tab to 2 spaces
set shiftwidth=2   " Amount to indent when using `>` or `<` commands
```

## undo
```
u    -> undo the last change
2u   -> undo the two last changes
U    -> undo a whole line
-r   -> redo the last undo
^R   -> redo (undo the undo's)
```

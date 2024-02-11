# Shortcuts

## select current word
```
Ctrl + D
Ctrl + Shift + Arrow #select more
```

## select current line
```
Ctrl + L
```
When using `Ctrl + C` without any selection the line where the cursor is will be copied.

## copy line without newline
option 1:
- Got to Settings
- Search for "Editor: Copy with Syntax Highlighter" and uncheck it

option 2: using `macros`
- install extensions `macros`
- create a macro by adding it to `settings.json`
  ```
  "macros.list": {
      "copyWithoutNewLine": [
          "cursorHome",
          "cursorEndSelect",
          "editor.action.clipboardCopyAction",
          "cancelSelection",
          "cursorUndo",
          "cursorUndo",
          "cursorUndo"
      ]
  }
  ```
- add the macro to `keybindings.json`
  ```
  {
      "key": "ctrl+alt+c",
      "command": "macros.copyWithoutNewLine",
      "when": "editorTextFocus && !editorHasSelection"
  }
  ```

## delete line
```
Ctrl  + Shift + K
```

## insert line
```
Ctrl + Enter          #insert below
Ctrl + Shift + Enter  #insert above
```

## comment/uncomment code
```
Ctrl + /
```

## column selection
```
Ctrl + Shift + Alt + Down/Up/left/Right/PageUp/PageDown
```

## go to line
```
Home     #beginning of line
End      #end of line
Ctrl + G #go to line
```

## go to error
```
F8         #next error/warning
Shift + F8 #previous error/warning
```

## new terminal window
```
Ctrl + J
```

## folding
mouse over the class or function, the folding arrows will be shown.
- `Ctl + Shft + [`: Fold the innermost uncollapsed region at the cursor
- `Ctl + Shft + ]`: unfolds the collapsed region at the cursor
- `Ctl + K, Ctl + 0`: folds all regions in the editor. `Ctrl+K, Ctrl+[n]` where n is the level number upto which to fold
- `Ctl + K, Ctl + J`: unfolds all regions in the editor.

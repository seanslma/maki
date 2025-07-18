# Shortcuts

## open command palette
```
Ctrl + Shift + P
```
Then search for what you need

## open `keybindings.json`
This file contains your custom keybindings. I
- Open the Command Palette by pressing `Ctrl + Shift + P`
- Type `Open Keyboard Shortcuts (JSON)` and select the corresponding command

## search text
```
Ctrl + F         # search in the current file
Ctrl + Shift + F # search in all files
```

## select current word
```
Ctrl + D
Ctrl + Shift + Arrow # select more
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

## cut line
```
Ctrl + X
```

## delete line
```
Ctrl + Shift + K
```

## insert line
```
Ctrl + Enter          #insert below
Ctrl + Shift + Enter  #insert above
```

## move/copy
```
Alt + Up/Down         # Move line up/down
Shift + Alt + Up/Down # Copy line up/down
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
- `Ctrl + Shift + [`: Fold the innermost uncollapsed region at the cursor
- `Ctrl + Shift + ]`: unfolds the collapsed region at the cursor
- `Ctrl + K, Ctrl + 0`: folds all regions in the editor. `Ctrl+K, Ctrl+[n]` where n is the level number upto which to fold
- `Ctrl + K, Ctrl + J`: unfolds all regions in the editor.

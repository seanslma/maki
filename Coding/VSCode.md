# VS Code

## Settings
Customizing IntelliSense:
https://code.visualstudio.com/docs/editor/intellisense

## Editor font size and line space
settings > editor > line height > 15
```
"editor.fontSize": 13,
"editor.lineHeight": 13,
```

## Debug console font size and line space
```
"debug.console.fontSize": 13,
"debug.console.lineHeight": 10,
```

## Terminal font size
Line height can't be scaled smaller than 1
```
"terminal.integrated.fontSize": 12,
```
## Trim trailing whitespaces
user settings > Trim Trailing Whitespace
```
"files.trimTrailingWhitespace": true,
```

## New line at EOF
File > Preference > Settings (^,) > 'insert final newline'
```
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
```

## Wrap line
workspace > settings.json
```
"editor.rulers": [80, 120],
"editor.wordWrap": "wordWrapColumn",
"editor.wordWrapColumn": 80,
"[markdown]": {
    "editor.wordWrap": "wordWrapColumn",
}
```

## Vertical rulers
`^,` user > settings.json > search for `ruler`
```
{
    "editor.rulers": [80, 120],
    "workbench.colorCustomizations": {
        "editorRuler.foreground": "#4e525042"
    },
}
```

## Active tab settings
Search "workbench.action.openSettingsJson" > Open user settings.json
```
"editor.rulers": [80,120],
"workbench.colorCustomizations": {
    "editorRuler.foreground": "#312f30",
    "tab.inactiveForeground":"#ECECEC",
    "tab.activeBackground": "#8f6155",
    "tab.activeBorderTop": "#007acc",
    "tab.activeBorder": "#ff0000",
    "tab.unfocusedActiveBorder": "#000000"
},
```

# Config

## Settings
Customizing IntelliSense:
https://code.visualstudio.com/docs/editor/intellisense

## user vs workspace settings
Note: the workspace settings will overwrite the user settings

## Hide title bar
In user settings, add
```json
"window.titleBarStyle": "custom",
```

## Editor font size and line space
settings > editor > line height > 15
```json
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

## terminal line number
Default is 1000
```json
"terminal.integrated.scrollback": 5000,
```

## New line at EOF
File > Preference > Settings (^,) > 'insert final newline'
```json
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
```

## Trim trailing whitespaces
user settings > Trim Trailing Whitespace
```json
"files.trimTrailingWhitespace": true,
```

## Wrap line
workspace > settings.json
```json
"editor.rulers": [80, 88, 120],
"editor.wordWrap": "wordWrapColumn",
"editor.wordWrapColumn": 120,
"[markdown]": {
    "editor.wordWrap": "wordWrapColumn",
    "editor.wordWrapColumn": 120
}
```

## Vertical rulers
`^,` user > settings.json > search for `ruler`
```json
"editor.minimap.enabled": false,
"editor.rulers": [80,88],
"workbench.colorCustomizations": {
    "editorRuler.foreground": "#333333",
    "tab.activeBorderTop": "#066794",
    "tab.unfocusedActiveBorder": "#000000"
},
```

## Active tab settings
Search "workbench.action.openSettingsJson" > Open user settings.json
```json
"editor.rulers": [80,88],
"workbench.colorCustomizations": {
    "editorRuler.foreground": "#312f30",
    "tab.inactiveForeground":"#ECECEC",
    "tab.activeBackground": "#8f6155",
    "tab.activeBorderTop": "#007acc",
    "tab.activeBorder": "#ff0000",
    "tab.unfocusedActiveBorder": "#000000"
},
```

## Copy relative filepath separator setting
Search `Explorer: Copy Relative Path Separator` in settings

## Auto closing quotes/brackets
```json
"editor.autoClosingQuotes": "never",
"editor.autoClosingBrackets": "never",
```    

## disable spell check in problems
in `settings.json` add:
```json
"cSpell.diagnosticLevel": "Hint",
```
For version >= 4.0, a better solution:
```json
"cSpell.useCustomDecorations": true,
"cSpell.textDecoration": "underline wavy #bbbbbb66", //"underline wavy #fc9867 auto", //
```

## disable inline values in debugger
It's annoying that Python debugger in VS Code is showing inline variable values (faded text next to your code while debugging)
```json
"debug.inlineValues": false
```

## dockerfile
mark files with some extension as docker file
```json
{
  "files.associations": {
        "*.docker": "dockerfile"
    }
}
```

# VS Code

## Settings
Customizing IntelliSense:
https://code.visualstudio.com/docs/editor/intellisense

## Line space
settings > editor > line height > 15

## Trim trailing whitespaces
user settings > Trim Trailing Whitespace

## New line at EOF
File > Preference > Settings (^,) > 'insert final newline'

## Wrap line
workspace > settings.json
```
{
    "editor.rulers": [80, 120],
    "editor.wordWrap": "wordWrapColumn",
    "editor.wordWrapColumn": 80,
    "[markdown]": {
        "editor.wordWrap": "wordWrapColumn",
    }
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
{
    "editor.rulers": [80,120],
    "workbench.colorCustomizations": {
        "editorRuler.foreground": "#312f30",
        "tab.inactiveForeground":"#ECECEC",
        "tab.activeBackground": "#8f6155",
        "tab.activeBorderTop": "#007acc",
        "tab.activeBorder": "#ff0000",
        "tab.unfocusedActiveBorder": "#000000"
    },
}
```

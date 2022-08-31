# VS Code

## Line space
settings > editor > line height > 15

## Settings
Customizing IntelliSense: 
https://code.visualstudio.com/docs/editor/intellisense

## Wrap line
settings.json
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

# Notepad++

## shortcut keys
- `Ctrl + L` cut current line
  
## select column to file end
- use the Begin/End Select feature on the Edit menu [select start]
- Alt + Left Click to select end line and column
- use the Begin/End Select feature on the Edit menu [select end]

## regex
### replace empty lines
```
type ^\R ( for exact empty lines) or
^\h*\R ( for empty lines with blanks, only).
Leave the Replace with zone empty.
```

### replace float
```
(\d+(\.\d+)?) -> ,\1,
```

### match commas
```
^[^,\n]*((,[^,\n]*){3}$)
#matches a single comma followed by zero or more
#  characters that are not comma or newline 3 times
(,[^,\n]*){3}
```

### match lines start-end with
```
<\!\-\-(.*?)\-\->
start((.|\n|\r|\r\n)*?)end
start(((.|\n|\r|\r\n)(?!start))*?)end #correct

start((.|\n|\r|\r\n)(?!end))*?V056(.|\n|\r|\r\n)*?end
#(.|\n|\r|\r\n) means "any char (new line included)"
#(?!end) means "not followed by end"
#*? means "match as short as possible" (while * means "match as long as possible")
```

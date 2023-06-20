# Click

## return value using click
https://stackoverflow.com/questions/26246824/how-do-i-return-a-value-when-click-option-is-used-to-pass-a-command-line-argume

Use `standalone_mode=False`:
```
print(main(standalone_mode=False))
```

## Multiple Values from Environment Values
https://click.palletsprojects.com/en/7.x/options/

- The default implementation for all types is to split on `whitespace`
- The exceptions to this rule are the `File` and `Path` types: Unix systems `colon` (:), and Windows `semicolon` (;)

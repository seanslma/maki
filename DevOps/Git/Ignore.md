# Ignore

## rules
https://git-scm.com/docs/gitignore

## list ignored files
only for tracked files
```sh
git status --ignored
```

## list all ignored files
https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore
```
find . -not -path './.git/*' | git check-ignore --stdin    #list files only
find . -not -path './.git/*' | git check-ignore --stdin -v #include ignore rules
git check-ignore *       #does not work
git check-ignore **/*    #does not work
```

## debug gitignore
https://git-scm.com/docs/git-check-ignore

check why file (not) ignored
```sh
git check-ignore --verbose ignored.file #git check-ignore -v ignored.file
```

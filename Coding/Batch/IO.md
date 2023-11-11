# IO

## read first line
limits:
- max line length of 1021 bytes, not including EOL
- file must use Windows style EOL of CarriageReturn LineFeed
- trailing control characters will be stripped from the line

```bat
set /p line=< file.txt
echo %line%
echo %line:~3% ::skip first 3 characters
```

## read from second line
```bat
@echo off
setlocal EnableDelayedExpansion

set file=myfile.txt
set curdir=%~dp0

set /p line1=< %file%

set i=0
echo %date% %time% ln: %line1%
for /f %%a in (%file%) do (
    set /a i=!i!+1
    if !i! GTR 1 (
        echo !date! !time!  !i! ln: %%a
    )
)

echo %date% %time% all done!
```

## read csv
```bat
:readcsv
    set i=0
    for /f "usebackq tokens=1-2 delims=," %%a in ("file.csv") do (
        set /a i=!i!+1
        if !i! GTR 1 exit /b
        echo %%a %%b
    )
    exit /b
```

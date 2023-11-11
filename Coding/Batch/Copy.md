# copy

```bat
@echo off

set file="SampleFile.csv"
set desdir=

If not exist %file% (
    echo Error: Input file does not exist %file%
    goto TheEnd
)

if "%desdir%"=="" (
    Set desdir=%~dp0
)
echo Source file: %file%
echo Destination dir: %desdir%
echo.

REM type for filename with spaces
for /f "delims=" %%a in ('type %file%') do (
    If not exist %%a (
        echo Error: File does not exist "%%a"
        goto TheEnd
    )
    echo f | xcopy "%%a" "%desdir%/%%~nxa" /Y /I /Q > nul
    echo Copied file: %%~nxa
)

:TheEnd
echo.
echo all done!
```

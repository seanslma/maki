# service

## change service log on
Change service from 'Local System' account and 'Network Service', you need to clear the password and when you click apply it will fill the password automatically

## service control
```bat
@echo off
@echo off

SET username=xxx@svr.com
SET password=xxx

set test_dir=client_test
set test_log_dir=client_test_logs

for /f %%a in (list.txt) do (
    echo ''''%%a
    net use "\\%%a" %password% /user:%username%
    ping /n 1 /w 1500 %%a | (findstr /r /c:"[0-9]*ms" > nul)
    if %errorlevel% neq 0 (
        echo NOT EXIST: %%a
    ) else (
        if "%1"=="copy" (
            xcopy %test_dir% \\%%a\c$\%test_dir%\ /i /s /e /y
        ) else if "%1"=="install" (
            sc \\%%a create MyService binpath= \\%%a\c$\%test_dir%\myservice.exe
        ) else if "%1"=="start" (
            sc \\%%a start MyService
        ) else if "%1"=="stop" (
            sc \\%%a stop MyService
        ) else if "%1"=="uninstall" (
            sc \\%%a delete MyService
        ) else if "%1"=="delete" (
            rmdir /s /q \\%%a\c$\%test_dir%
        ) else if "%1"=="query" (
            sc \\%%a query MyService
        ) else if "%1"=="copylog" (
            copy /y \\%%a\c$\%test_dir%\test.log %test_log_dir%\log_%%a.log
        ) else if "%1"=="rmlog" (
            rmdir /s /q \\%%a\c$\%test_dir%\test.log
        ) else (
            REM default case...
        )
    )
    net use "\\%%a" /delete
)

echo all done!
```

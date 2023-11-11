# cmd
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy

## read 4 cols of csv
```bat
for /f "usebackq tokens=1-4 delims=," %%a in ("file.csv") do (
    echo %%a %%b %%c %%d
)
```

## input parameter
```bat
set inp=x
IF [%1]==[] (
  set inp=s
)
```

## if else
  python --version >nul 2>&1 && ( python test.py ) || ( py test.py )

## list all files in a folder
  dir /b         #include folders
  dir /b /a-d    #exclude folders
  dir /b /a-d /s #exclude folders but include files in folders
  dir /b /a-d | findstr /I /R "^xyz*.pdf"

## output to console and file
  run.bat >run.log | type run.log
  run.bat | findstr /R "^xyz???.*" >> run.log 2>&1

## ouput taskmgr to csv file
  tasklist /FO csv > "%userprofile%\desktop\tasks.csv"
## rename all files in a folder
```bat
rem in cmd replace %% with %
for /f "tokens=*" %%a in ('dir /b') do ren "%%a" "00_%%a"

for %%f in (*.csv) do rename "%%f" "%%~nf_old.csv"

rem cmd
for %f in (*.csv) do rename "%f" "%~nf_old.csv"
```

## kill task
```bat
tasklist | findstr /I /c:"mysql"
tasklist /v | findstr /I /c:"mysql"

taskkill /F /PID pid_number
taskkill /F /IM "process name"
start explorer
```

## delete recycle bin data
```bat
rd /s c:\$Recycle.Bin
```

## delete hidden file on shared drive
```bat
rem show hidden files
dir "networkdrive" /A:H /B
rem delete hidden file
del /A:H "hiddenfile"
```

## disk performance check
```bat
winsat disk -drive g
```

## change path
  setx path "%path%;C:\yourFolder"
Windows resource kit tools 'pathman.exe':
  pathman /au c:\Programs\Python35 #add a path
  pathman /ru c:\Programs\Python35 #del a path

## escape "
use "" to represent "

## change service account
```bat
SC.EXE CONFIG MyServiceName obj= "Local Service" password= ""
```

## Parallel run from cmd
```bat
rem %~dp0 is the bat file path
start "" %~dp0\%dir%1\My.exe 1
start "" %~dp0\%dir%2\My.exe 2
start "" %~dp0\%dir%3\My.exe 3
```

## event
https://www.petri.com/managing-command-line-event-logs\\
wevtutil epl nam c:\machine.svr.com.evt /r:machine.svr.com /u:<user_name> /p:<password>

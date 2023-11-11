## other

```bat
rem Output file names in dir to file
dir /b > f.txt

rem Get the bat file path
set bat_dir=%~dp0

rem Get the bat file directory and join with file name
set file_path="%~dp0Test.py"

rem Get the first parameter, the file path
set workbook="%~1"

rem Use a variable
echo %file_path%

rem get filename from path
Use %~nxf for <filename>.<extension>

rem check remote logged user
query user /server:machine.svr.com
wmic.exe /node:"machine.svr.com" computersystem get username

rem check methods from dll, open VS console prompt
dumpbin /exports "C:\xx\yy.dll"

rem Kill a process by name
taskkill /f /im My.exe

rem Find a specific task
tasklist |find /i "chrome"

rem Move files
robocopy "C:\src_dir" "C:\des_dir" /move

rem Delete files
del "C:\my_dir\*.*"
```

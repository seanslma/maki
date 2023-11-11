# time

```bat
for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined MyDate set MyDate=%%x
for /f %%x in ('wmic path win32_localtime get /format:list ^| findstr "="') do set %%x
set fmonth=00%Month%
set fday=00%Day%
set today=%Year%%fmonth:~-2%%fday:~-2%
```

```bat
@echo off
set day=0
echo >"%temp%\%~n0.vbs" s=DateAdd("d",%day%,now) : d=weekday(s)
echo>>"%temp%\%~n0.vbs" WScript.Echo year(s)^& right(100+month(s)-1,2)^& right(100+day(s),2)
for /f %%a in ('cscript /nologo "%temp%\%~n0.vbs"') do set "result=%%a"
del "%temp%\%~n0.vbs"
set "YYYY=%result:~0,4%"
set "MM=%result:~4,2%"
set "DD=%result:~6,2%"
if "%MM%"=="00" set "MM=12" & set /a YYYY=YYYY-1
set "data=%yyyy%%mm%"

echo last year/month was "%data%"
pause
```

## date
```bat
@echo off

set _date=""
call:isodtfunc _date
echo %_date%
goto:eof

:isodtfunc
:: use wmic to retrieve date and time
for /f "skip=1 tokens=1-6" %%g in ('wmic path win32_localtime get day^,hour^,minute^,month^,second^,year /format:table') do (
  if "%%~l"=="" goto s_done
  set _yyyy=%%l
  set _mm=00%%j
  set _dd=00%%g
  set _hour=00%%h
  set _minute=00%%i
)
:s_done

:: pad digits with leading zeros
set _mm=%_mm:~-2%
set _dd=%_dd:~-2%
set _hour=%_hour:~-2%
set _minute=%_minute:~-2%

:: display the date/time
set %~1=%_yyyy%%_mm%%_dd%%_hour%%_minute%
goto:eof

:datefunc
setlocal
rem use findstr to strip blank lines from wmic output
for /f "usebackq skip=1 tokens=1-3" %%g in (`wmic path win32_localtime get day^,month^,year ^| findstr /r /v "^$"`) do (
  set _day=00%%g
  set _month=00%%h
  set _year=%%i
)
rem pad day and month with leading zeros
set _day=%_day:~-2%
set _month=%_month:~-2%
rem output format required is yyyy-mm-dd
set %~1=%_year%-%_month%-%_day%
endlocal
goto:eof
```

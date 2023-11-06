# sftp

## winscp sftp sync
sync sftp to local folder
```bat
@echo off

set dir=%~dp0
set log="%dir%\my.log"
set mask=xxxxx.xxx.xxxx.*
set path="\\xx.xx\test\"
set ftpdir="/register/usr/access_grp1/"
set winscp="%dir%\WinSCP-5.13.3-Portable\winscp.com" /ini=nul /loglevel=-1 /script="%dir%\syn.txt"
set datetimenow=""

call:isodtfunc datetimenow
(echo %datetimenow% & %winscp% /parameter %mask% %ftpdir% %path% & echo.) >> %log%

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
set %~1=%_yyyy%-%_mm%-%_dd% %_hour%:%_minute%
goto:eof
```

script syn.txt
```sh
#connect to SFTP server using private key
open sftp://usr@sftp-reg.cloud.xxx.com/
  -hostkey="ssh-rsa 2048 Hdkiifvvr1rNc0+jfk+yzcVWxxxnhu8eu/3EA="
  -privatekey="usr_ssh_key.ppk" -passphrase="xxxx"

#download file
#get -preservetime -filemask="%1%" "%2%*" "%3%"

#synchronize files
option batch continue
synchronize local -preservetime -filemask="%1%" "%3%" "%2%"

#exit WinSCP
exit
```

## run-ssh-add-on-windows
https://stackoverflow.com/questions/18683092/how-to-run-ssh-add-on-windows

If you are using Git Bash, turn on ssh-agent:
```sh
# start the ssh-agent in the background
ssh-agent -s
# Agent pid 59566
```

## using git's start-ssh-agent
Make sure you have Git installed and have git's cmd folder in your PATH. For example, on my computer the path to git's cmd folder is `c:\Program Files\Git\cmd`

Make sure your id_rsa file is in the folder `c:\users\yourusername\.ssh`

Restart your command prompt if you haven't already, and then run start-ssh-agent. It will find your id_rsa and prompt you for the passphrase

Update 2019 - **A better solution** if you're using Windows 10: OpenSSH is available as part of Windows 10 which makes using SSH from cmd/powershell much easier in my opinion. It also doesn't rely on having git installed, unlike my previous solution.
- Open Manage optional features from the start menu and make sure you have Open SSH Client in the list. If not, you should be able to add it.
- Open Services from the start Menu
- Scroll down to OpenSSH Authentication Agent > right click > properties
- Change the Startup type from Disabled to any of the other 3 options. I have mine set to Automatic (Delayed Start)
- Open cmd and type where ssh to confirm that the top listed path is in System32. Mine is installed at C:\Windows\System32\OpenSSH\ssh.exe. If it's not in the list you may need to close and reopen cmd.

Once you've followed these steps, ssh-agent, ssh-add and all other ssh commands should now work from cmd. To start the agent you can simply type ssh-agent.

Optional step/troubleshooting: If you use git, you should set the GIT_SSH environment variable to the output of where ssh which you ran before (e.g C:\Windows\System32\OpenSSH\ssh.exe). This is to stop inconsistencies between the version of ssh you're using (and your keys are added/generated with) and the version that git uses internally. This should prevent issues that are similar to this

Some nice things about this solution:
- You won't need to start the ssh-agent every time you restart your computer
- Identities that you've added (using ssh-add) will get automatically added after restarts. (It works for me, but you might possibly need a config file in your c:\Users\User\.ssh folder)
- You don't need git!
- You can register any rsa private key to the agent. The other solution will only pick up a key named id_rsa

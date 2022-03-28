# Credential

## add git credential to Win Credentails Manager
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
```
#not work
cmdkey /list #show all credentials
cmdkey /generic:LegacyGeneric:target=git:https://github.com /user:username /pass:mypassword #update pwd

#can only change the pwd temporally, delete it
rundll32.exe keymgr.dll, KRShowKeyMgr
```

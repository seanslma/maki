# Credential

## add git credential to Win Credentails Manager
```
cmdkey /generic:LegacyGeneric:target=git:https://github.com /user:username /pass:mypassword
cmdkey /list #show all credentials

# better option
rundll32.exe keymgr.dll, KRShowKeyMgr
```

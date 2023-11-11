# watch

## send email
```bat
@echo off
setlocal EnableDelayedExpansion

if exist "1~%" (
    echo I'm OK    
) else (
    ::send email and attach file
    set subject=Error happened
    set mail_body=Line 1.^<br /^>Line 2 ^(example^)     
    call :SendEmail "!subject!", "!mail_body!", "2~%"
)
echo done
exit /b

:SendEmail
    SETLOCAL
    set mail_from=from@example.com
    set mail_to=to@example.com
    powershell -command "Send-MailMessage -BodyAsHtml -From '%mail_from%' -To '%mail_to%' -SmtpServer 'mail.xx.yy' -Subject '%~1' -Body '%~2' -Attachments '%~3'"
    exit /b
```

## machine watch
```bat
@echo off
set ip=\\ip.xx.yy\c$
if exist %ip% (
    echo %ip% is OK
) else (
    goto SendEmail
)
exit /b

:SendEmail
    set mail_fr=my@example.com
    set mail_to=my@gmail.com
    set subject=From %COMPUTERNAME%
    set mail_body=MACHINE is down
    powershell -windowstyle hidden -command "Send-MailMessage -From '%mail_fr%' -To '<%mail_to%>' -Subject '%subject%' -SmtpServer  'mail.xx.yy' -BODY '%mail_body%'"
    exit /b
```

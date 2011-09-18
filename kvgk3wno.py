"""checks whether the song has changed in the blog and notifies"""
import urllib
from BeautifulSoup import BeautifulSoup as bs
kvgk=urllib.urlopen("http://punehues.blogspot.com").read()
soup=bs(kvgk)
finding=soup.find('h1',id="song")
songname=finding
songname=list(finding)
finalstr=songname[0]
f=open("doc.txt",'r')
prevstr=f.read()
f.close()
if finalstr==prevstr:
                print("same so notification not sent")
else:
                print("not same")
                f=open("doc.txt",'w')
                f.write(finalstr)
                f.close()
                #!/usr/bin/env python
                # @Script sendsms.py
                # @Author Siddhant Sanyam (siddhant3s@gmail.com)
                # @Online http://github.com/siddhant3s/sendsms
                # @Requires Python2.7 or (Python2.x with argparse.py)
                # @Lisense BSD License 


                import urllib, urllib2, urlparse, re, argparse, ConfigParser, os.path, getpass,sys,logging, cookielib

                default_auth_file=os.path.expanduser('~/.sendsms.auth')
                ### Command Line Praser's Arguements
                parser=argparse.ArgumentParser(description="Sends sms non-interctively using indyarocks.com")
                parser.add_argument('-t','--authfile',metavar='FILE',default=default_auth_file,help='Specify the authorization file mannually. By default it is ~/.sendsms.auth')
                parser.add_argument('-s','--setup',action='store_true',default=False, help= "Configure and generate the default authfile for the first time. Will change the existing authfile if existed")
                parser.add_argument('-q','--quiet', action='store_true',default=False, help="Don't output anything. Overrides --debug below")
                parser.add_argument('-d','--debug', action='store_true',default=False, help="Show debugging information.")
                parser.add_argument('-u','--username', help="Supply username here. If supplied, you will be prompted for the password")
                parser.add_argument('--force-login', action='store_true',help="Force a new login, dumping old cookies and session information")
                parser.add_argument("to",nargs='?', default=None,help="The number to send the message to. Can be a nick as defined in the Phonebook section of authfile. Can be multiple recipients separated by dot (.) ")
                parser.add_argument("message",default=None, nargs='?',help="The message you want to send. Else will be read from stdin")
                args=parser.parse_args()
                ### End Parser
                ### Load Config File
                logging.basicConfig(level=logging.WARNING if args.quiet else logging.DEBUG if args.debug else logging.INFO, format="%(message)s")
                loginfo=logging.info
                config=ConfigParser.ConfigParser()
                        
                loginfo("Reading Authfile:%s" % args.authfile)        
                if not config.read(args.authfile) and not args.setup:
                    logging.critical("Cannot Open authfile: %s.\n"
                                     "Run with --setup argument to setup your authfile.\n"
                                     "Exiting\n"%args.authfile)
                    sys.exit(0)
                else: 
                    loginfo("Read!")
                if args.setup:
                    try:
                        config.add_section("Login")
                    except ConfigParser.DuplicateSectionError:
                        pass
                    try:
                        config.add_section("Auth")
                    except ConfigParser.DuplicateSectionError:
                        pass
                 
                    except ConfigParser.DuplicateSectionError:
                        pass

                    config.set('Login','username',raw_input("Enter your phone number registered at FullonSMS:"))
                    config.set('Login','password',getpass.getpass("Enter your password:"))
                    config.set('Auth','loginpage','http://fullonsms.com/login.php')
                    config.set('Auth','logincheck','http://fullonsms.com/CheckLogin.php')
                    config.set('Auth','logindone','http://fullonsms.com/home.php?Login=1')
                    config.set('Auth','sendsms','http://fullonsms.com/home.php')
                    config.set('Auth','sms_sent','http://fullonsms.com/MsgSent.php')
                    with open(args.authfile, 'wb') as configfile:
                        config.write(configfile)
                    loginfo("Written file %s. Now exiting." % args.authfile)
                    if(os.path.exists(os.path.expanduser('~/.sendsms.cookies'))):
                        os.remove(os.path.expanduser('~/.sendsms.cookies'))
                        loginfo("Previous session file removed")
                    
                    sys.exit(0)
                confget=config.get
                senders_numbers=['9021716142','8446588873','8928118491','9011059894','7709983325','9422314960','7875053682','9595155213','9543910639','9422928202','9422025243'] #contains the numbers of all senders
                ###
                ### Fetch the message either from stdin or --message        
                soup=bs(kvgk)	
                findband=soup.find('p',id="band")
                bandname=list(findband)
                finalbandname=bandname[0]
                f1=open("doc.txt",'r')
                finalmsg="Song of the day :-" + "         Name :" + f1.read() + "\n             " + finalbandname  + "        - from punehues@blogspot.com"
                message=finalmsg     
                f1.close()
                ###message=message[:160]
                ###
                ### Fetch Username either from --username or prompt
                if args.username:
                    username=args.username
                    password=getpass.getpass("Enter the password:")
                else:
                    username=confget('Login','username')
                    password=confget('Login','password')
                ###
                loginfo("Username:%s" % username)
                logging.debug("Password:%s" % password)
                ### Cookies
                try_with_previous = False
                filecookiejar = cookielib.MozillaCookieJar(os.path.expanduser('~/.sendsms.cookies'))
                try:
                    filecookiejar.load(ignore_discard=True)
                except:
                    logging.debug("Cannot open the cookie file. Check if it exists. Ignore if this is first time.")
                    cookieprocessor=urllib2.HTTPCookieProcessor()
                    loginfo("No previous Authentication session")
                else:
                    loginfo("Previous Authentication session found. Will try with that first")
                    logging.debug("Previous Cookie read from file: %s" % filecookiejar)
                    cookieprocessor=urllib2.HTTPCookieProcessor(filecookiejar)
                    try_with_previous=True
                o = urllib2.build_opener( cookieprocessor )
                if args.force_login:
                    loginfo("--force-login selected. Will not consider previous authentication sessions")
                    try_with_previous = False
                def tryopen(opener,url,data=None):
                    global logging
                    while True:
                        try:
                            f = opener.open(url,data)
                            return f
                        except urllib2.URLError:
                            loginfo("Caught an Exception URLError. Retrying...")
                            pass
                class SendSMS:
                    """Base class which send sms using various online websties like fullonsms.com"""
                    def __init__(self):
                        pass
                    def sendsms():
                        pass

                ### sendmessage function
                def sendmessage(to_number,message):
                    global confget
                    global o
                    global logging
                    ### send the message
                    fullsendsms=confget('Auth','sendsms')
                    info =  urllib.urlencode({
                            "CancelScript":"/home.php",
                            "MobileNos":to_number,
                            "Message":message,
                            "SelGroup":"",
                            "Gender":"0",
                            "FriendName":"Your Friend Name",
                            "ETemplatesId":"",
                            "TabValue":"contacts"
                            })
                    logging.debug("POST Query: %s" % info)
                    f = tryopen(o,fullsendsms,info)
                    data_returned=f.readlines()[-1]
                    ###
                    ### check if it was sent properly
                    logging.debug("Last line of Data returned: %s" % data_returned)
                    if data_returned.find(confget('Auth','sms_sent'))!=-1:
                        return 'sent'
                    elif data_returned.find(confget('Auth','loginpage'))!=-1:
                        return 'login'
                    else:
                        return 'failed'
                    ###
                ###
                ### login function 
                def login(uname,passwd):
                    global logging
                    global o
                    global confget
                    global filecookiejar
                    logging.debug("Logging using url: %s" % confget('Auth','logincheck'))
                    login_encode=urllib.urlencode({'MobileNoLogin':uname, 'LoginPassword':passwd})
                    logging.debug("login_encode:%s" % login_encode)
                    cookieprocessor=urllib2.HTTPCookieProcessor() #new cookie processor
                    o = urllib2.build_opener(cookieprocessor) # a new urlopener
                    f = tryopen(o,confget('Auth','logincheck'),login_encode)
                    logging.debug("Sent Login information, got the following return URL: %s", f.geturl())
                    if f.read().find(confget('Auth','logindone')) != -1:
                        #save cookies
                        cj=cookieprocessor.cookiejar
                        cookie=enumerate(cj).next()[1]
                        logging.debug("New Cookie:%s:" % cookie)
                        filecookiejar.set_cookie(cookie)
                        filecookiejar.save(ignore_discard=True)
                        logging.debug("Cookies saved in %s" % filecookiejar.filename)
                        return True
                    else:
                        return False
                for n in senders_numbers:
                    ###
                    ### Send the message and check if it was sent
                    loginfo("Sending to %s, the following message:\n%s" % (n,message))
                    ###First check without loggin in using previous cookies
                    logging.debug("try_with_previous:%s"% try_with_previous)
                    while True:
                        if not try_with_previous:
                         ### Logging in
                            loginfo("Trying to login")
                            if login(username,password):
                                loginfo("Login Successfull")
                                try_with_previous=True
                            else:
                                loginfo("Login Failed. Check username, password")
                                sys.exit(3)
                        result=sendmessage(n,message)
                        if result=='sent':
                            loginfo("Seems Like message was successfully sent to %s." % n)
                            loginfo("\a")
                            break
                        elif result=='failed':
                            loginfo("SMS Not sent to %s. Can't figure out why. Perhaps try again later\n" % n)
                            break
                        elif result=='login':
                            try_with_previous=False
	
        
        


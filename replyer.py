#Class AUTO RE-LOGIN

from datetime import datetime
from datetime import timedelta, date
from time import sleep
import time, timeit, random, sys, os, json, requests, subprocess, string, codecs, urllib, urllib.parse, shutil, atexit
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient

bot_login = codecs.open('json/logged.json', 'r', 'utf-8')
run_bot = json.load(bot_login)

system = "ALFINO-PCV3"
host = 'https://gwx.line.naver.jp'
FINBOT_TIMELINE_API = 'https://gwx.line.naver.jp/mh/api'
FINBOT_TIMELINE_MH = 'https://gwx.line.naver.jp/mh'
FINBOT_OBS_DOMAIN = 'https://obs-tw.line-apps.com'
FINBOT_AUTH_QUERY_PATH = '/api/v4p/rs'
FINBOT_AUTH_QUERY_PATH_FIR = '/api/v4/TalkService.do'
FINBOT_CERTIFICATE_PATH = '/Q'
FINBOT_API_QUERY_PATH_FIR = '/S4'

UA = run_bot['DESKTOPMAC']['UA']
LA = run_bot['DESKTOPMAC']['LA']
UA1 = run_bot['CHROMEOS']['UA']
LA1 = run_bot['CHROMEOS']['LA']
UA2 = run_bot['DESKTOPWIN']['UA']
LA2 = run_bot['DESKTOPWIN']['LA']
UA3 = run_bot["IOS"]["UA"]
LA3 = run_bot["IOS"]["LA"]
UA4 = run_bot['WIN10']['UA']
LA4 = run_bot["WIN10"]['LA']
UA5 = run_bot['CLOVAFRIENDS']['UA']
LA5 = run_bot["CLOVAFRIENDS"]["LA"]
RELOAD_UA = run_bot['RELOAD']['User-Agent']
RELOAD_LA = run_bot['RELOAD']['X-LineAccess']
_session = requests.session()

UA = ["Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)","Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0","Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0","Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0","Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"]
msg_dict = {}
msg_dict1 = {}
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def sendCarousel(data):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    data = data
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.10.1'
    headers['Content-Type'] = 'application/json'
    return _session.post(url,data=json.dumps(data),headers=headers)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def fositive():
	txt1 = ['Target Added', 'Add success', 'Added', 'Has been Promoted']
	send1 = random.choice(txt1)
	return send1
def negative():
	txt2 = ['Target Removed', 'Target Deleted', 'Removed', 'Deleted', 'Clear Target']
	send2 = random.choice(txt2)
	return send2
def intro():
	txt3 = ['Send Did You mean to Update', 'Send Target To Up']
	send3 = random.choice(txt3)
	return send3
def fail():
	txt4 = ['Failed', 'Failure', 'Something Went Wrong', 'Access Negative', 'Error']
	send4 = random.choice(txt4)
	return send4
def on():
	txt5 = ['Status Enabled', 'Enabled', 'Status On', 'Access Granted', 'Already Active']
	send5 = random.choice(txt5)
	return send5
def off():
	txt6 = ['Status Dissabled', 'Dissabled', 'Deactivated', 'Status Off']
	send6 = random.choice(txt6)
	return send6
def cft():
	txt7 = ['Photo Profile Updated', 'Picture Update', 'Profile updated']
	send7 = random.choice(txt7)
	return send7
def dno():
	txt8 = ['Success', 'Done', 'Beres Bos', 'Clear Boss']
	send8 = random.choice(txt8)
	return send8
def up():
	txt9 = ['Update to: ', 'Changed to: ', 'Replaced to: ']
	send9 = random.choice(txt9)
	return send9
def List():
	txt10 = ['No list added', 'Empty list', 'No target added', 'Daftar masih kosong', 'Tak ada daftar yang di tambahkan']
	send10 = random.choice(txt10)
	return send10
def Bl():
	txt11 = ['Blacklist added', 'User blacklisted', 'Pengguna telah ditambahkan dalam daftar hitam']
	send11 = random.choice(txt11)
	return send11
def dBL():
	txt12 = ['Blacklist deleted', 'Blacklist removed', 'User blacklist removed', 'Daftar hitam dihapus']
	send12 = random.choice(dBL)
	return send12
def ass():
	assa = ["وَعَلَيْكُمْ السَّلاَم","Wa'alaikumussalaam warrahmatullahi wabarakatuh","وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ"]
	assalam = random.choice(assa)
	return assalam
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def update_non_existing_inplace(original_dict, to_add):
    for key, value in original_dict.items():
        if key not in to_add:
            to_add[key] = value
        if type(value) == dict:
            for k, v in value.items():
                if k not in to_add[key]:
                    to_add[key][k] = v
    original_dict.update(to_add)
    return original_dict

class Key(dict):
    def __missing__(self, key):
        return '{' + key + '}'

class CallFinbot(object):
    def __init__(self, callback):
        self.callback = callback

    def QrUrl(self, url, showQr=True):
        self.callback(url)

    def default(self, str):
        self.callback(str)

def getJson(url, headers=None):
    if headers is None:
        return json.loads(_session.get(url).text)
    else:
        return json.loads(_session.get(url, headers=headers).text)

def defaultCallback(str):
    print(str)

def DESKTOPMAC(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA,'X-Line-Application': LA,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def CHROMEOS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA1,'X-Line-Application': LA1,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client
 
def DESKTOPWIN(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA2,'X-Line-Application': LA2,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def IOS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA3,'X-Line-Application': LA3,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def WIN10(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA4,'X-Line-Application': LA4,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def CLOVAFRIENDS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA5,'X-Line-Application': LA5,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def AUTO_RELOAD(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': RELOAD_UA,'X-Line-Application': RELOAD_LA,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client
    
def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data1.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend1)

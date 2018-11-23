#Class AUTO RE-LOGIN

from ALFINONH import *
from KANG.ttypes import *
from datetime import datetime
from datetime import timedelta, date
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, pafy, time, timeit, random, sys, ast, re, os, json, requests, threading, string, codecs, ctypes, shutil, atexit, six, youtube_dl, traceback
import urllib, urllib.parse
import base64, tempfile
from NET.protocol import TCompactProtocol
from NET.transport import THttpClient
from assist import Assist, Assist2, LineBot
from gtts import gTTS
from googletrans import Translator
from threading import Thread
_session = requests.session()

bot_login = codecs.open('json/logged.json', 'r', 'utf-8')
run_bot = json.load(bot_login)

system = "ALFINO-PCV3"
host = 'https://gwx.line.naver.jp'
FINBOT_TIMELINE_API = 'https://gd2.line.naver.jp/mh/api'
FINBOT_TIMELINE_MH = 'https://gd2.line.naver.jp/mh'
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

UserAgent = ["Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)","Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0","Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0","Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0","Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"]

def login(resp, id, password):
	bot = Assist(resp, id, password)

def loginId(resp, id, password):
	bot2 = Assist2(resp, id, password)

def login3(name, email, password):
	lineBot = LineBot(name, email, password)
	
def RunAll():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=loginId, args=('F1',Logged["A"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F2',Logged["A"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F3',Logged["A"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F4',Logged["A"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F5',Logged["A"]["5"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F6',Logged["A"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F7',Logged["A"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F8',Logged["A"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F9',Logged["A"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F10',Logged["A"]["10"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F11',Logged["B"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F12',Logged["B"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F13',Logged["B"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F14',Logged["B"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F15',Logged["B"]["5"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F16',Logged["B"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F17',Logged["B"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F18',Logged["B"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F19',Logged["B"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F20',Logged["B"]["10"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F21',Logged["C"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F22',Logged["C"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F23',Logged["C"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F24',Logged["C"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F25',Logged["C"]["5"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F26',Logged["C"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F27',Logged["C"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F28',Logged["C"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F29',Logged["C"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F30',Logged["C"]["10"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F31',Logged["D"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F32',Logged["D"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F33',Logged["D"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F34',Logged["D"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F35',Logged["D"]["5"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F36',Logged["D"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F37',Logged["D"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F38',Logged["D"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F39',Logged["D"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login, args=('F40',Logged["D"]["10"],Logged["passwd"])).start()

def run1():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=loginId, args=('F1',Logged["A"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F2',Logged["A"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F3',Logged["A"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F4',Logged["A"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F5',Logged["A"]["5"],Logged["passwd"])).start()
	return Fsbv3

def run2():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=loginId, args=('F6',Logged["A"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F7',Logged["A"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F8',Logged["A"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F9',Logged["A"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F10',Logged["A"]["10"],Logged["passwd"])).start()
	return Fsbv3

def run3():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=loginId, args=('F11',Logged["B"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F12',Logged["B"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F13',Logged["B"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F14',Logged["B"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F15',Logged["B"]["5"],Logged["passwd"])).start()
	return Fsbv3

def run4():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=loginId, args=('F16',Logged["B"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F17',Logged["B"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F18',Logged["B"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F19',Logged["B"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=loginId, args=('F21',Logged["B"]["10"],Logged["passwd"])).start()
	return Fsbv3

def run5():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=login3, args=('F21',Logged["C"]["1"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F22',Logged["C"]["2"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F23',Logged["C"]["3"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F24',Logged["C"]["4"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F25',Logged["C"]["5"],Logged["passwd"])).start()
	return Fsbv3

def run6():
	with open('json/finbot1.json', 'r') as fp:
		Logged = json.load(fp)
	Fsbv3 = threading.Thread(target=login3, args=('F26',Logged["C"]["6"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F27',Logged["C"]["7"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F28',Logged["C"]["8"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F29',Logged["C"]["9"],Logged["passwd"])).start()
	Fsbv3 = threading.Thread(target=login3, args=('F31',Logged["C"]["10"],Logged["passwd"])).start()
	return Fsbv3


def like(self, mid, postid, likeType=1001):
	mid = self.profile.mid
	header = {"Content-Type" : "application/json","X-Line-Mid" : mid,"x-lct" : run_bot['fino']['AuthToken']}
	payload = {"likeType" : likeType,"activityExternalId" : postid,"actorId" : mid}
	r = requests.post("http://" + host + "/mh/api/v23/like/create.json?homeId=" + mid,headers = header,data = json.dumps(payload))
	return r.json()

def comment(self, mid, postid, text):
	mid = self.pofile.mid
	header = {"Content-Type" : "application/json","X-Line-Mid" : mid,"x-lct" : run_bot['fino']['AuthToken']}
	payload = {"commentText" : text,"activityExternalId" : postid,"actorId" : mid}
	r = requests.post("http://" + host + "/mh/api/v23/comment/create.json?homeId=" + mid,headers = header,data = json.dumps(payload))
	return r.json()
	
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
	Headers = {
	'User-Agent': run_bot['RELOAD']['User-Agent'],
	'X-Line-Application': run_bot['RELOAD']['X-LineAccess'],
	"x-lal": "ja-US_US"
	}
	Headers.update({"x-lpqs" : path})
	if(update_headers is not None):
		Headers.update(update_headers)
		transport = THttpClient.THttpClient(host + path)
		protocol = TCompactProtocol.TCompactProtocol(transport)
		client = service(protocol)
		return client

def genTemporary(self, returnAs='path'):
	try:
		if returnAs not in ['file','path']:
			raise Exception('Invalid returnAs value')
		fName, fPath = 'finbotSQL-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()
		if returnAs == 'file':
			return fName
		elif returnAs == 'path':
			return os.path.join(fPath, fName)
	except Exception as e:
		print(e)

class Calculator:
    def addition(self,x,y):
        added = x + y
        return added
    def subtraction(self,x,y):
        subtracted = x - y
        return subtracted
    def multiplication(self,x,y):
        multiplied = x * y
        return multiplied
    def division(self,x,y):
        divided = x / y
        return divided

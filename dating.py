'''
Created on Oct 23, 2016

@author: Makeda Phoenix
'''

import json
import requests
import datetime

url = 'http://challenge.code2040.org/api/dating'
urlFini = 'http://challenge.code2040.org/api/dating/validate'
token = 'fe51f0ab89f32b551b8baa8632c0001c'
data = {'token' : token}

r = requests.post(url, data)
info = r.json()

datestamp = info['datestamp']
interval = info['interval']

currentDate = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')


toFormat = currentDate + datetime.timedelta(seconds = int(interval))
newDate = toFormat.strftime('%Y-%m-%dT%H:%M:%SZ')

dataFini = {'token' : token, 'datestamp' : newDate}

response = requests.post(urlFini, dataFini)
print(response.text)

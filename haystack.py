'''
Created on Oct 23, 2016

@author: Makeda Phoenix
'''

import json
import requests

url = 'http://challenge.code2040.org/api/haystack'
urlFini = 'http://challenge.code2040.org/api/haystack/validate'
token = 'fe51f0ab89f32b551b8baa8632c0001c'
data = {'token' : token}

r = requests.post(url, data)
info = r.json()
needle = info['needle']
haystack = info['haystack']

for i in range(0, len(haystack)):
    if needle == haystack[i]:
        index = i
        break
    
dataFini = {'token' : token, 'needle' : index}
response = requests.post(urlFini, dataFini)
print(response.text)

'''
Created on Oct 23, 2016

@author: Makeda Phoenix
'''

import json
import requests

url = 'http://challenge.code2040.org/api/prefix'
urlFini = 'http://challenge.code2040.org/api/prefix/validate'
token = 'fe51f0ab89f32b551b8baa8632c0001c'
data = {'token' : token}

r = requests.post(url, data)
info = r.json()
prefix = info['prefix']
list1 = info['array']
listFini = []

same = True
prefixLength = len(prefix)

#compare beginning of Strings in array to prefix
for i in range(0, len(list1)):
    check = list1[i][:prefixLength]
    if check == prefix:
        same = True
    else:
        same = False
    if same == False:
        listFini.append(list1[i])
    same = False

dataFini = {'token' : token, 'array' : listFini}
result = requests.post(urlFini, json = dataFini)

print(result.text)

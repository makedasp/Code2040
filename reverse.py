'''
Created on Oct 23, 2016

@author: Makeda Phoenix
'''
import json
import requests


url = 'http://challenge.code2040.org/api/reverse'
urlFini = 'http://challenge.code2040.org/api/reverse/validate'
token = 'fe51f0ab89f32b551b8baa8632c0001c'
data = {'token' : token}

toReverse = requests.post(url, data)
reversed = toReverse.text[::-1]

dataFini = {'token' : token, 'string' : reversed}
response = requests.post(urlFini, dataFini)
print(response.text)

'''
Created on Oct 23, 2016

@author: Makeda Phoenix
'''

import json
import requests

url = 'http://challenge.code2040.org/api/register'
token = 'fe51f0ab89f32b551b8baa8632c0001c'
data = {'token' : token, 'github' : 'https://github.com/makedasp/Code2040'}
response = requests.post(url, data)
print(response.text)

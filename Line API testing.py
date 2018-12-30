#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import requests

url = 'https://notify-api.line.me/api/notify'
token = 'eHS01NulezqJXxkrSErDZxAgezwhEaNR3B6YrQm48z7'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ทดสอบภาษาไทย hello World'
r = requests.post(url, headers=headers, data={'message': msg})

print(r.text, end='\n',)


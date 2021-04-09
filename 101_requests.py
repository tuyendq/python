#!/usr/bin/env python3

import requests

path = 'robots.txt'
host = 'https://tryhackme.com/'

while(host is not ''):
    response = requests.get(host + path)
    print(response)
    status_code = response.status_code
    text = response.text
    print(text)
    host = ''

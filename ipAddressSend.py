#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

url = 'https://notify-api.line.me/api/notify'
token = 'BycSzifdRdq8znBVIo3ZJFZ94WejWF8KqRFRL157f72'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

date = datetime.datetime.now()
tarih = datetime.datetime.strftime(date, '%c')

read_ip = open('ipReel.txt', 'r', encoding="utf-8")
ip = read_ip.readlines()
read_ip.close()

msg = tarih + '\nIp Adresim: ' + ip[0] 
#print(msg)
r = requests.post(url, headers=headers, data = {'message':msg})
#print(r.text)

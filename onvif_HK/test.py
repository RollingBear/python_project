# -*- coding: utf-8 -*-

#   2019/4/25 0025 下午 4:17     

__author__ = 'RollingBear'


import requests
import json


headers = {'content-type': 'application/json'}
url_get = 'http://127.0.0.1:9898/getrtspurl'
url_control = 'http://127.0.0.1:9898/cameracontrol'

data_get = {'ip': '192.168.81.11', 'port': '80', 'username': 'admin', 'password': 'admin123456', 'is_auth': 'True'}
data_control = {'ip': '192.168.81.11', 'port': '80', 'username': 'admin', 'password': 'admin123456', 'action': 'left'}

# result = requests.post(url_get, data=json.dumps(data_get), headers=headers)
result = requests.post(url_control, data=json.dumps(data_control), headers=headers)

print(result.text)
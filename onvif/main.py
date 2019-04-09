# -*- coding: utf-8 -*-

#   2019/4/8 0008 下午 5:27     

__author__ = 'RollingBear'


from onvif import ONVIFCamera

camera = ONVIFCamera('192.168.81.11', 80, 'abc', 'abcd1234')

# resp = camera.devicemgmt.GetHostname()
# print(resp)

file = camera.devicemgmt.GetCapabilities()
print(file)

# help(ONVIFCamera)

media_service = camera.create_media_service()
print(media_service)
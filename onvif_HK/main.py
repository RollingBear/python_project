# -*- coding: utf-8 -*-

#   2019/4/8 0008 下午 5:27     

__author__ = 'RollingBear'

import cv2
import zeep
from onvif import ONVIFCamera



def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


def make_uri_withauth(uri, USERNAME, PASSWORD):
    newuri = uri[:7] + str(USERNAME) + ':' + str(PASSWORD) + '@' + uri[7:]
    return newuri


camera = ONVIFCamera('192.168.81.11', 80, 'admin', 'admin123456')

# resp = camera.devicemgmt.GetHostname()
# print(resp)

# file = camera.devicemgmt.GetCapabilities()
# print(file)

# help(ONVIFCamera)

# camera.devicemgmt.GetServices(False)
media_service = camera.create_media_service()
# ptz_service = camera.create_ptz_service()

# print(media_service)

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

# profiles = media_service.GetSnapshotUri()
profiles = media_service.GetProfiles()
token = profiles[0].token
uri = media_service.GetStreamUri(
    {'StreamSetup': {'Stream': 'RTP_unicast', 'Transport': {'Protocol': 'RTSP'}}, 'ProfileToken': token})

# uri = 'rtsp://admin:admin123456@192.168.81.11:554/Streaming/Channels/101?transportmode=mcast&profile=Profile_1'

# print(uri)
url = make_uri_withauth(uri['Uri'], 'admin', 'admin123456')
cap = cv2.VideoCapture(url)

while (True):
    ret, frame = cap.read()

    print(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

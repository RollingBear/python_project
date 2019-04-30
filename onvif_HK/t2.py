# -*- coding: utf-8 -*-

#   2019/4/29 0029 下午 4:55

__author__ = 'RollingBear'

from onvif import ONVIFCamera
import zeep


def zeep_python_value(self, xml_value):
    return xml_value


zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_python_value

mycam = ONVIFCamera('192.168.81.222', 80, 'admin', 'admin123456', 'E:\\python\\python_project\\onvif_HK\\wsdl')

media = mycam.create_media_service()
media_profile = media.GetProfiles()[0]

ptz = mycam.create_ptz_service()

token = media_profile.token
# print(token)
GetUri = media.GetSnapshotUri({'ProfileToken': token})
# print(GetUri)
print(mycam.ptz.GetConfiguration())
# request = ptz.create_type('AbsoluteMove')
# request.ProfileToken = media_profile.token

# request.Position.PanTilt = {'x': 0.5, 'y': -0.5}
# ptz.AbsoluteMove(request)
pos = ptz.GetStatus({'ProfileToken': token}).Position
# print(pos)

Cmove = ptz.create_type('ContinuousMove')
Cmove.ProfileToken = token
Cmove.Velocity.Zoom._x = 0.2
ptz.ContinuousMove(Cmove)


# req_move = ptz.create_type('AbsoluteMove')
# req_move.ProfileToken = token
#
# req_stop = ptz.create_type('Stop')
# req_stop.ProfileToken = token
#
# msg = ptz.create_type('GetConfigurationsResponse')
# status = ptz.GetPresets.GetProfiles()

# print(media.GetProfiles())
# print(req_move)


# print(req_stop)
# print(msg)
# print(status)

# def move_left(speed=0.1):
#     req_move.Position.Zoom.x = speed
#     # req_move.Velocity.PanTilt.y = 0.0
#     ptz.AbsoluteMove(req_move)
#     # ptz.Stop(req_stop)

# move_left()

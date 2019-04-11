# _*_coding:utf-8_*_
import sys
import bottle
from bottle import response, request, post
from onvif import ONVIFCamera
import zeep
import logging
from logging.handlers import RotatingFileHandler
import traceback
import time
from gevent import monkey

monkey.patch_all()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    stream=sys.stdout)

# 定义按文件大小切割日志
logger = logging.getLogger()
Rthandler = RotatingFileHandler(sys.path[0] + '/log.log', maxBytes=10, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)

app = bottle.Bottle()
bottle.BaseRequest.MEMFILE_MAX = 10 * 1024 * 1024  #


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

XMAX = 1
XMIN = -1
YMAX = 1
YMIN = -1


# 摄像头控制
def perform_move(ptz, request, timeout):
    # Start continuous move
    ptz.ContinuousMove(request)
    # Wait a certain time
    time.sleep(timeout)
    # Stop continuous move
    ptz.Stop({'ProfileToken': request.ProfileToken})


# 摄像头上转
def move_up(ptz, request, timeout=1):
    print('move up...')
    request.Velocity.PanTilt._x = 0
    request.Velocity.PanTilt._y = YMAX
    perform_move(ptz, request, timeout)


# 摄像头下转
def move_down(ptz, request, timeout=1):
    print('move down...')
    request.Velocity.PanTilt._x = 0
    request.Velocity.PanTilt._y = YMIN
    perform_move(ptz, request, timeout)


# 摄像头右转
def move_right(ptz, request, timeout=1):
    print('move right...')
    request.Velocity.PanTilt._x = XMAX
    request.Velocity.PanTilt._y = 0
    perform_move(ptz, request, timeout)


# 摄像头左转
def move_left(ptz, request, timeout=1):
    print('move left...')
    request.Velocity.PanTilt._x = XMIN
    request.Velocity.PanTilt._y = 0
    perform_move(ptz, request, timeout)


# 摄像头控制
def continuous_move(action, ip, port, username, password):
    mycam = ONVIFCamera(ip, port, username, password)
    # Create media service object
    media = mycam.create_media_service()
    # Create ptz service object
    ptz = mycam.create_ptz_service()

    # Get target profile
    media_profile = media.GetProfiles()[0]

    # Get PTZ configuration options for getting continuous move range
    request = ptz.create_type('GetConfigurationOptions')
    request.ConfigurationToken = media_profile.PTZConfiguration.token
    ptz_configuration_options = ptz.GetConfigurationOptions(request)

    request = ptz.create_type('ContinuousMove')
    request.ProfileToken = media_profile.token

    ptz.Stop({'ProfileToken': media_profile.token})

    # Get range of pan and tilt
    # NOTE: X and Y are velocity vector
    global XMAX, XMIN, YMAX, YMIN
    XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
    XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
    YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
    YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

    if action == 'up':
        move_up(ptz, request)
    elif action == 'down':
        move_down(ptz, request)
    elif action == 'left':
        move_left(ptz, request)
    elif action == 'right':
        move_right(ptz, request)


@app.route('/getrtspurl', method='POST')
def getrtspurl():
    """
        接收参数：json格式
        POST
        {'ip': '', 'port': '', 'username': '', 'password': '', 'action': ''}
        :return:
    """
    try:
        response.content_type = "application/json"
        data = request.json
        ip = data['ip']
        port = int(data['port'])
        username = data['username']
        password = data['password']
        mycam = ONVIFCamera(ip, port, username, password)
        media_service = mycam.create_media_service()
        profiles = media_service.GetProfiles()
        token = profiles[2].token
        uri = media_service.GetStreamUri(
            {'StreamSetup': {'Stream': 'RTP_unicast', 'Transport': {'Protocol': 'RTSP'}}, 'ProfileToken': token})
        print(uri)
    except Exception as e:
        logger.error(traceback.format_exc())


@app.route('/cameracontrol', method='POST')
def cameracontrol():
    """
        接收参数：json格式 POST
        {'ip':'','port':'','username':'','password':'','action':''}
        :return:
    """
    try:
        response.content_type = "application/json"
        data = request.json
        ip = data['ip']
        port = int(data['port'])
        username = data['username']
        password = data['password']
        action = data['action']
        continuous_move(action, ip, port, username, password)
    except Exception as e:
        logger.error(traceback.format_exc())


def start():
    bottle.run(app,
               # server='gevent',
               # host="0.0.0.0",
               host="127.0.0.1",
               port=9898, reloader=True, debug=True)

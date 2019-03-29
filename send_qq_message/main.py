# -*- coding: utf-8 -*-

#   2019/3/27 0027 下午 5:35     

__author__ = 'RollingBear'

import sys
import ctypes
import logging
import traceback

from PyQt5.QtWidgets import QApplication

from send_qq_message.ui import main_window


def start():
    app = QApplication(sys.argv)
    ui = main_window()
    sys.exit(app.exec_())


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        logging.info(traceback.format_exc())
        return False


def get_admin():
    if is_admin():
        start()
    else:
        try:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.shellExecuteW(None, 'runas', sys.executable, __file__, None, 1)
        except Exception:
            logging.info(traceback.format_exc())


if __name__ == '__main__':
    get_admin()

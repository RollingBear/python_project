# -*- coding: utf-8 -*-

#   2019/4/3 0003 下午 4:39     

__author__ = 'RollingBear'

from sys import argv, exit
from PyQt5.QtWidgets import QApplication

from browser_bate_1_1_0.web_view import web_view

if __name__ == '__main__':
    app = QApplication(argv)
    web = web_view()
    web.show()
    exit(app.exec_())

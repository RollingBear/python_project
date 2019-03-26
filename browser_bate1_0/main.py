# -*- coding: utf-8 -*-

#   2019/3/26 0026 上午 10:14     

__author__ = 'RollingBear'

from PyQt5.QtWidgets import QApplication

import sys

import browser_bate1_0.ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = browser_bate1_0.ui.main_window()
    ui.show()
    sys.exit(app.exec_())

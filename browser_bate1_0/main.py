# -*- coding: utf-8 -*-

#   2019/3/26 0026 上午 10:14     

__author__ = 'RollingBear'

from PyQt5.QtWidgets import QApplication

from browser_bate1_0.ui import main_window

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_window(init_url='https://www.qq.com', label='HomePage')
    ui.show()
    sys.exit(app.exec_())

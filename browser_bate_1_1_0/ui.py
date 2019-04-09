# -*- coding: utf-8 -*-

#   2019/4/3 0003 下午 4:40     

__author__ = 'RollingBear'

from PyQt5.QtCore import QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QProgressBar, QSizePolicy, QTabWidget, QStatusBar


class ui(QMainWindow):

    def __init__(self, ui):
        super().__init__()

        self.ui = ui
        self.initial()

    def initial(self):
        self.ui.setObjectName('Main window')
        self.ui.resize(1280, 720)

        self.central_widget = QWidget(self.ui)
        self.central_widget.setObjectName('Central Widget')

        self.vertical_layout = QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName('Vertical layout')
        self.horizontal_layout_1 = QHBoxLayout()
        self.horizontal_layout_2 = QHBoxLayout()
        self.horizontal_layout_1.setObjectName('Horizontal layout 1')
        self.horizontal_layout_2.setObjectName('Horizontal layout 2')

        new_icon = QIcon()
        new_icon.addPixmap(QPixmap(':/icon/res/new.png'), QIcon.Normal, QIcon.Off)
        home_icon = QIcon()
        home_icon.addPixmap(QPixmap(':/icon/res/home.png'), QIcon.Normal, QIcon.Off)
        forward_icon = QIcon()
        forward_icon.addPixmap(QPixmap(':/icon/res/forward.ico'), QIcon.Normal, QIcon.Off)
        back_icon = QIcon()
        back_icon.addPixmap(QPixmap(':/icon/res/back.ico'), QIcon.Normal, QIcon.Off)
        refresh_btn = QIcon()
        refresh_btn.addPixmap(QPixmap(':/icon/res/reload.ico'), QIcon.Normal, QIcon.Off)
        stop_btn = QIcon()
        stop_btn.addPixmap(QPixmap(':/icon/res/stop.ico'), QIcon.Normal, QIcon.Off)

        self.new_btn = QPushButton(self.central_widget)
        self.new_btn.setObjectName('New button')
        self.new_btn.setIcon(new_icon)
        self.horizontal_layout_1.addWidget(self.new_btn)
        self.home_btn = QPushButton(self.central_widget)
        self.home_btn.setObjectName('Home button')
        self.home_btn.setIcon(home_icon)
        self.horizontal_layout_1.addWidget(self.home_btn)
        self.forward_btn = QPushButton(self.central_widget)
        self.forward_btn.setObjectName('Forward button')
        self.forward_btn.setIcon(forward_icon)
        self.forward_btn.setEnabled(False)
        self.horizontal_layout_1.addWidget(self.forward_btn)
        self.back_btn = QPushButton(self.central_widget)
        self.back_btn.setObjectName('Back button')
        self.back_btn.setIcon(back_icon)
        self.back_btn.setEnabled(False)
        self.horizontal_layout_1.addWidget(self.back_btn)
        self.refresh_btn = QPushButton(self.central_widget)
        self.refresh_btn.setObjectName('Refresh button')
        self.refresh_btn.setIcon(refresh_btn)
        self.horizontal_layout_1.addWidget(self.refresh_btn)
        self.stop_btn = QPushButton(self.central_widget)
        self.stop_btn.setObjectName('Stop button')
        self.stop_btn.setIcon(stop_btn)
        self.horizontal_layout_1.addWidget(self.stop_btn)

        self.url_line_edit = QLineEdit(self.central_widget)
        self.url_line_edit.setObjectName('Url line edit')
        self.horizontal_layout_1.addWidget(self.url_line_edit)

        self.horizontal_layout_2.addLayout(self.horizontal_layout_1)

        self.progress_bar = QProgressBar(self.central_widget)
        self.progress_bar.setObjectName('Progress bar')
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalPolicy(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(size_policy)
        self.progress_bar.setProperty('value', 0)
        self.progress_bar.setTextVisible(False)
        self.horizontal_layout_2.addWidget(self.progress_bar)

        go_icon = QIcon()
        go_icon.addPixmap(QPixmap(':/icon/res/go.png'), QIcon.Normal, QIcon.Off)

        self.go_btn = QPushButton(self.central_widget)
        self.go_btn.setObjectName('Go button')
        self.go_btn.setIcon(go_icon)
        self.horizontal_layout_2.addWidget(self.go_btn)

        self.vertical_layout.addLayout(self.horizontal_layout_2)

        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName('Tab widget')
        self.tab_widget.setTabShape(QTabWidget.Triangular)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.vertical_layout.addWidget(self.tab_widget)

        self.ui.setCentralWidget(self.central_widget)

        self.status_bar = QStatusBar(self.ui)
        self.status_bar.setObjectName('Status bar')
        self.ui.setStatusBar(self.status_bar)

        self.retranslate_ui(self.ui)
        self.tab_widget.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(self.ui)

    def retranslate_ui(self, ui):
        _translate = QCoreApplication.translate
        ui.setWindowTitle(_translate('Main window', 'PyQt5 Browser 1.1.0a'))
        self.new_btn.setText(_translate('Main window', 'New Page'))
        self.home_btn.setText(_translate('Main window', 'Home Page'))
        self.forward_btn.setText(_translate('Main window', 'Forward'))
        self.back_btn.setText(_translate('Main window', 'Back'))
        self.refresh_btn.setText(_translate('Main window', 'Refresh'))
        self.stop_btn.setText(_translate('Main window', 'Stop'))
        self.go_btn.setText(_translate('Main window', 'GO'))
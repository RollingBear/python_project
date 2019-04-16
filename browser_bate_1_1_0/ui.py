# -*- coding: utf-8 -*-

#   2019/4/3 0003 下午 4:40     

__author__ = 'RollingBear'

from PyQt5 import QtCore, QtGui, QtWidgets


class ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1280, 720)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("vertical_layout")

        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")

        new_icon = QtGui.QIcon()
        new_icon.addPixmap(QtGui.QPixmap("res/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        home_icon = QtGui.QIcon()
        home_icon.addPixmap(QtGui.QPixmap("res/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        forward_icon = QtGui.QIcon()
        forward_icon.addPixmap(QtGui.QPixmap("res/forward.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        back_icon = QtGui.QIcon()
        back_icon.addPixmap(QtGui.QPixmap("res/back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        refresh_icon = QtGui.QIcon()
        refresh_icon.addPixmap(QtGui.QPixmap("res/reload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        stop_icon = QtGui.QIcon()
        stop_icon.addPixmap(QtGui.QPixmap("res/stop.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        go_icon = QtGui.QIcon()
        go_icon.addPixmap(QtGui.QPixmap("res/go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.new_button = QtWidgets.QPushButton(self.central_widget)
        self.new_button.setIcon(new_icon)
        self.new_button.setObjectName("new_button")
        self.horizontal_layout_1.addWidget(self.new_button)
        self.home_button = QtWidgets.QPushButton(self.central_widget)
        self.home_button.setIcon(home_icon)
        self.home_button.setObjectName("home_button")
        self.horizontal_layout_1.addWidget(self.home_button)
        self.forward_button = QtWidgets.QPushButton(self.central_widget)
        self.forward_button.setEnabled(False)
        self.forward_button.setIcon(forward_icon)
        self.forward_button.setObjectName("forward_button")
        self.horizontal_layout_1.addWidget(self.forward_button)
        self.back_button = QtWidgets.QPushButton(self.central_widget)
        self.back_button.setEnabled(False)
        self.back_button.setIcon(back_icon)
        self.back_button.setObjectName("back_button")
        self.horizontal_layout_1.addWidget(self.back_button)
        self.refresh_button = QtWidgets.QPushButton(self.central_widget)
        self.refresh_button.setIcon(refresh_icon)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontal_layout_1.addWidget(self.refresh_button)
        self.stop_button = QtWidgets.QPushButton(self.central_widget)
        self.stop_button.setIcon(stop_icon)
        self.stop_button.setObjectName("stop_button")
        self.horizontal_layout_1.addWidget(self.stop_button)
        
        self.line_edit = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit.setObjectName("line_edit")
        self.horizontal_layout_1.addWidget(self.line_edit)
        self.horizontal_layout_2.addLayout(self.horizontal_layout_1)
        self.progressBar = QtWidgets.QProgressBar(self.central_widget)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())

        self.progressBar.setSizePolicy(size_policy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontal_layout_2.addWidget(self.progressBar)

        self.go_button = QtWidgets.QPushButton(self.central_widget)
        self.go_button.setIcon(go_icon)
        self.go_button.setObjectName("go_button")
        self.horizontal_layout_2.addWidget(self.go_button)

        self.vertical_layout.addLayout(self.horizontal_layout_2)

        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.vertical_layout.addWidget(self.tabWidget)

        main_window.setCentralWidget(self.central_widget)
        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate

        main_window.setWindowTitle(_translate("main_window", "PyQt Browser 1.1.0a"))

        self.new_button.setText(_translate("main_window", "New Page"))
        self.home_button.setText(_translate("main_window", "Home Page"))
        self.forward_button.setText(_translate("main_window", "Forward"))
        self.back_button.setText(_translate("main_window", "Back"))
        self.refresh_button.setText(_translate("main_window", "Refresh"))
        self.stop_button.setText(_translate("main_window", "Stop"))
        self.go_button.setText(_translate("main_window", "GO"))

# import browser_bate_1_1_0.res_rc

# -*- coding: utf-8 -*-

#   2019/3/22 0022 上午 11:20     

__author__ = 'RollingBear'

from PyQt5 import QtCore, QtGui, QtWidgets

from ticket_query.event_class import event_class


class ui_main(object):

    def setupUI(self, main_window):
        event = event_class()

        main_window.setObjectName('MainWindow')
        main_window.resize(800, 600)
        main_window.setStyleSheet('font: 10pt \"Microsoft YaHei UI\";')

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName('central widget')
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(0, 0, 798, 43)
        self.widget.setObjectName('widget')

        self.horizontal_layout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontal_layout.setContentsMargins(10, 1, 1, 3)
        self.horizontal_layout.setSpacing(15)
        self.horizontal_layout.setObjectName('horizontal layout')

        self.label = QtWidgets.QLabel(self.label)
        self.label.setObjectName('label')
        self.horizontal_layout.addWidget(self.label)

        self.line_edit = QtWidgets.QLineEdit(self.widget)
        self.line_edit.setMaximumSize(QtCore.QSize(742, 16777215))
        self.line_edit.setObjectName('line edit')
        self.horizontal_layout.addWidget(self.line_edit)

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName('label_2')
        self.horizontal_layout.addWidget(self.label_2)

        self.line_edit_2 = QtWidgets.QLineEdit(self.widget)
        self.line_edit_2.setObjectName('line edit 2')
        self.horizontal_layout.addWidget(self.line_edit_2)

        self.date_edit = QtWidgets.QDateEdit(self.widget)
        self.date_edit.setDate(QtCore.QDate(2019, 1, 1))
        self.date_edit.setObjectName('date edit')
        self.horizontal_layout.addWidget(self.date_edit)

        self.push_button = QtWidgets.QPushButton(self.widget)
        self.push_button.setObjectName('push button')
        self.horizontal_layout.addWidget(self.push_button)

        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(0, 40, 791, 561))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName('scroll area')

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 789, 559))
        self.scroll_area_widget_contents.setObjectName('scroll area widget content')

        self.table_widget = QtWidgets.QTableWidget(self.scroll_area_widget_contents)
        self.table_widget.setGeometry(QtCore.QRect(0, 0, 791, 561))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())

        self.table_widget.setSizePolicy(size_policy)
        self.table_widget.setBaseSize(QtCore.QSize(0, 0))
        self.table_widget.setObjectName('table widget')
        self.table_widget.setColumnCount(5)
        self.table_widget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        self.table_widget.horizontalHeader().setDefaultSectionSize(155)
        self.table_widget.verticalHeader().setDefaultSectionSize(47)
        self.table_widget.verticalHeader().setMinimumSectionSize(45)

        self.line = QtWidgets.QFrame(self.scroll_area_widget_contents)
        self.line.setGeometry(QtCore.QRect(0, 23, 784, 31))
        self.line.setToolTipDuration(0)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')

        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        self.push_button.clicked.connect(
            lambda: event.search(self.table_widget, self.line_edit.text(), self.line_edit_2.text(),
                                 self.date_edit.date().toPyDate()))
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate('main window', 'main window'))

        self.label.setText(_translate('main_window', 'From'))
        self.label_2.setText(_translate('main_window', 'To'))
        self.push_button.setText(_translate('main_window', 'search'))

        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate('main_window', '车次'))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate('main_window', '出发时间'))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate('main_window', '到站时间'))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate('main_window', '硬卧'))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate('main_window', '硬座'))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ui_main()
    ui.setupUI(main_window)
    main_window.show()
    sys.exit(app.exec_())

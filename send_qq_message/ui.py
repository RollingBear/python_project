# -*- coding: utf-8 -*-

#   2019/3/28 0028 下午 1:31     

__author__ = 'RollingBear'

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QMessageBox, QLabel, QLineEdit, QGridLayout, QPushButton
from PyQt5.QtWidgets import QInputDialog, QRadioButton
from time import sleep

from send_qq_message.config import config
from send_qq_message.send_message import send_msg


class main_window(QWidget):

    def __init__(self):

        super().__init__()

        self._target = ''
        self._class_ready = False

        self.msg_sender = send_msg()
        self.conf = config('\\config.ini')

        self.setWindowTitle("Mr.YE's Dark Whisper 0.1.0a")
        self.init_ui()
        self.show()

    def init_ui(self):

        self.widget_set = QGridLayout()
        self.setLayout(self.widget_set)
        self.widget_set.setSpacing(10)

        self.target_msg = QLabel(self)
        self.target_msg.setText("Target window's name: ")
        self.widget_set.addWidget(self.target_msg, 0, 0)
        self.target_label = QLabel(self)
        self.widget_set.addWidget(self.target_label, 0, 1)

        self.target_name = QLineEdit(self)
        self.target_name.setPlaceholderText('Input your target window name')
        self.widget_set.addWidget(self.target_name, 1, 1)
        self.target_name.textChanged[str].connect(self.target_change)
        self.lock_btn = QPushButton('Lock Target', self)
        self.lock_btn.setCheckable(True)
        self.widget_set.addWidget(self.lock_btn, 1, 2)
        self.lock_btn.clicked[bool].connect(self.target_lock)

        self.send_mes = QLabel(self)
        self.send_mes.setText('The simple sent message: ')
        self.widget_set.addWidget(self.send_mes, 2, 0)
        self.mes_label = QLabel(self)
        self.widget_set.addWidget(self.mes_label, 2, 1)

        self.message = QLineEdit(self)
        self.message.setPlaceholderText('Input sent message:')
        self.widget_set.addWidget(self.message, 3, 1)
        self.message.textChanged[str].connect(self.msg_change)
        self.msg_lock_btn = QPushButton('Lock Message', self)
        self.msg_lock_btn.setCheckable(True)
        self.widget_set.addWidget(self.msg_lock_btn, 3, 2)
        self.msg_lock_btn.clicked[bool].connect(self.msg_lock)

        self.interval_modify_btn = QPushButton('Send Interval Modify', self)
        self.widget_set.addWidget(self.interval_modify_btn, 4, 0)
        self.interval_modify_btn.clicked.connect(self._interval_modify)

        self.rand_msg_list_modify_btn = QPushButton('Random List Modify', self)
        self.widget_set.addWidget(self.rand_msg_list_modify_btn, 4, 1)
        self.rand_msg_list_modify_btn.clicked.connect(lambda: self._msg_list_modify('rand'))
        self.sequ_msg_list_modify_btn = QPushButton('Sequential List Modify', self)
        self.widget_set.addWidget(self.sequ_msg_list_modify_btn, 4, 2)
        self.sequ_msg_list_modify_btn.clicked.connect(lambda: self._msg_list_modify('sequ'))

        self.mode_simple_btn = QRadioButton('Simple Mode', self)
        self.mode_simple_btn.setChecked(False)
        self.widget_set.addWidget(self.mode_simple_btn, 5, 0)
        self.mode_simple_btn.toggled.connect(self.mode_simple)
        self.mode_random_btn = QRadioButton('Random Mode', self)
        self.mode_random_btn.setChecked(False)
        self.widget_set.addWidget(self.mode_random_btn, 5, 1)
        self.mode_random_btn.toggled.connect(self.mode_random)
        self.mode_sequential_btn = QRadioButton('Sequential Mode', self)
        self.mode_sequential_btn.setChecked(False)
        self.widget_set.addWidget(self.mode_sequential_btn, 5, 2)
        self.mode_sequential_btn.toggled.connect(self.mode_sequential)

        self.start_btn = QPushButton('F I R E !', self)
        self.widget_set.addWidget(self.start_btn, 6, 2)
        self.start_btn.clicked.connect(self.start)
        self.stop_btn = QPushButton('Stop', self)
        self.widget_set.addWidget(self.stop_btn, 6, 3)
        self.stop_btn.clicked.connect(self.stop)

        self.enable_all(False)

    def target_change(self, text):
        self.target_label.setText(text)
        self.target_label.adjustSize()

    def target_lock(self, pressed):
        target_name = self.target_name.displayText()
        print(target_name)
        print(pressed)

        if '熊' in target_name:
            QMessageBox.question(self, '???', 'You dare do this?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            quit()

        self.mode_simple_btn.setEnabled(True)
        self.mode_random_btn.setEnabled(True)
        self.mode_sequential_btn.setEnabled(True)

        if pressed:
            self.target_name.setEnabled(False)
            self._class_ready = True
            self.msg_sender.__init__(target_name)
        else:
            self.target_name.setEnabled(True)
            self._class_ready = False
            self.msg_sender.__init__(None)

    def msg_change(self, text):
        self.mes_label.setText(text)
        self.mes_label.adjustSize()

    def msg_lock(self, pressed):
        if pressed:
            self.message.setEnabled(False)
            self.msg_sender.message_modify(self.message.displayText())
        else:
            self.message.setEnabled(True)

    def _interval_modify(self, event):
        value, ok = QInputDialog.getDouble(self, 'interval modify', 'Input interval', float(self.msg_sender.interval),
                                           0.01, 1000, 2)
        self.msg_sender.interval_modify(value)

    def mode_simple(self):
        if self.mode_simple_btn.isChecked():
            self.mode_random_btn.setChecked(False)
            self.mode_sequential_btn.setChecked(False)

            self.rand_msg_list_modify_btn.setEnabled(False)
            self.sequ_msg_list_modify_btn.setEnabled(False)
            self.message.setEnabled(True)
            self.msg_lock_btn.setEnabled(True)

            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)

    def mode_random(self):
        if self.mode_random_btn.isChecked():
            self.mode_simple_btn.setChecked(False)
            self.mode_sequential_btn.setChecked(False)

            self.rand_msg_list_modify_btn.setEnabled(True)
            self.sequ_msg_list_modify_btn.setEnabled(False)
            self.message.setEnabled(False)
            self.msg_lock_btn.setEnabled(False)

            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)

    def mode_sequential(self):
        if self.mode_sequential_btn.isChecked():
            self.mode_simple_btn.setChecked(False)
            self.mode_random_btn.setChecked(False)

            self.rand_msg_list_modify_btn.setEnabled(False)
            self.sequ_msg_list_modify_btn.setEnabled(True)
            self.message.setEnabled(False)
            self.msg_lock_btn.setEnabled(False)

            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)

    def start(self):
        if self.mode_simple_btn.isChecked():
            self.msg_sender.send_simple()
        elif self.mode_random_btn.isChecked():
            self.msg_sender.send_random()
        elif self.mode_sequential_btn.isChecked():
            self.msg_sender.send_sequential()

    def stop(self):
        self.msg_sender.running_state_change(False)
        sleep(0.1)
        self.msg_sender.running_state_change(True)

    def _msg_list_modify(self, type):
        self.msg_sender.msg_list_modify(type)

    def enable_all(self, state):
        self.message.setEnabled(state)
        self.msg_lock_btn.setEnabled(state)
        self.interval_modify_btn.setEnabled(state)
        self.rand_msg_list_modify_btn.setEnabled(state)
        self.sequ_msg_list_modify_btn.setEnabled(state)
        self.mode_simple_btn.setEnabled(state)
        self.mode_random_btn.setEnabled(state)
        self.mode_sequential_btn.setEnabled(state)
        self.start_btn.setEnabled(state)
        self.stop_btn.setEnabled(state)

    def center(self):
        geomotery = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        geomotery.moveCenter(center_point)
        self.move(geomotery.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

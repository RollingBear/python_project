# -*- coding: utf-8 -*-

#   2019/3/27 0027 上午 9:40     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QGridLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLineEdit, QWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWidgets import QHeaderView


class url_input(QLineEdit):

    def __init__(self, browser):
        super(url_input, self).__init__()

        self.browser = browser

        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())
        self.browser.load(url)


class requests_table(QTableWidget):
    header = ['url', 'status', 'content-type']

    def __init__(self):
        super(requests_table, self).__init__()

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(self.header)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def update(self, data):

        last_row = self.rowCount()
        next_row = last_row + 1
        self.setRowCount(next_row)

        for col, dat in enumerate(data, 0):
            if not dat:
                continue
            self.setItem(last_row, col, QTableWidgetItem(dat))


class manager(QNetworkAccessManager):

    def __init__(self, table):
        QNetworkAccessManager.__init__(self)

        self.finished.connect(self._finished)
        self.table = table

    def _finished(self, reply):
        headers = reply.rawHeaderPairs()
        headers = {str(k): str(v) for k, v in headers}

        content_type = headers.get('Content-Type')
        url = reply.url().toString()

        status = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
        status, ok = status.toInt()
        self.table.update([url, str(status), content_type])


class javaSctipt_evaluator(QLineEdit):

    def __init__(self, page):
        super(javaSctipt_evaluator, self).__init__()
        self.page = page
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        frame = self.page.currentFrame()
        result = frame.evaluateJavaScript(self.text())


class action_input_box(QLineEdit):

    def __init__(self, page):

        super(action_input_box, self).__init__()

        self.page = page
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):

        frame = self.page.currentFrame()
        action_string = str(self.text()).lower()

        if action_string == 'b':
            self.page.triggerAction(QWebEnginePage.Back)
        elif action_string == 'f':
            self.page.triggerAction(QWebEnginePage.Forward)
        elif action_string == 's':
            self.page.triggerAction(QWebEnginePage.Stop)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    grid = QGridLayout()
    browser = QWebEngineView()
    _url_input = url_input(browser)
    _requests_table = requests_table()

    _manager = manager(_requests_table)
    page = QWebEnginePage()
    _js_eval = javaSctipt_evaluator(page)
    act_input = action_input_box(page)
    browser.setPage(page)

    grid.addWidget(_url_input, 1, 0)
    grid.addWidget(browser, 2, 0)
    grid.addWidget(_requests_table, 3, 0)
    grid.addWidget(_js_eval, 4, 0)
    grid.addWidget(_js_eval, 5, 0)

    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()

    sys.exit(app.exec_())
